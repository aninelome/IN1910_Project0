from math import factorial

def add(x, y):
    return x + y

def factorial(n):
    """Returns the factorial of n"""
    fact = 1
    for i in range(1,n+1): 
        fact *= i 
    return fact


def sin(x,N):
    """Taylor series expansion of the sin function"""
    s = 0
    for n in range(0,N+1):
        s += ((-1)**n)*(x**((2*n)+1))/factorial((2*n)+1)
    return s

def divide(x,y):
    return x/y

def less_than(original,n):
    """Returns a new list of the elements in the 
    original list that were smaller than n"""
    less_than = [i for i in original if i < n]
    return less_than

def innerprod(x,y):
    """Calculates the innerproduct of x and y"""
    v = 0
    for i in range(len(x)):
        v += x[i]*y[i]
    return v



# Testing making a change


# Testing making a change2
