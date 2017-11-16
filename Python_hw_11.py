import math


#=======================================================================
#task 11
#=======================================================================

def radian (degree):
    result = (degree * math.pi) / 180
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



