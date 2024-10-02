#контекстный менеджер "with", работа с файлами
# w - write (запись, презапись)
# a - add (дозапись)
# x - создает уникальный файл

# file = open('new_file.txt', "w", encoding="UTF-8")
# file.write('текст на кириллице')
# file.close()

# with open('new_file.txt', 'a', encoding="UTF-8") as new_file:
#     new_file.write('\nвтороя строка')

with open('other.txt', 'x', encoding="UTF-8") as file:
    file.write('новый файл')
    