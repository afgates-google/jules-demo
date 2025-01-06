
def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y == 0:
    return "Division by zero!"
  return x / y

import math

def sqrt(x):
    if x < 0:
        return "Cannot calculate square root of a negative number"
    return math.sqrt(x)


def cube(x):
    return x * x * x

