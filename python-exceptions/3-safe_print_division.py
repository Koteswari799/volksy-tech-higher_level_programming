#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b
        return c
    except:
        return None
    finally:
        print('Inside result: {:d}'.format(c))
