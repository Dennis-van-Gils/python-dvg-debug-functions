.. image:: https://img.shields.io/pypi/v/dvg-debug-functions
    :target: https://pypi.org/project/dvg-debug-functions
.. image:: https://img.shields.io/pypi/pyversions/dvg-debug-functions
    :target: https://pypi.org/project/dvg-debug-functions
.. image:: https://travis-ci.org/Dennis-van-Gils/python-dvg-debug-functions.svg?branch=master
    :target: https://travis-ci.org/Dennis-van-Gils/python-dvg-debug-functions
.. image:: https://coveralls.io/repos/github/Dennis-van-Gils/python-dvg-debug-functions/badge.svg?branch=master
    :target: https://coveralls.io/github/Dennis-van-Gils/python-dvg-debug-functions?branch=master
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
.. image:: https://img.shields.io/badge/License-MIT-purple.svg
    :target: https://github.com/Dennis-van-Gils/python-dvg-debug-functions/blob/master/LICENSE.txt

DvG_debug_functions
===================
*Provides functions for printing debug information to the terminal output.*

- Github: https://github.com/Dennis-van-Gils/python-dvg-debug-functions
- PyPI: https://pypi.org/project/dvg-debug-functions

Installation:

    ``pip install dvg-debug-functions``

API
===

Functions
---------
* ``print_fancy_traceback(err=None, back: int = 3, show_full_paths: bool = False)``

    Print the exception or the current regular call-stack traceback to the
    terminal, using ANSI color codes that mimic the IPython command shell.

        Args:
            err (``Exception`` | ``str`` | ``None``, optional):
                When ``err`` is of type ``Exception``, then an exception traceback will
                be printed. When ``err`` is of another type, then the current regular
                call-stack traceback will be printed.

                Default: ``None``

            back (``int``, optional):
                Depth of the traceback to print.

                Default: ``3``

            show_full_paths (``bool``, optional):
                Shows the full filepath in the traceback when True, otherwise just
                the filename.

                Default: ``False``

    Example output:

    .. image:: images/print_fancy_traceback.png


* ``dprint(str_msg: str, ANSI_color: str = None)``

    'Debug' print a single line to the terminal with optional ANSI color
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


* ``tprint(str_msg: str, ANSI_color: str = None)``

    Identical to ``dprint()``, but now prepended with a ``time.perf_counter()``
    timestamp.

Classes
-------

    .. code-block:: python

        class ANSI:
            NONE    = ""
            RED     = "\033[1;31m"
            GREEN   = "\033[1;32m"
            YELLOW  = "\033[1;33m"
            BLUE    = "\033[1;34m"
            PURPLE  = "\033[1;35m"  # aka MAGENTA
            MAGENTA = "\033[1;35m"
            CYAN    = "\033[1;36m"
            WHITE   = "\033[1;37m"
