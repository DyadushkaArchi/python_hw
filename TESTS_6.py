# Определить является ли строка изограммой,
# т.е. что все буквы в ней за исключением пробелов встречаются только один раз.
# Например, строки 'Питон', 'downstream', 'книга без слов' являются изограммами,
# а само слово 'изограмма' - нет.


def is_isogramm(text):
    text = str(text)
    letter_frequency = {}
    for i in range(len(text)):
        key = str(text[i])
        if not key in letter_frequency:
            letter_frequency[key] = 1
        elif key in letter_frequency:
            return False

    return True

print(is_isogramm('pardox'))



