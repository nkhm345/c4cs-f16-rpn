#!/usr/bin/env python3
def calculate(string):
    stack = []
 
    for val in string.split(' '):
        if val in ['-', '+', '*', '/']:
            op1 = stack.pop()
            op2 = stack.pop()
            if val=='-': result = op2 - op1
            if val=='+': result = op2 + op1
            if val=='*': result = op2 * op1
            if val=='/': result = op2 / op1
            stack.append(result)
        else:
            try:
                stack.append(float(val))
            except:
            	raise TypeError
 
    return stack.pop()
def main():
    while True:
        calculate(input("rpn calc> "))
if __name__ == '__main__': # Note that's "underscore underscore n a m e ..."
    main()