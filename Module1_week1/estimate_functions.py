# Estimate functions

import math

# Cos estimation function
def approx_cos(x, n):
    cos = 0
    for i in range(n):
        cos += ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
    return cos
assert round(approx_cos(x=1, n=10), 2) == 0.54
print(round(approx_cos(x=3.14, n=10), 2))

# Sin estimation function
def approx_sin(x, n):
    sin = 0
    for i in range(n):
        sin += ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
    return sin
assert round(approx_sin(x=1, n=10), 4) == 0.8415
print(round(approx_sin(x=3.14, n=10), 4))

# Sinh estimation function
def approx_sinh(x, n):
    sinh = 0
    for i in range(n):
        sinh += (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
    return sinh
assert round(approx_sinh(x=1, n=10), 2) == 1.18
print(round(approx_sinh(x=3.14, n=10), 2))

# Cosh estimation function
def approx_cosh(x, n):
    cosh = 0
    for i in range(n):
        cosh += (x ** (2 * i)) / math.factorial(2 * i)
    return cosh
assert round(approx_cosh(x=1, n=10), 2) == 1.54
print(round(approx_cosh(x=3.14, n=10), 2))