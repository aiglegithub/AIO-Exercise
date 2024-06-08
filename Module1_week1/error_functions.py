# Error functions

# Absolute error function
def cal_ae(y, y_hat):
    return abs(y - y_hat)
y = 1
y_hat = 6
assert cal_ae(y, y_hat) == 5
y = 2
y_hat = 9
print(cal_ae(y, y_hat))

# Squared error function
def cal_se(y, y_hat):
    return (y - y_hat) ** 2
y = 4
y_hat = 2
assert cal_se(y, y_hat) == 4
print(cal_se(2, 1))