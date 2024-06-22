#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test"""
# pylint: disable=missing-function-docstring

import io
import unittest
from unittest import mock

from dvg_debug_functions import (
    dprint,
    tprint,
    ANSI,
    print_fancy_traceback as pft,
)


class TestAll(unittest.TestCase):
    def test_dprint(self):
        with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            dprint("No color")

        assert fake_stdout.getvalue() == "No color\n"

    def test_dprint_in_red(self):
        with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            dprint("In red", ANSI.RED)

        assert fake_stdout.getvalue() == "\x1b[1;31mIn red\x1b[1;37m\n"

    def test_tprint(self):
        with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            tprint("No color")

        assert fake_stdout.getvalue()[-9:] == "No color\n"

    def test_pft(self):
        try:
            0 / 0  # type: ignore
        except ZeroDivisionError as err:
            with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
                pft(err, 1)

            assert (
                fake_stdout.getvalue().split("\n")[-2]
                == "\x1b[1;31mZeroDivisionError: \x1b[1;37mdivision by zero"
            )

    def test_pft_overshoot_callstack(self):
        try:
            0 / 0  # type: ignore
        except ZeroDivisionError as err:
            with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
                pft(err, 50)

            assert (
                fake_stdout.getvalue().split("\n")[-2]
                == "\x1b[1;31mZeroDivisionError: \x1b[1;37mdivision by zero"
            )

    def test_pft_err_as_string(self):
        with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            pft("Custom error string", 1)

        assert (
            fake_stdout.getvalue().split("\n")[-2]
            == "\x1b[1;31mError: \x1b[1;37mCustom error string"
        )


if __name__ == "__main__":
    unittest.main()
