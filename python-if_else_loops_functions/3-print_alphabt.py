#!/usr/bin/python3
for i in range(ord('a'), ord('z')+1):
    if i not in 'qe':
        continue
        print("{:c}".format(i), end = "")
