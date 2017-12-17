# В двумерном массиве отсортировать четные столбцы по возрастанию,
# а нечетные - по убыванию


def even_sort(matrix):
       for i in range(len(matrix[0])):
              current_number1 = matrix[0][i]
              current_number2 = matrix[1][i]
              if i % 2 == 0:
                  if current_number1 > current_number2:
                         matrix[0][i] = current_number2
                         matrix[1][i] = current_number1
              else:
                   if current_number1 < current_number2:
                         matrix[0][i] = current_number2
                         matrix[1][i] = current_number1

       return matrix


matrix = [[1, 2, 3, 4, 5, 6],
          [7, 8, 9, 10, 11, 0]]

print(even_sort(matrix))