import numpy as np

data = 5
data_np = np.array([5, 6])
a = np.arange(15).reshape(3, 5)
print (data_np)

def f_to_c(f):
    celsius = (f-32)*(5/9)
    return celsius

print (f_to_c(data_np))