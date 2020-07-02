from dvg_debug_functions import (
    dprint,
    tprint,
    ANSI,
    print_fancy_traceback as pft,
)
from unittest import mock
import io


def test_dprint():
    with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
        dprint("No color")

    assert fake_stdout.getvalue() == "No color\n"


def test_dprint_in_red():
    with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
        dprint("In red", ANSI.RED)

    assert fake_stdout.getvalue() == "\x1b[1;31mIn red\x1b[1;37m\n"


def test_tprint():
    with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
        tprint("No color")

    assert fake_stdout.getvalue()[-9:] == "No color\n"


def test_pft():
    try:
        0 / 0
    except ZeroDivisionError as err:
        with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            pft(err, 1)

        assert (
            fake_stdout.getvalue().split("\n")[-2]
            == "\x1b[1;31mZeroDivisionError: \x1b[1;37mdivision by zero"
        )


def test_pft_overshoot_callstack():
    try:
        0 / 0
    except ZeroDivisionError as err:
        with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            pft(err, 50)

        assert (
            fake_stdout.getvalue().split("\n")[-2]
            == "\x1b[1;31mZeroDivisionError: \x1b[1;37mdivision by zero"
        )


def test_pft_err_as_string():
    with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
        pft("Custom error string", 1)

    assert (
        fake_stdout.getvalue().split("\n")[-2]
        == "\x1b[1;31mError: \x1b[1;37mCustom error string"
    )


def test_pft():
    try:
        0 / 0
    except ZeroDivisionError as err:
        with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            pft(err, 1)


def test_pft_descr_abbr():
    try:
        0 / 0
    except ZeroDivisionError as err:
        err.abbreviation = "abbr"
        err.description = "descr"
        with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            pft(err, 1)

        assert (
            fake_stdout.getvalue().split("\n")[-2]
            == "\x1b[1;31mZeroDivisionError: \x1b[1;37mabbr: descr"
        )
