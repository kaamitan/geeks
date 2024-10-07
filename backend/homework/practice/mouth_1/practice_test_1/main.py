weeks = [
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье",
]

summing = []
for day in weeks:
    result = float(input(f"сколько вы потратили за {day}???: "))
    summing.append(result)
totalSum = round(sum(summing), 1)
average = round(totalSum / 7 ,1)
print(f"общая сумма потраченных денег за неделю : {totalSum} cомов")
print(f"также средняя сумма потраченных денег {average} сомов")