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

import wx

import MainGui

import EditConvProfileDialog
from DataObjects import *

# Implementing ConvProfile
class ConvProfileDialog(MainGui.ConvProfileDialog):
    def __init__(self, parent, **kwargs):
	MainGui.ConvProfileDialog.__init__(self, parent)

        # Receive or load list of profiles?
        # To load I need access to parent.config
        profiles = kwargs.get('profiles', dict())
        for name, convprof in profiles.iteritems():
            self.m_listBoxProfiles.Append(name, convprof)

        if self.m_listBoxProfiles.GetCount():
            self.m_listBoxProfiles.SetSelection(0)


    def OnCancelButtonClick(self, event):
        event.Skip()
        # Signal cancelation and exit
        self.EndModal(wx.ID_CANCEL)


    def OnOKButtonClick(self, event):
        event.Skip()

        # Compile profiles from listBox clientdata objects
        self.profiles = dict()
        for itemId in xrange(0, self.m_listBoxProfiles.GetCount()):
            convprof = self.m_listBoxProfiles.GetClientData(itemId)
            self.profiles[convprof.name] = convprof
        # Signal success and exit
        self.EndModal(wx.ID_OK)


    def OnButtonClickAdd(self, event):
        event.Skip()

        # Show add dialog
        dlg = EditConvProfileDialog.EditConvProfileDialog(self)
        retcode = dlg.ShowModal()
        dlg.Destroy()

        if retcode != wx.ID_OK:
            return

        # Create profile object, create entry in listbox, attach object
        convprof = DataConvProf(dlg.name, dlg.outdir, dlg.ext, dlg.format, dlg.voldiv)
        itemId = self.m_listBoxProfiles.Append(convprof.name, convprof)
        self.m_listBoxProfiles.SetSelection(itemId)
        

    def OnButtonClickEdit(self, event):
        event.Skip()

        itemId = self.m_listBoxProfiles.GetSelection()
        if itemId == wx.NOT_FOUND:
            return
        # Get object to edit
        prof = self.m_listBoxProfiles.GetClientData(itemId)

        # Show Edit Dialog
        dlg = EditConvProfileDialog.EditConvProfileDialog(
            self, name=prof.name, ext=prof.ext,
            outdir=prof.outdir, format=prof.format, voldiv=prof.voldiv)
        retcode = dlg.ShowModal()
        dlg.Destroy()

        if retcode != wx.ID_OK:
            return

        # Create new profile, update entry in listbox, attach new object
        prof = DataConvProf(dlg.name, dlg.outdir, dlg.ext, dlg.format, dlg.voldiv)
        self.m_listBoxProfiles.SetString(itemId, prof.name)
        self.m_listBoxProfiles.SetClientData(itemId, prof)


    def OnButtonClickDelete(self, event):
        event.Skip()

        # Find selection
        itemId = self.m_listBoxProfiles.GetSelection()
        if itemId == wx.NOT_FOUND:
            return

        # Delete item
        self.m_listBoxProfiles.Delete(itemId)
        if itemId:
            itemId -= 1 # Select previous if possible

        if self.m_listBoxProfiles.GetCount():
            # Ensure something can be selected and do so
            self.m_listBoxProfiles.SetSelection(itemId)
