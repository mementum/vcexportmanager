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

# Implementing DataConversion
class DataConversionDialog(MainGui.DataConversionDialog):
    def __init__(self, parent, **kwargs):
	MainGui.DataConversionDialog.__init__(self, parent)

        # save flag
        self.save = False
        # Source name
        srcname = kwargs.get('srcname', '')
        self.m_textCtrlSrcName.SetValue(srcname)
        # Dest name
        self.dstname = kwargs.get('dstname', '')
        if not self.dstname:
            self.dstname = srcname
        self.m_textCtrlDstName.SetValue(self.dstname)
        # Comment
        self.comment = kwargs.get('comment', '')
        self.m_textCtrlComment.SetValue(self.comment)
        # Active for export
        self.active = kwargs.get('active', True)
        self.m_checkBoxActive.SetValue(self.active)

        # Check for multi flag to activate "Next"
        self.multi = kwargs.get('multi', False)
        if self.multi:
            self.m_buttonCancel.Hide()
            self.m_panelMulti.Show()
            self.Layout()


    def OnButtonClickSave(self, event):
        event.Skip()
        # Save the data
        self.dstname = self.m_textCtrlDstName.GetValue()
        self.active = self.m_checkBoxActive.GetValue()
        self.comment = self.m_textCtrlComment.GetValue()

        self.save = True
        # Exit indicating success
        if not self.multi:
            self.EndModal(wx.ID_OK)


    def OnButtonClickCancel(self, event):
        event.Skip()
        # Exit indicating cancelation
        self.EndModal(wx.ID_CANCEL)


    def OnButtonClickMultiNext(self, event):
        event.Skip()
        self.EndModal(wx.ID_YES)


    def OnButtonClickMultiSkip(self, event):
        event.Skip()
        self.EndModal(wx.ID_CANCEL)
