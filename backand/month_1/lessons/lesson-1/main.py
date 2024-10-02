monday = float(input('Введите расход за первый день:'))
tuesday = float(input('Введите расход за второй день:'))
wednesday = float(input('Введите расход за третий день:'))
thursday = float(input('Введите расход за четвертый день:'))
friday = float(input('Введите расход за пятый день:'))
saturday = float(input('Введите расход за шестой день:'))
sunday = float(input('Введите расход за седьмой день:'))


total_expanse = monday + tuesday + wednesday + thursday + friday + saturday + sunday
days_in_week = 7

average_daily_expanse = total_expanse / days_in_week
average_daily_expanse = round(average_daily_expanse, 1)

print(f'Общая сумма расходов за неделю: {total_expanse} ')
print(f'Средний расход в день: {average_daily_expanse}')
