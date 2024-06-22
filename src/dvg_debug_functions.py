#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provides functions for neatly printing debug information to the terminal
output, well-suited for multithreaded programs.
"""
__author__ = "Dennis van Gils"
__authoremail__ = "vangils.dennis@gmail.com"
__url__ = "https://github.com/Dennis-van-Gils/python-dvg-debug-functions"
__date__ = "22-06-2024"
__version__ = "2.5.0"

import os
import sys
import time
import traceback
import inspect
from typing import Union

dprint_mutex = None
try:
    from qtpy import QtCore

    dprint_mutex = QtCore.QMutex()
except ImportError:
    pass

# Setting this global module variable to `True` or `False` will overrule the
# argument `show_full_paths` in `print_fancy_traceback()`.
OVERRULE_SHOW_FULL_PATHS = None


class ANSI:
    NONE = ""
    RED = "\033[1;31m"
    GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    BLUE = "\033[1;34m"
    PURPLE = "\033[1;35m"  # aka MAGENTA
    MAGENTA = "\033[1;35m"
    CYAN = "\033[1;36m"
    WHITE = "\033[1;37m"


def dprint(str_msg: str, ANSI_color: Union[str, None] = None):
    """'Debug' print a single line to the terminal with optional ANSI color
    codes. There is a lot of overhead using this print statement, but it is
    particularly well-suited for multithreaded PyQt programs where multiple
    threads are each printing information to the same terminal. The ``dprint()``
    function ensure that each line sent to the terminal will remain as a
    continious single line, whereas a regular ``print()`` statement will likely
    result in the lines getting mixed up.

    The line will be terminated with a newline character and the terminal output
    buffer is forced to flush before and after every print. In addition, if
    PyQt5 is present in the Python environment, then a mutex lock will be
    obtained and released again for each ``dprint()`` execution.
    """
    # Explicitly ending the string with a newline '\n' character, instead
    # of letting the print statement end it for you (end='\n'), fixes the
    # problem of single lines getting printed to the terminal with
    # intermittently delayed newlines when coming from different threads.
    # I.e. it prevents:
    # >: Output line of thread 1Output line of thread 2   (\n)
    # >:                                                  (\n)
    # and makes sure we get:
    # >: Output line of thread 1                          (\n)
    # >: Output line of thread 2                          (\n)

    if dprint_mutex is not None:
        locker = QtCore.QMutexLocker(dprint_mutex)

    sys.stdout.flush()
    if ANSI_color is None:
        print(f"{str_msg}\n", end="")
    else:
        print(f"{ANSI_color}{str_msg}{ANSI.WHITE}\n", end="")
    sys.stdout.flush()

    if dprint_mutex is not None:
        locker.unlock()


def tprint(str_msg: str, ANSI_color: Union[str, None] = None):
    """Identical to ``dprint()``, but now prepended with a ``time.perf_counter()``
    timestamp.
    """
    dprint(f"{time.perf_counter():.4f} {str_msg}", ANSI_color)


def print_fancy_traceback(
    err=None, back: int = 3, show_full_paths: bool = False
):
    """Print the exception or the current regular call-stack traceback to the
    terminal, using ANSI color codes that mimic the IPython command shell.

    Args:
        err (``Exception`` | ``str`` | ``None``, optional):
            When ``err`` is of type ``Exception``, then an exception traceback
            will be printed. When ``err`` is of another type, then the current
            regular call-stack traceback will be printed.

            Default: ``None``

        back (``int``, optional):
            Depth of the traceback to print.

            Default: ``3``

        show_full_paths (``bool``, optional):
            Shows the full filepath in the traceback when True, otherwise just
            the filename.

            Default: ``False``
    """

    def print_frame(filename, line_no, frame_name):
        print(
            ANSI.CYAN
            + "File "
            + ANSI.GREEN
            + f'"{filename}"'
            + ANSI.CYAN
            + ", line "
            + ANSI.GREEN
            + f"{line_no}"
            + ANSI.CYAN
            + ", in "
            + ANSI.PURPLE
            + f"{frame_name}"
            + ANSI.WHITE
        )

    print(
        "\n"
        + ANSI.WHITE
        + "Fancy traceback "
        + ANSI.CYAN
        + "(most recent call last)"
        + ANSI.WHITE
        + ":"
    )

    if isinstance(err, Exception):
        # Exception traceback
        etype, evalue, tb = sys.exc_info()
        stack = traceback.extract_tb(tb)
        stack = stack[-back:]

        for frame in stack:
            if OVERRULE_SHOW_FULL_PATHS is not None:
                file_descr = (
                    frame.filename
                    if OVERRULE_SHOW_FULL_PATHS
                    else os.path.basename(frame.filename)
                )
            else:
                file_descr = (
                    frame.filename
                    if show_full_paths
                    else os.path.basename(frame.filename)
                )

            print_frame(file_descr, frame.lineno, frame.name)

        print(f"----> {stack[-1].line}")
        if etype is None:
            print(": ", end="")
        else:
            print(ANSI.RED + f"{etype.__name__}: ", end="")
        print(ANSI.WHITE + f"{evalue}")

    else:
        # Regular call stack traceback
        stack = inspect.stack()
        stack.reverse()
        stack = stack[-back - 1 : -1]

        for frame in stack:
            if OVERRULE_SHOW_FULL_PATHS is not None:
                file_descr = (
                    frame.filename
                    if OVERRULE_SHOW_FULL_PATHS
                    else os.path.basename(frame.filename)
                )
            else:
                file_descr = (
                    frame.filename
                    if show_full_paths
                    else os.path.basename(frame.filename)
                )

            print_frame(file_descr, frame.lineno, frame.function)

        if isinstance(err, str):
            print(ANSI.RED + "Error: " + ANSI.WHITE + f"{err}")
