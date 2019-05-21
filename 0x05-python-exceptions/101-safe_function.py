#!/usr/bin/python3
def safe_function(fct, *args):

    import sys

    try:
        return fct(*args)

    except Exception as ddd:
        print("Exception:", ddd, file=sys.stderr)
        return None
