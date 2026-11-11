# user defined function

# function define
def calc_gst(price): #parameters
    new_price = price + price * 0.18
    # print(new_price)
    return new_price

calc_gst(200) # arguments
print(calc_gst(300))

# in-built functions
# print();
# len(marks)

# module function
from math import sqrt, log2
print(sqrt(36))
print(log2(8))

import random
print(random.random()) # from 0 to 1 it generates the random number
print(random.randint(10, 50)) # it generates the random integer between range