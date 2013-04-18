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

import collections
import datetime
import struct
import os

class EndOfBars(Exception):
    pass


class BarAbstract(object):
    sep = ','

    def __init__(self, reverse=False):
        self.dt = datetime.datetime.max if not reverse else datetime.datetime.min
        self.o = 0.0
        self.h = float('-inf')
        self.l = float('inf')
        self.c = 0.0
        self.v = 0
        self.oi = 0


    def update(self, bar, reverse=False):
        if not reverse:
            if bar.dt < self.dt:
                self.o = bar.o
            self.c = bar.c
            self.oi = bar.oi
        else:
            self.o = bar.o
            if bar.dt > self.dt:
                self.c = bar.c
                self.oi = bar.oi

        if bar.h > self.h:
            self.h = bar.h
        if bar.l < self.l:
            self.l = bar.l

        self.v += bar.v/10
        self.dt = bar.dt


    def __str__(self):
        return '%s%s%.2f%s%.2f%s%.2f%s%.2f%s%d%s%d' % \
               (str(self.dt), self.sep, \
               self.o, self.sep, \
               self.h, self.sep, \
               self.l, self.sep, \
               self.c, self.sep, \
               self.v, self.sep, \
               self.oi)


class Bar(BarAbstract):

    def __init__(self, ifile):
        BarAbstract.__init__(self)
        data = ifile.read(self.size)
        if len(data) < self.size:
            raise EndOfBars

        data = struct.unpack(self.fmt, data)
        self.unpack(data)
        self.convertDateTime()

    def convertDateTime(self):
        # Years are stored as if they had 500 days
        y, md = divmod(self.dc, 500)
        # Months are stored as if they had 32 days
        m, d = divmod(md, 32)
        self.dt = datetime.datetime(y, m, d)

    def unpack(self, data):
        self.o, self.h, self.l, self.c, self.v, self.oi = data


class BarEoD(Bar):
    size = 28
    fmt = 'IffffII'

    def unpack(self, data):
        self.dc = data[0]
        Bar.unpack(self, data[1:])


class BarMinute(Bar):
    size = 32
    fmt = 'IIffffII'

    def unpack(self, data):
        self.dc, self.tc = data[0:2]
        Bar.unpack(self, data[2:])

    def convertDateTime(self):
        Bar.convertDateTime(self)
        # Daily Time is stored in seconds
        hhmm, ss = divmod(self.tc, 60)
        hh, mm = divmod(hhmm, 60)
        # NOTE: Vchart seems to always store in CET - 2
        # hh += 2
        self.dt = self.dt.replace(hour=hh, minute=mm, second=ss)


class DailyBars(object):
    def __init__(self, ifile, printbars=False):
        self.bars = list()
        while True:
            try:
                bar = BarEoD(ifile)
            except EndOfBars:
                break

            if printbars:
                sep = ','
                line = '%s%s%s%s' % (bar.dt.strftime('%Y%m%d'), sep, '0', sep)
                line += '%.2f%s%.2f%s%.2f%s%.2f%s%d%s%d' % (bar.o, sep, bar.h, sep, bar.l, sep, bar.c, sep, bar.v, sep, bar.oi)
                print line

            self.bars.append(bar)


    def export(self, ofile, sep=',', name=None, bartype=None, header=True, datefmt='%Y%m%d', timeout=True, voldiv=None):
        if header:
            if name is not None:
                ofile.write('Name%s' % sep)
            if bartype is not None:
                ofile.write('BarType%s' % sep)

            ofile.write('Date%s' % sep)

            if timeout is not None:
                ofile.write('Time%s' % sep)

            ofile.write('Open%sHigh%sLow%sClose%sVolume%sOpenInterest' % (sep, sep, sep, sep, sep))
            ofile.write('\r\n')


        for bar in self.bars:
            if name is not None:
                ofile.write('%s%s' % (name, sep))
            if bartype is not None:
                ofile.write('%s%s' % (bartype, sep))

            ofile.write('%s%s' % (bar.dt.strftime(datefmt), sep))
            if timeout is not None:
                ofile.write('%s%s' % ('0', sep))
            vol = bar.v if not voldiv else bar.v/voldiv
            ofile.write('%.2f%s%.2f%s%.2f%s%.2f%s%d%s%d' % (bar.o, sep, bar.h, sep, bar.l, sep, bar.c, sep, vol, sep, bar.oi))
            ofile.write('\r\n')


class MinuteBars(object):
    def __init__(self, ifile, printbars=False):

        self.daybars = collections.defaultdict(list)

        while True:
            try:
                bar = BarMinute(ifile)
            except EndOfBars:
                break
            self.daybars[bar.dt].append(bar)

            if printbars:
                sep = ','
                line = '%s%s%s%s' % (bar.dt.strftime('%Y%m%d'), sep, bar.dt.strftime('%H%M%S'), sep)
                line += '%.2f%s%.2f%s%.2f%s%.2f%s%d%s%d' % (bar.o, sep, bar.h, sep, bar.l, sep, bar.c, sep, bar.v, sep, bar.oi)
                print line


    def spitout(self, ofile, bar,  name=None, bartype=None):
        if name is not None:
            ofile.write('%s%s' % (name, sep))
        if bartype is not None:
            ofile.write('%s%s' % (bartype, sep))
        ofile.write('%s%s%s%s' % (bar.dt.strftime('%Y%m%d'), sep, bar.dt.strftime('%H%M%S'), sep))
        ofile.write('%.2f%s%.2f%s%.2f%s%.2f%s%d%s%d' % (bar.o, sep, bar.h, sep, bar.l, sep, bar.c, sep, bar.v, sep, bar.oi))
        ofile.write('\r\n')


    def export(self, ofile, sep=',', name=None, bartype=None, header=True, compression=1, days=1):
        if header:
            if name is not None:
                ofile.write('Name%s' % sep)
            if bartype is not None:
                ofile.write('BarType%s' % sep)

            ofile.write('Date%sTime%sOpen%sHigh%sLow%sClose%sVolume%sOpenInterest' % (sep, sep, sep, sep, sep, sep, sep))
            ofile.write('\r\n')


        # see how many days we can yield
        daykeys = self.daybars.keys()
        daykeys.sort()
        maxdays = min(days, len(self.daybars))

        for daykey in daykeys[-maxdays]:
            bars = iter(self.daybars[daykey])
            # There has to be at least 1 bar or else there would be no day
            curbar = bars.next()
            curtm = curbar.tm

            while True:
                try:
                    bar = bars.next()
                except StopIteration:
                    # The last calculated bar has to be spitout
                    self.spitout(ofile, curbar, name, bartpye)
                    break
                else:
                    # Number of minutes of bar
                    barminutes = bar.tm.hour * 60 + bar.tm.minute
                    rem = barminutes % compression
                    if rem:
                        curbar.update(bar)
                        curbar.tm = curtm # keep time of first bar
                    else:
                        self.spitout(ofile, curbar, name, bartype)
                        curbar = bar
                        curtm = curbar.tm
                

class MinuteBarsRev(object):
    def __init__(self, ifile, printbars=False, compression=1, period=1):

        self.bars = list()

        # Go to end of file (we iterate backwards)
        ifile.seek(0, os.SEEK_END)

        # Create a first void bar
        curbar = None
        curdt = datetime.date.min
        count = 0

        compdelta = datetime.timedelta(minutes=compression)

        while True:
            # Move to beginning of bar to be read
            try:
                ifile.seek(-BarMinute.size, os.SEEK_CUR)
            except IOError:
                # FIXME: we need to store the last active bar (if any)
                if curbar:
                    curbar.dt = curbar.dt + compdelta
                    self.bars.append(curbar)
                # exit the loop
                raise EndOfBars

            bar = BarMinute(ifile)
            if bar.dt.date() != curdt:
                # If the day has changed, we obviously have to change the bar
                count += 1
                if count == period:
                    break
                if curbar:
                    curbar.dt += compdelta
                    self.bars.append(curbar)

                # 1st bar or bar stored ... nullify
                curbar = None
                # Do it only if we change the day
                curdt = bar.dt.date()

            if not curbar:
                curbar = BarAbstract(reverse=True)

            # Update the bar (or fill it for the 1st time)
            curbar.update(bar, reverse=True)

            # first bar of the day could be an edge bar
            barminutes = (bar.dt.hour * 60 + bar.dt.minute) % compression
            if not barminutes:
                curbar.dt += compdelta
                # 1. store current bar in list
                self.bars.append(curbar)

                # bar stored ... nullify
                curbar = None

            # Move the cursor to the beginner of the bar just read
            ifile.seek(-BarMinute.size, os.SEEK_CUR)

            if printbars:
                sep = ','
                line = '%s%s%s%s' % (bar.dt.strftime('%Y%m%d'), sep, bar.dt.strftime('%H%M%S'), sep)
                line += '%.2f%s%.2f%s%.2f%s%.2f%s%d%s%d' % (bar.o, sep, bar.h, sep, bar.l, sep, bar.c, sep, bar.v, sep, bar.oi)
                print line

        self.bars.reverse()


    def export(self, ofile, sep=',', name=None, bartype=None, header=True):
        if header:
            if name is not None:
                ofile.write('Name%s' % sep)
            if bartype is not None:
                ofile.write('BarType%s' % sep)

            ofile.write('Date%sTime%sOpen%sHigh%sLow%sClose%sVolume%sOpenInterest' % (sep, sep, sep, sep, sep, sep, sep))
            ofile.write('\r\n')


        for bar in self.bars:
            if name is not None:
                ofile.write('%s%s' % (name, sep))
            if bartype is not None:
                ofile.write('%s%s' % (bartype, sep))
            ofile.write('%s%s%s%s' % (bar.dt.strftime('%Y%m%d'), sep, bar.dt.strftime('%H%M%S'), sep))
            ofile.write('%.2f%s%.2f%s%.2f%s%.2f%s%d%s%d' % (bar.o, sep, bar.h, sep, bar.l, sep, bar.c, sep, bar.v, sep, bar.oi))
            ofile.write('\r\n')


class LastDayFromMin(BarAbstract):

    def __init__(self, ifile, printbars=False):
        # Data is assumed to be an open file - use StringIO if you have a string

        BarAbstract.__init__(self, reverse=True)
        today = datetime.date.today()

        # Go to end
        ifile.seek(0, os.SEEK_END)

        while True:
            # Move to beginning of bar to be read
            ifile.seek(-BarMinute.size, os.SEEK_CUR)
            bar = BarMinute(ifile)
            if bar.dt.date() < today:
                break

            self.update(bar, reverse=True)
            if printbars:
                sep = ','
                line = '%s%s%s%s' % (bar.dt.strftime('%Y%m%d'), sep, bar.dt.strfmtime('%Y%M%S'), sep)
                line += '%.2f%s%.2f%s%.2f%s%.2f%s%d%s%d' % (bar.o, sep, bar.h, sep, bar.l, sep, bar.c, sep, bar.v, sep, bar.oi)
                print line

            # Rewind the currently read bar
            ifile.seek(-BarMinute.size, os.SEEK_CUR)
