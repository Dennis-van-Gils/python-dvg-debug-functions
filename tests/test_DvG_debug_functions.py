from DvG_debug_functions import dprint, ANSI, print_fancy_traceback as pft
from unittest import mock
import io



def test_dprint():
    with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
        dprint("In red", ANSI.RED)

    assert fake_stdout.getvalue() == '\x1b[1;31mIn red\x1b[1;37m\n'
    


def test_pft():
    try:
        0/0
    except ZeroDivisionError as err:
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            pft(err, 1)
            
        assert fake_stdout.getvalue().split('\n')[-2] == \
            '\x1b[1;31mZeroDivisionError: \x1b[1;37mdivision by zero'