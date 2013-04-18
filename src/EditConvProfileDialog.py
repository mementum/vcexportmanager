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

# Implementing EditConvProfile
class EditConvProfileDialog(MainGui.EditConvProfileDialog):
    def __init__(self, parent, **kwargs):
	MainGui.EditConvProfileDialog.__init__(self, parent)

        self.name = kwargs.get('name', '')
        self.m_textCtrlName.SetValue(self.name)

        self.ext = kwargs.get('ext', '')
        self.m_textCtrlExt.SetValue(self.ext)

        self.outdir = kwargs.get('outdir', '')
        self.m_dirPickerOutDir.SetPath(self.outdir)

        self.voldiv = kwargs.get('voldiv', 1)
        self.m_textCtrlVolDiv.SetValue(str(self.voldiv))

        # DO NOTHING - FIXME
        self.format = kwargs.get('format', '')


    def OnOKButtonClick(self, event):
        event.Skip()
        self.name = self.m_textCtrlName.GetValue()
        self.outdir = self.m_dirPickerOutDir.GetPath()
        self.ext = self.m_textCtrlExt.GetValue()
        self.format = '' # DO NOTHING FIXME
        self.voldiv = int(self.m_textCtrlVolDiv.GetValue())

        if not self.name:
            wx.Message('The profile needs a name or else it cannot be saved', 'Error')
            return
        self.EndModal(wx.ID_OK)


    def OnCancelButtonClick(self, event):
        event.Skip()
        self.EndModal(wx.ID_CANCEL)
