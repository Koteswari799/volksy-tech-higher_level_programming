#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        return result
    except:
        return None
        return result
    finally:
        print('inside result:{}'.format(result))
