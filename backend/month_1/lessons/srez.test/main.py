def kalc(inp1: float, opr: str, inp2: float) -> float:
    """
    Калькулятор для выполнения арифметических операций.

    Параметры:
    inp1: Первое число.
    opr: Арифметический оператор ('+', '-', '*', '/', '//', '%').
    inp2: Второе число.

    Возвращает:
    float: Результат операции.
    """
    try:
        if opr == "+":
            return inp1 + inp2
        elif opr == "-":
            return inp1 - inp2
        elif opr == "*":
            return inp1 * inp2
        elif opr == "/":
            return inp1 / inp2
        elif opr == "//":
            return inp1 // inp2
        elif opr == "%":
            return inp1 % inp2
        else:
            raise ValueError("Недопустимый оператор.")
    
    except ZeroDivisionError:
        return "Ошибка: Деление на ноль!"

# Примеры использования
print(kalc(1, "+", 1))   # Вывод: 2
print(kalc(10, "/", 2))  # Вывод: 5.0
print(kalc(10, "//", 3)) # Вывод: 3
print(kalc(10, "%", 3))  # Вывод: 1
print(kalc(10, "/", 0))  # Вывод: Ошибка: Деление на ноль!




# """6"""
# kgz_regions = [
#     "Чуй", "Ыссык-Кол", "Нарын", "Талас",
#     "Джалал-Абад", "Ош", "Баткен"
# ]

# first_three = tuple(kgz_regions[:3])
# print(first_three)

# """5"""
# geekteach = {
#     'name': 'Geecteach',
#     'address': 'Токтогулова 175',
#     'courses': {'Backand', 'Androud'}
# }

# geeks = dict(name='GEEKS', address='Ибраимова 103')
# geekteach.update(geeks)
# geeks = geekteach.copy()
# geeks['courses'].update(['Frontend', 'IOS'])
# print(geeks)





# """4"""

# geeks_in = ['Бишкек', 'Ош', 'Кара-Балта', 'Бишкек 9мкр']

# # geeks_in.short()
# # geeks_in = [i.upper() for i in geeks_in]

# geeks_in = geeks_in[::-1]
# print(geeks_in)






# """3"""

# for i in range(1, 10+1):
#     if i > 7 :
#         print(i)
#     else:
#         print(False)





# """2"""
# counter = 5

# while counter != 0:
#     print('GEEKS.Pyton, first month, final test!')
#     counter -= 1



# """1"""
# geeks_founding_year = 2018
# current_year = int(input('enter current year: '))


# if(current_year - geeks_founding_year) > 5:
#     print('Образавтательному центру больше 5 лет ')
# else:
#     pass
# elif(current_year - geeks_founding_year) in range(1,5 + 5):
#     print('Образавательному центру меньше 5 лет ')


