monday = float(input('Расход за понедельник:'))
tuesday = float(input('Расход за вторник:'))
wednesday = float(input('Расход за среду:'))
thursday = float(input('Расход за четверг:'))
friday = float(input('Расход за пятницу:'))
saturday = float(input('Расход за субботу:'))
sunday = float(input('Расход за воскресенье:'))

total_expens = monday + tuesday + wednesday + thursday + friday + saturday + sunday
weeks = 7
average_expens = total_expens / weeks

total_expens = round(total_expens,1)
average_expens = round(average_expens,1)

print("")
print(f'Расходы за неделю:{total_expens}\nСредний расход за неделю:{average_expens}')
print('')

if total_expens >= 1 and total_expens <= 150 :
    print('вы потратили мало')
elif total_expens >=151 and total_expens <= 500 : 
    print("вы потратили средне")
elif total_expens >= 501 : 
    print("вы потратили много")
else : 
    print('вы ничего не потратили')