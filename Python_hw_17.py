import math

#==============================================================================
#task 17
#==============================================================================
#Написать функцию решения квадратного уравнения.

def solve_quadratic_equation(a, b, c): # return 2 values
    discriminant = b**2 - 4 * a * c

    if discriminant > 0:
        x1 = (- b + math.sqrt(discriminant)) / 2 * a
        x2 = (- b - math.sqrt(discriminant)) / 2 * a
        return x1, x2
    if discriminant == 0:
        x1 = (- b + math.sqrt(discriminant)) / 2 * a
        return x1, None
    else:
        return None, None


example = solve_quadratic_equation(1, 4, 20)
print(example)


