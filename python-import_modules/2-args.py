#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenght = len(sys.argv)
    if lenght <= 1:
        print(" 0 argument. ")
    elif lenght == 2:
        print("{:d} argument:".format(length - 1))
    else:
        print("{:d} argument:".format(length - 1))
    for i in range(1,lenght):
        print("{:d}: {:s}".format(i, sys.argv[i]))
