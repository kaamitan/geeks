# # Количество дней в каждом месяце
# days_in_month = {
#     1: 31,  # Январь
#     2: 28,  # Февраль (пока не учитываем високосный год)
#     3: 31,  # Март
#     4: 30,  # Апрель
#     5: 31,  # Май
#     6: 30,  # Июнь
#     7: 31,  # Июль
#     8: 31,  # Август
#     9: 30,  # Сентябрь
#     10: 31,  # Октябрь
#     11: 30,  # Ноябрь
#     12: 31   # Декабрь
# }

# # Високосный год
# def is_leap_year(year):
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# # Ввод данных
# day = int(input('Введите день рождения: '))
# month = int(input('Введите месяц рождения: '))
# year = int(input('Введите год рождения: '))

# # Если год високосный, корректируем количество дней в феврале
# if is_leap_year(year):
#     days_in_month[2] = 29

# # Проверка на корректность дня, месяца и года
# if month not in days_in_month or day > days_in_month[month] or year < 1924 or year > 2024:
#     print("\nОшибка в вводе!\nПроверьте ещё раз!")
#     print(f"Правильный ввод: <день, месяц, год>: <(1-{days_in_month[month]}) (1-12) (1924-2024)>")
# else:
#     # Определение знака зодиака
#     if (month == 3 and day >= 21) or (month == 4 and day <= 20):
#         say = 'Овен'
#     elif (month == 4 and day >= 21) or (month == 5 and day <= 21):
#         say = 'Телец'
#     elif (month == 5 and day >= 22) or (month == 6 and day <= 21):
#         say = 'Близнецы'
#     elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
#         say = 'Рак'
#     elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
#         say = 'Лев'
#     elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
#         say = 'Дева'
#     elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
#         say = 'Весы'
#     elif (month == 10 and day >= 23) or (month == 11 and day <= 22):
#         say = 'Скорпион'
#     elif (month == 11 and day >= 23) or (month == 12 and day <= 21):
#         say = 'Стрелец'
#     elif (month == 12 and day >= 22) or (month == 1 and day <= 20):
#         say = 'Козерог'
#     elif (month == 1 and day >= 21) or (month == 2 and day <= 18):
#         say = 'Водолей'
#     elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
#         say = 'Рыбы'
#     else:
#         print('Неверный ввод дня или месяца!')
#         say = 'Неизвестен'

#     # Вывод результата
#     print(f"\nДень: {day}\nМесяц: {month}\nГод: {year}\nЗнак зодиака: {say}")
#     print("__________________")
#     print(f"{day}.{month}.{year}\n")






datetime = 'day , month , year' 

rounds = 10
while rounds > 0:
    # day = input(f'enter day: ({rounds}) ').lower()
    # month = input(f'enter month: ({rounds}) ').lower()
    # year = input(f'enter year: ({rounds}) ').lower()
    datetime = input(f'enter datetime: ({rounds}) ').lower()
    if datetime == 'exit':
        break


jan = 1
feb = 2 
mar = 3
apr = 4
may = 5
jun =  6
jul =  7
aug =  8
sep =  9
octo = 10
nov = 11 
dec = 12


day = int(input('Введите день дату рождения:'))
month = int(input('Введите месяц рождения:'))
year = int(input('Введите год рождения:'))


if (month > 12 or day > 31 or year <= 1924 or year > 2024):
   print("")
   print("Ошибка в вводе!\nПроверьте еще раз!")
   print("вы ошиблись в вводе!!!\nправильный ввод: <day,month,year>: <(1-31) (1-12) (1924-2024)>")
   print("")
else:
    if (month == mar and day >= 21) or (month == apr and day <= 20):
        say = 'Овен'
    elif (month == apr and day >= 21) or (month == may and day <= 21):
        say = 'Телец'
    elif (month == may and day >= 22) or (month == jun and day <= 21):
        say = 'Близнецы'
    elif (month == jun and day >= 22) or (month == jul and day <= 22):
         say = 'Рак'
    elif (month == jul and day >= 23) or (month == aug and day <= 21):
        say = 'Лев'
    elif (month == aug and day >= 22) or (month == sep and day <=23):
        say = 'Дева'
    elif (month == sep and day >= 24) or (month == octo and day <= 23):
        say = 'Весы'
    elif (month == octo and day >= 24) or (month == nov and day <= 22):
        say = 'Скорпион'
    elif (month == nov and day >= 23) or (month == dec and day <= 22):
        say = 'Стрелец'
    elif (month == dec and day >= 23) or (month == jan and day <= 20):
        say = 'Козерог'
    elif (month == jan and day >= 21) or (month == feb and day <= 19):
        say = 'Водолей'
    elif (month == feb and day >= 20) or (month == mar and day <= 20):
        say = 'Рыбы'
    else:
        print('неверный ввод день и месяцев!')
    
    print(" ")
    print(f'день:{day}\nмесяц:{month}\nгод:{year}\nзнак задиака: {say}')
    print("__________________")
    print(f"{day}.{month}.{year}")
    print(" ")
rounds -= 1
