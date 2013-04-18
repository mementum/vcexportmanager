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
import itertools
import os.path

class DataSource(object):
    codegen = itertools.count(0)

    def __init__(self, fullpath):
        # AutoInc code for unique identification
        self.code = next(DataSource.codegen)

        self.fullpath = fullpath
        fdir, self.fname  = os.path.split(fullpath)
        _, self.dirname = os.path.split(fdir)
        self.name, _ = os.path.splitext(self.fname)


class DataDest(object):
    def __init__(self, name='', comment='', active=True):
        self.name = name
        self.comment = comment
        self.active = active


class DataConvProf(object):
    def __init__(self, name, outdir='', ext='', format='', voldiv=1):
        self.name = name
        self.outdir = outdir
        self.ext = ext
        self.format = format
        self.voldiv = voldiv
