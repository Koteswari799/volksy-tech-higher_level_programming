#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print('{:d}'.format(value))
        return True
    except ValueError as err:
    except Exception as err:
        print('Exception: {}'.format(err),file=stderr)
        return False
