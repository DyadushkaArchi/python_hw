import math


#=======================================================================
#task 11
#=======================================================================

def radian (degree):
    transfer = 0.0174533
    result = degree * transfer
    return result

angle = 60
result = radian(angle)
print(math.cos(result))

angle = 45
result = radian(angle)
print(math.cos(result))

angle = 40
result = radian(angle)
print(math.cos(result))



