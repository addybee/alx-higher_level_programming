#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except BaseException as e:
        print("Exception: {}".format(e), file=stderr)
        res = None
    finally:
        return res
