# Activation functions

import math
# Sigmoid function
def cal_sig(x):
    return 1 / (1 + math.exp(-x))
assert round(cal_sig(3), 2) == 0.95
print(round(cal_sig(2), 2))

# Elu function
alpha = 0.01
def cal_elu(x, alpha):
    if not isinstance(alpha, float):
        raise TypeError("Input must be a number")
    if alpha <= 0:
        raise ValueError("Input must be a positive number")
    if x >= 0:
        return x
    else:
        return alpha * (math.exp(x) - 1)
assert round(cal_elu(1, alpha), 2) == 1
print(round(cal_elu(-1, alpha), 2))

# Activation function
def cal_activation_func(x, act_name):
    if act_name == 'sigmoid':
        return cal_sig(x)
    elif act_name == 'elu':
        return cal_elu(x, alpha)
    elif act_name == 'relu':
        return max(0, x)
    else:
        raise ValueError("Invalid activation function")
assert cal_activation_func(x=1, act_name='relu') == 1
print(round(cal_activation_func(x=3, act_name='sigmoid'), 2))