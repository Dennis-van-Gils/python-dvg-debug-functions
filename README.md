[![PyPI version](https://badge.fury.io/py/dvg-debug-functions.svg?kill_cache=1)](https://badge.fury.io/py/dvg-debug-functions)
[![Build Status](https://travis-ci.org/Dennis-van-Gils/python-dvg-debug-functions.svg?branch=master&kill_cache=1)](https://travis-ci.org/Dennis-van-Gils/python-dvg-debug-functions)
[![Coverage Status](https://coveralls.io/repos/github/Dennis-van-Gils/python-dvg-debug-functions/badge.svg?branch=master&kill_cache=1)](https://coveralls.io/github/Dennis-van-Gils/python-dvg-debug-functions?branch=master)

# DvG_debug_functions
Provides functions for printing debug information to the terminal output.

# dprint()
```Python
dprint(str_msg, ANSI_color=None) 
````
'Debug' print a single line to the terminal with optional ANSI color codes. The line will be terminated with a newline character and the terminal output buffer is forced to flush before and after every print. In addition, if PyQt5 is present in the Python environment, then a mutex lock will be obtained and released again for each dprint execution.

There is a lot of overhead using this print statement, but it is particularly well-suited for multithreaded PyQt programs where multiple threads are each printing information to the same terminal. The `dprint` function ensure that each line sent to the terminal will remain as a continious single line, whereas a regular `print` statement will likely result in the lines getting mixed up.

# print_fancy_traceback()
```Python
print_fancy_traceback(err, back=3)
```
Prints the exception `err` to the terminal with a traceback that is `back` deep, using ANSI color codes that mimic the IPython command shell.

Example output:

![print_fancy_traceback.png](https://raw.githubusercontent.com/Dennis-van-Gils/python-dvg-debug-functions/master/images/print_fancy_traceback.png)

