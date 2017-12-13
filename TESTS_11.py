# В двумерном массиве отсортировать четные столбцы по возрастанию,
# а нечетные - по убыванию



def even_sort(matrix):
       for i in range(len(matrix)):
              if i % 2 == 0:
                     matrix[i] = matrix.sort
              else:
                     matrix[i] = matrix.sort(key=lambda matrix : matrix.sort(reverse=True))
       return matrix



