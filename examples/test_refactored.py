'''
This program calculates the factorial of a number.
It is an example program for the Pylint poster.
The function name doesn't follow the snake case.
'''
def computeFactorial(num):#pylint: disable=invalid-name
    '''Returns the factorial of a number.'''
    if num == 1:
        return 1
    return num*computeFactorial(num-1)

print(computeFactorial(10))
