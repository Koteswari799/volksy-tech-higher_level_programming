#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(0, x):
        try:
            print('{:d}'.format([i]), end ="")
            count = count + 1
        except:
            pass
        print('')
        return count
