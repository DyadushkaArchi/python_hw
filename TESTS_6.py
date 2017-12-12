# Определить является ли строка изограммой,
# т.е. что все буквы в ней за исключением пробелов встречаются только один раз.
# Например, строки 'Питон', 'downstream', 'книга без слов' являются изограммами,
# а само слово 'изограмма' - нет.


def is_isogramm(text):
    lst = {}
    for i in range(len(str(text))):
        key = str(text)[i]
        if not str(key) in lst:
            lst[str(key)] = 1
        elif str(key) in lst:
            return False

    return True

print(is_isogramm('paradox'))



