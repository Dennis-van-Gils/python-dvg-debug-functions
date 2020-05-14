# DvG_debug_functions
Provides functions for printing debug information to the terminal output.

# dprint()
```Python
dprint(str_msg, ANSI_color=None) 
````
'Debug' print a single line to the terminal with optional ANSI color codes. The line will be terminated with a newline character and the terminal output buffer is forced to flush before and after every print. In addition, if PyQt5 is present in the Python environment, then a mutex lock will be obtained and released again for each dprint execution.

There is a lot of overhead using this print statement, but it is particularly well-suited for multithreaded PyQt programs where multiple threads are printing information to the same terminal. On the contrary, a regular `print` statement will likely result in mixed up text output.

# print_fancy_traceback()
```Python
print_fancy_traceback(err, back=3)
```
Prints the exception `err` to the terminal with a traceback that is `back` deep, using ANSI color codes that mimic the IPython command shell.

Example output:
![print_fancy_traceback.png](https://raw.githubusercontent.com/Dennis-van-Gils/python-dvg-debug-functions/master/images/print_fancy_traceback.png)

