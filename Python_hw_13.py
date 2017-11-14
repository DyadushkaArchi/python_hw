import math

#======================================================================
#task 13
#======================================================================
#Пользователь вводит длины катетов прямоугольного треугольника.
#Написать функцию, которая вычислит площадь треугольника и его периметр.
#Результат работы функции вывести на печать.

def Sq_Pm(catheter1, catheter2):
    square = (catheter1 * catheter2) / 2

    hypotenuse = math.sqrt((catheter1)**2 + (catheter2)**2)
    perimeter = hypotenuse + catheter1 + catheter2
    return square, perimeter

catheter1 = 3
catheter2 = 4
example = Sq_Pm(catheter1, catheter2)
print(example)
