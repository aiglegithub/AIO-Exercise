# is_number function
import math
def is_number(n):
    if not isinstance(n, (int, float)):
        return False
    return math.isnan(n) == False and math.isinf(n) == False
assert is_number(3) == 1.0
assert is_number('-2a') == 0.0
print(is_number(1))
print(is_number('n'))