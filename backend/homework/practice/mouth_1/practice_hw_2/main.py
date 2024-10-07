rounds = 10

jan = 1 
feb = 2
mar = 3
apr = 4
may = 5
jun = 6 
jul = 7
aug = 8 
sep = 9
octo = 10
nov = 11
dec = 12 


while rounds > 0 : 

    exits = "exit stop quit выход выйти стоп"

    day = input('Введите день рождение :')
    if day in exits :
        break

    month = input('Введите месяц рождение:')
    if month in exits : 
        break

    year = input('Введите год рождение :')
    if year in exits : 
        break


    if not day.isdigit() and month.isdigit() and year.isdigit():
        print('вы ошиблись ввидите заного.') 
        rounds -= 1
        continue

    day = int(day)
    month =int(month)
    year = int(year)
    rounds -= 1
    if day > 31 :
        print('Вы ввели неправильно! Повторяйте снова!!!')
    elif month > 12 :
        print('Вы ввели неправильно! Повторяйте снова!!!')
    elif year <= 1900 and year > 2024 : 
        print('Вы ввели неправильно! Повторяйте снова!!!')

