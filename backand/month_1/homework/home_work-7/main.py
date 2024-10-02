"""Функция ближайшего числа"""
def closest_number(numbers, target):
    sorted_numbers = sorted(numbers, key=lambda x: abs(x - target))
    return target, sorted_numbers

"""Пример использования"""
numbers_list = [5, 2, 9, 15, 3]
target_number = 8
result = closest_number(numbers_list, target_number)
print("Задача 1:", result)


"""Пример использования lambda с filter и map"""
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
doubled_numbers = list(map(lambda x: x * 2, numbers))
print("Задача 2: Четные числа:", even_numbers)
print("Задача 2: Удвоенные числа:", doubled_numbers)

def get_element(iterable):
    while True:
        try:
            index = int(input("Введите индекс элемента (или -1 для выхода): "))
            if index == -1:
                print("Выход из программы.")
                break
            print(f"Элемент на индексе {index}: {iterable[index]}")
        except IndexError:
            print(f"Некорректный индекс! Введите индекс от 0 до {len(iterable) - 1}.")
        except ValueError:
            print("Пожалуйста, введите целое число.")

numbers = [10, 20, 30, 40, 50]
get_element(numbers)
