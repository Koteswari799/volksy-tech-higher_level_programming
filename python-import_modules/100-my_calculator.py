#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    fromm sys import agrv
    if len(agrv) != 4:
        print('./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    operator = agrv[2]
    n1 = int(agrv[1])
    n2 = int(agv[3])
    if operator == '+':
        print('{} + {} = {}'.format(n1, n2, add(n1, n2)))
    elif operator == '-':
        print('{} + {} = {}'.format(n1, n2, sub(n1, n2)))
    elif  operator == '*':
        print('{} + {} = {}'.format(n1, n2, mul(n1, n2)))
    elif operator == '/':
        print('{} + {} ={}'.format(n1. n2, div(n1, n2)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)


