# task 22


def group_by_surname(list_of_enrollees): # returns 4 ints
    lst_a_i = []
    lst_j_p = []
    lst_q_t = []
    lst_u_z = []

    for i in range(len(list_of_enrollees)):
        lst = list_of_enrollees[i-1]
        name_surname = lst.split(' ')

        surname = name_surname[1]
        letter = surname[0]

        if letter in 'ABCDEFGHI':
            lst_a_i += [1]
        elif letter in 'JKLMNOP':
            lst_j_p += [1]
        elif letter in 'QRST':
            lst_q_t += [1]
        elif letter in 'UVXYZ':
            lst_u_z += [1]

    result = lst_a_i.count(1), lst_j_p.count(1), lst_q_t.count(1), lst_u_z.count(1)

    # Если убрать этот блок, то функция не будет ничего печатать
    result2 = print("""
                       Group A-I - %d students.
                       Group J-P - %d students. 
                       Group Q-T - %d students. 
                       Group U-Z - %d students.""" % \
                       (int(lst_a_i.count(1)), int(lst_j_p.count(1)), int(lst_q_t.count(1)), int(lst_u_z.count(1))))
    return result


lst = ['Will Smith', 'Bred Pitt', 'Jonny Depp', 'Silvestr Stalone', 'Joly Joly', 'Artur Azarenkow', 'DeMar Derozen', 'Kyrire Yrving']
print(group_by_surname(lst))


           

