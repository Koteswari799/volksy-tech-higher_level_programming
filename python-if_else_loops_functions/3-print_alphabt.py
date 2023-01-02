#!/usr/bin/python3
for i in range(ord('a'),ord('z')):
    if i not in 'qe':
        print("{:c}".format(i), end = "")
