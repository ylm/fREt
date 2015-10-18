#!/usr/bin/python3

# Copyright (c) 2015 Yannick Lamarre
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:

# Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.

# Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

__author__ = 'Yannick Lamarre'
__license__ = 'BSD License'

import sys
import os
import io
import argparse
import curses
import xdlrc_parser

def clip_cursor(curpos_tup, maxyx_tup, ystep, xstep):
    retval = [0, 0]
    retval[0] = curpos_tup[0] + ystep*2
    retval[1] = curpos_tup[1] + xstep*2
    if retval[0] < 0:
        retval[0] = maxyx[0] - retval[0] + 2
    elif retval[0] > maxyx[0]:
        retval[0] = retval[0] - maxyx[0] - 2
    if retval[1] < 0:
        retval[1] = maxyx[1] - retval[1] + 2
    elif retval[1] > maxyx[1]:
        retval[1] = retval[1] - maxyx[1] - 2
    return retval


def main():
    parser = argparse.ArgumentParser(description='fpga Reverse Engineering tool')
    parser.add_argument('file', nargs='?',
                       help='File to edit')
    args = parser.parse_args()
    if args.file:
        device_layout = xdlrc_parser.load_xdlrc(args.file)
    else:
        device_layout = None
    curses.wrapper(main_window, device_layout)
    
    
def main_window(stdscr, device_layout):
    tilesym_dict = {}
    stdscr.clear()
    cursor_posx = 0
    cursor_posy = 0
    if device_layout:
        wrkpad = curses.newpad(device_layout.tile_rows*2, device_layout.tile_cols*2)
        for irow in range(0, device_layout.tile_rows):
            for icol in range(0, device_layout.tile_cols):
                itile = device_layout.tile_list[irow*device_layout.tile_cols + icol]
                wrkpad.addstr(irow*2, icol*2, itile[4]._val[0]+' ')
        while True:
            stdscr.move(cursor_posy+1, cursor_posx+1)
            wrkpad.refresh(cursor_posy, cursor_posx, 1, 1, 30, 120)
            curses.curs_set(1)
            stdscr.refresh()
            c_key = stdscr.getkey()

            if c_key == 'q':
                break
            elif c_key == 'h':
                pass
            elif c_key == 'j':
                pass
            elif c_key == 'k':
                pass
            elif c_key == 'l':
                pass
            elif c_key == 'y':
                pass
            elif c_key == 'u':
                pass
            elif c_key == 'b':
                pass
            elif c_key == 'n':
                pass
            else:
                pass


def manage_tile_dictionary(device_layout):
    """Manages the dictionary for screen's tile symbols

    The dictionary mapping a character to be displayed to a tile name
    I

    Args:
        device_layout: A DeviceLayout object containing device information

    Returns:
        A dict mapping a tile name to a character to be displayed

    """
    return_value = []

main()
