#!/usr/bin/env python
# -*- coding: latin-1; py-indent-offset:4 -*-
################################################################################
# 
# This file is part of VCExportManager
#
# VCExportManager is a graphical interface to automate Visualchart (R)
# data files conversion to Ascii (CSV) format
#
# Copyright (C) 2012 Sensible Odds Ltd.
#
# The development site is at:
#
#    http://code.google.com/p/vcexportmanager/
#
# VCExportManager is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# VCExportManager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with VCExportManager. If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

NAME = 'VisualChart Export Manager'
VERSION='1.00'

# Python Standard Modules
import glob
import itertools
import os
import os.path

# Python Extra Libraries
import wx

# Python Own Modules
import MainGui
import AboutDialog
import ConvProfileDialog
import DataConversionDialog
from DataObjects import *

# Python Own Sub-Modules
import vcdata.vcbars as vcbars

# Implementing MainFrame
class MainFrame(MainGui.MainFrame):
    MarketMap = {
        '0001' : 'CBOE', '0003' : 'NASDAQ',
        '0013' : 'HEX', '0015' : 'EUREX',
        '0034' : 'FOREX', '0060': 'MEFF',
        '0095' : 'S&P', '0096' : 'INTL',
        '0097' : 'EUROSTOXX', '0098': 'DAX', 
        }

    def __init__(self, parent):
	MainGui.MainFrame.__init__(self, parent)
        self.SetTitle('%s %s' % (NAME, VERSION))

        # Operating System Details for column sizes
        winDC = wx.ClientDC(self)
        self.avgcharwidth = winDC.GetCharWidth() # for column lengths

        # Initialize Destination ListCtrl
        colidx = itertools.count()
        self.m_listCtrlDst.InsertColumn(next(colidx), 'Active') # Active 6 chars
        self.m_listCtrlDst.InsertColumn(next(colidx), 'InName') # InName 15 chars
        self.m_listCtrlDst.InsertColumn(next(colidx), 'OutName') # OutName 15 chars
        self.m_listCtrlDst.InsertColumn(next(colidx), 'Comment') # Comment 255 chars
        colcharlens = [6, 15, 15, 255]
        for i in range(self.m_listCtrlDst.GetColumnCount()):
            self.m_listCtrlDst.SetColumnWidth(i, colcharlens[i] * self.avgcharwidth)

        # Initialize TreeCtrl - The root is hidden
        self.m_treeCtrlSources.AddRoot('')

        # Initialize Config object
        self.config = wx.Config('VCExportManager', 'VCExportManager');
        self.config.SetRecordDefaults(True)

        # Dictionary of codes to map sources and destinations
        self.codemap = dict()

        # Dictionary of available datasources
        self.sources = dict()

        # Default VisualChart BaseDirectory
        self.basedir = self.config.Read('BaseDir', '')
        if self.basedir:
            self.m_dirPickerBaseDir.SetPath(self.basedir)
            self.FillTree()

        # Dictionary of Data Destinations
        self.dests = dict()

        # Read Saved Destinations from Configuration
        self.config.SetPath('/DataDest')
        contflag, srcname, nindex = self.config.GetFirstGroup()
        idx = 0
        while contflag:
            dstname = self.config.Read('%s/name' % srcname, '')
            comment = self.config.Read('%s/comment' % srcname, '')
            active = self.config.ReadBool('%s/active' % srcname, True)

            # FIXME - Need to do a check with -1 codes by conversion
            code = self.codemap.get(srcname, -1)
            dest = DataDest(dstname, comment, active)
            self.dests[code] = dest

            colidx = itertools.count(1)
            self.m_listCtrlDst.InsertStringItem(idx, str(dest.active))
            self.m_listCtrlDst.SetItemData(idx, code)
            self.m_listCtrlDst.SetStringItem(idx, next(colidx), srcname)
            self.m_listCtrlDst.SetStringItem(idx, next(colidx), dest.name)
            self.m_listCtrlDst.SetStringItem(idx, next(colidx), dest.comment)
            idx += 1

            contflag, srcname, nindex = self.config.GetNextGroup(nindex)

        self.config.SetPath('..')
        # End Read Saved Destinations from Configuration

        # Begin Read Saved Conversion Profiles from Configuration
        self.convprofiles = dict()
        self.config.SetPath('/ConvProfile')
        contflag, name, nindex = self.config.GetFirstGroup()
        while contflag:
            outdir = self.config.Read('%s/outdir' % name, '')
            ext = self.config.Read('%s/ext' % name, '')
            format = self.config.Read('%s/format' % name, '')
            voldiv = self.config.ReadInt('%s/voldiv' % name, 1)

            convprof = DataConvProf(name, outdir, ext, format, voldiv)
            self.convprofiles[name] = convprof
            self.m_choiceConvProfiles.Append(name, convprof)

            contflag, name, nindex = self.config.GetNextGroup(nindex)

        self.config.SetPath('..')
        # Edn Read Saved Conversion Profiles from Configuration

        if self.m_choiceConvProfiles.GetCount():
            self.m_choiceConvProfiles.SetSelection(0) # Set a selection


    def OnButtonClickAbout(self, event):
        event.Skip()
        dlg = AboutDialog.AboutDialog(self)
        dlg.ShowModal()
        dlg.Destroy()
        

    def OnDirChangedBaseDir(self, event):
        event.Skip()
        self.FillTree()


    def FillTree(self):
        # Get VisualChartBaseDir - Save it to Config
        self.basedir = self.m_dirPickerBaseDir.GetPath()
        self.config.Write('BaseDir', self.basedir)

        # Clear TreeCtrl And Sources Dict
        self.sources = dict()
        rootitem = self.m_treeCtrlSources.GetRootItem()
        self.m_treeCtrlSources.DeleteChildren(rootitem)

        # Scan the Directory - Take the '01' into account
        # Assign a code in 'self.codemap'
        # to map it to destinations - use the 'code' as the
        # PyData in the TreeCtrl

        if os.path.isdir(self.basedir):
            for dirname in sorted(os.listdir('%s/01' % self.basedir)):
                if not os.path.isdir('%s/01/%s' % (self.basedir, dirname)):
                    # we expect only directories
                    continue

                if dirname in self.MarketMap:
                    dirnamelabel = '%s - %s' % (dirname, self.MarketMap[dirname])
                else:
                    dirnamelabel = dirname
                # Add the directory to the tree - receive treeItem
                diritem = self.m_treeCtrlSources.AppendItem(rootitem, dirnamelabel)
                # self.m_treeCtrlSources.SetItemHasChildren(diritem)

                # Get the daily data files and add them to the diritem
                fullpaths = glob.glob('%s/01/%s/*.fd' % (self.basedir, dirname))
                for fullpath in sorted(fullpaths):
                    source = DataSource(fullpath)
                    self.codemap[source.name] = source.code
                    self.sources[source.code] = source
                    item = self.m_treeCtrlSources.AppendItem(diritem, source.name)
                     # Save codes as PyData
                    self.m_treeCtrlSources.SetPyData(item, source.code)


    def OnTreeItemRightClickSources(self, event):
        event.Skip()
        treeItemId = event.GetItem()
        self.m_treeCtrlSources.SelectItem(treeItemId)

        self.m_menuTreeSources.treeItemId = treeItemId
        self.m_treeCtrlSources.PopupMenu(self.m_menuTreeSources, event.GetPoint())


    def OnTreeItemActivatedSource(self, event):
        event.Skip()
        treeItemId = event.GetItem()

        code = self.m_treeCtrlSources.GetPyData(treeItemId)
        # Edit instead of add if a destination exists
        self.EditDest(code, self.dests.get(code, None))


    # Add Souce to Destinations
    def OnButtonClickAdd(self, event):
        event.Skip()

        # Selection retrieval and check
        treeItemId = self.m_treeCtrlSources.GetSelection()
        if not treeItemId.IsOk():
            return # no selection returned

        code = self.m_treeCtrlSources.GetPyData(treeItemId)
        # Edit instead of add if a destination exists
        self.EditDest(code, self.dests.get(code, None))


    # Double Click on ListCtrl
    def OnListItemActivatedDst(self, event):
        event.Skip()
        itemId = event.GetIndex()
        if itemId == wx.NOT_FOUND:
            return
        code = self.m_listCtrlDst.GetItemData(itemId)
        # Edit the double-clicked destination
        self.EditDest(code, self.dests.get(code, None))


    def EditDest(self, code, dest=None, multi=False):
        # The method returns the "retcode" of the dialog to allow for
        # edition of "multiple" destinations in a row
        
        # Get the source
        source = self.sources[code]

        # If no destination was provided create a dummy one
        if not dest:
            dest = DataDest(source.name)

        # Creat dialog
        dlg = DataConversionDialog.DataConversionDialog(
            self, srcname=source.name,
            dstname=dest.name, active=dest.active, comment=dest.comment,
            multi=multi)
        retcode = dlg.ShowModal()
        dlg.Destroy()
        if not dlg.save:
            return retcode # Return if not to be saved

        # Update/Fill in values in (dummy) destination
        dest.name = dlg.dstname
        dest.comment = dlg.comment
        dest.active = dlg.active

        self.dests[code] = dest # add/update destination

        # The data has to go to the registry
        self.config.Write('DataDest/%s/name' % source.name, dest.name) # output name
        self.config.Write('DataDest/%s/comment' % source.name, dest.comment) # comment
        self.config.WriteBool('DataDest/%s/active' % source.name, dest.active) # if it shall be exported

        # The data has to go to be added/edited to/in the ListControl
        idx = self.m_listCtrlDst.FindItemData(-1, code)
        if idx == wx.NOT_FOUND:
            # No destination with the code available in ListCtrl
            colidx = itertools.count(1) 
            idx = self.m_listCtrlDst.GetItemCount()
            # Insert new item at the end
            self.m_listCtrlDst.InsertStringItem(idx, str(dest.active))
            self.m_listCtrlDst.SetItemData(idx, code) # Assign the code as itemdata
        else:
            # Destination found - set the first column 
            colidx = itertools.count(0)
            self.m_listCtrlDst.SetStringItem(idx, next(colidx), str(dest.active))

        # Set the additional 3 columns
        self.m_listCtrlDst.SetStringItem(idx, next(colidx), source.name)
        self.m_listCtrlDst.SetStringItem(idx, next(colidx), dest.name)
        self.m_listCtrlDst.SetStringItem(idx, next(colidx), dest.comment)

        return retcode


    def OnButtonClickEdit(self, event):
        event.Skip()

        selcount = self.m_listCtrlDst.GetSelectedItemCount()
        if not selcount:
            # Say nothing ... the user has to select something
            return

        multi = (selcount > 1) # set the "multiple edition flag"

        itemId = self.m_listCtrlDst.GetFirstSelected()
        while itemId != wx.NOT_FOUND:
            code = self.m_listCtrlDst.GetItemData(itemId)
            retcode = self.EditDest(code, self.dests.get(code, None), multi=multi)
            if retcode != wx.ID_YES:
                # OK would be in "single edition", "YES" indicates the
                # User wants to carry on editing
                break
            itemId = self.m_listCtrlDst.GetNextSelected(itemId)


    def OnButtonClickRemove(self, event):
        # Remove the Selected ones
        event.Skip()
        selections = list() # list to compile selections
        itemId = self.m_listCtrlDst.GetFirstSelected()
        while itemId != wx.NOT_FOUND:
            selections.append(itemId)
            itemId = self.m_listCtrlDst.GetNextSelected(itemId)

        self.RemoveDest(selections) # do the work


    def OnButtonClickRemoveAll(self, event):
        event.Skip()
        self.RemoveDest(range(0, self.m_listCtrlDst.GetItemCount())) # remove all


    def OnButtonClickRemoveActive(self, event):
        event.Skip()
        self.RemoveActiveFlag(actflag=True) # get only the active ones


    def OnButtonClickRemoveNonActive(self, event):
        event.Skip()
        self.RemoveActiveFlag(actflag=False) # get only the inactive ones


    def RemoveActiveFlag(self, actflag):
        flaglist = list() # list to compile active/inactive ones
        for itemId in xrange(0, self.m_listCtrlDst.GetItemCount()):
            code = self.m_listCtrlDst.GetItemData(itemId)
            dest = self.dests[code]
            if dest.active == actflag:
                flaglist.append(itemId)

        self.RemoveDest(flaglist) # do the job


    def RemoveDest(self, remlist):
        # Remove destinations
        for itemId in reversed(remlist):
            code = self.m_listCtrlDst.GetItemData(itemId)
            dest = self.dests[code]
            source = self.sources[code]

            # 1. Delete from list ctrl
            self.m_listCtrlDst.DeleteItem(itemId)
            # 2. Delete from Registry
            self.config.DeleteGroup('/DataDest/%s' % source.name)
            # 3. Delete from dictionary
            del self.dests[code]

            
    def OnButtonClickEditProfiles(self, event):
        # Edit the ChoiceControl profiles list
        # Show the dialog
        dlg = ConvProfileDialog.ConvProfileDialog(self, profiles=self.convprofiles)
        retcode = dlg.ShowModal()
        dlg.Destroy()
        if retcode == wx.ID_CANCEL:
            return # make no changes

        self.convprofiles = dlg.profiles # Get profiles from dialog objected
        self.m_choiceConvProfiles.Clear() # clear choice
        self.config.DeleteGroup('/ConvProfile') # clear registry
        # Add to Choice and to Registry
        for profname, convprof in self.convprofiles.iteritems():
            self.m_choiceConvProfiles.Append(profname, convprof)
            self.config.Write('/ConvProfile/%s/outdir' % profname, convprof.outdir)
            self.config.Write('/ConvProfile/%s/ext' % profname, convprof.ext)
            self.config.Write('/ConvProfile/%s/format' % profname, convprof.format)
            self.config.WriteInt('/ConvProfile/%s/voldiv' % profname, int(convprof.voldiv))

        if self.m_choiceConvProfiles.GetCount:
            self.m_choiceConvProfiles.SetSelection(0) # set selection if possible

    def DoConversion(self, codes):
        # Conversion profile
        itemId = self.m_choiceConvProfiles.GetSelection()
        if itemId == wx.NOT_FOUND:
            wx.MessageBox('No profile seleted for conversion', 'Conversion Error')
            return

        convprof = self.m_choiceConvProfiles.GetClientData(itemId)

        # Codes have been compiled. They can now be exported in sequence
        for code in codes:
            src = self.sources[code]
            dst = self.dests[code]

            self.m_statusBar.SetStatusText('Exporting %s to %s' % (src.name, dst.name))

            try:
                ifile = open(src.fullpath, 'rb')
            except:
                # FIXME: show error for this file
                pass
            else:
                eod = vcbars.DailyBars(ifile)
                ifile.close()


            ofname = '%s/%s' % (convprof.outdir, dst.name)
            if convprof.ext:
                ofname += '.%s' % convprof.ext
            try:
                ofile = open(ofname, 'wb')
            except:
                # FIXME: show error for this file
                pass
            else:
                eod.export(ofile, datefmt='%Y/%m/%d', timeout=None, voldiv=convprof.voldiv)
                ofile.close()

            self.m_statusBar.SetStatusText('Exported %s to %s' % (src.name, dst.name))

        self.m_statusBar.SetStatusText('Exporting finished')


    def OnButtonClickConvert(self, event):
        event.Skip()

        codes = list()
        itemId = self.m_listCtrlDst.GetFirstSelected()
        while itemId != wx.NOT_FOUND:
            code = self.m_listCtrlDst.GetItemData(itemId)
            codes.append(code)
            itemId = self.m_listCtrlDst.GetNextSelected(itemId)

        self.DoConversion(codes)


    def OnButtonClickConvertAll(self, event):
        event.Skip()

        codes = list()
        for itemId in xrange(0, self.m_listCtrlDst.GetItemCount()):
            code = self.m_listCtrlDst.GetItemData(itemId)
            codes.append(code)

        self.DoConversion(codes)


    def OnButtonClickConvertActive(self, event):
        event.Skip()

        codes = list()
        for itemId in xrange(0, self.m_listCtrlDst.GetItemCount()):
            code = self.m_listCtrlDst.GetItemData(itemId)
            if self.dests[code].active:
                codes.append(code)

        self.DoConversion(codes)
