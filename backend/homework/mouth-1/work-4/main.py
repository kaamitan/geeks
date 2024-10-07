mentors = ["Тимур", "Арсен", "Гулина", "Даниель"]

while True:
    print("\nВыберете действие:")
    print("1. Добавить ментора")
    print("2. Изменить имя ментора")
    print("3. Удалить ментора")
    print("4. Выйти")

    choice = input("Введите номер действия: ")
    
    while len(choice) > 0 and (choice[0] == ' ' or choice[-1] == ' '):
        if choice[0] == ' ':
            choice = choice[1:]
        if choice[-1] == ' ':
            choice = choice[:-1]

    if choice == '1':  
        if len(mentors) >= 10:
            print("Список менторов полон.")
        else:
            name = input("Введите имя ментора для добавления: ")

            while len(name) > 0 and (name[0] == ' ' or name[-1] == ' '):
                if name[0] == ' ':
                    name = name[1:]
                if name[-1] == ' ':
                    name = name[:-1]

            if len(name) > 0:
                name = name[0].upper() + ''.join([ch.lower() for ch in name[1:]])

            if len(name) > 15:
                print("Имя не должно быть длиннее 15 символов.")
            elif name in mentors:
                print("Такой ментор уже есть.")
            else:
                mentors.append(name)
                print(f"Ментор {name} добавлен.")

    elif choice == '2':  
        old_name = input("Введите текущее имя ментора: ")

        while len(old_name) > 0 and (old_name[0] == ' ' or old_name[-1] == ' '):
            if old_name[0] == ' ':
                old_name = old_name[1:]
            if old_name[-1] == ' ':
                old_name = old_name[:-1]

        if len(old_name) > 0:
            old_name = old_name[0].upper() + ''.join([ch.lower() for ch in old_name[1:]])

        if old_name not in mentors:
            print("Ментор с таким именем не найден.")
        else:
            new_name = input("Введите новое имя ментора: ")

            while len(new_name) > 0 and (new_name[0] == ' ' or new_name[-1] == ' '):
                if new_name[0] == ' ':
                    new_name = new_name[1:]
                if new_name[-1] == ' ':
                    new_name = new_name[:-1]

            if len(new_name) > 0:
                new_name = new_name[0].upper() + ''.join([ch.lower() for ch in new_name[1:]])

            if len(new_name) > 15:
                print("Имя не должно быть длиннее 15 символов.")
            elif new_name in mentors:
                print("Такой ментор уже существует.")
            else:
                index = 0
                for i in range(len(mentors)):
                    if mentors[i] == old_name:
                        index = i
                        break
                mentors[index] = new_name
                print(f"Имя ментора изменено с {old_name} на {new_name}.")

    elif choice == '3':  
        print("\nВыберете метод удаления:")
        print("1. По индексу")
        print("2. По имени")

        delete_choice = input("Введите номер метода: ")

        while len(delete_choice) > 0 and (delete_choice[0] == ' ' or delete_choice[-1] == ' '):
            if delete_choice[0] == ' ':
                delete_choice = delete_choice[1:]
            if delete_choice[-1] == ' ':
                delete_choice = delete_choice[:-1]

        if delete_choice == '1':  
            index = input("Введите индекс ментора для удаления: ")

            while len(index) > 0 and (index[0] == ' ' or index[-1] == ' '):
                if index[0] == ' ':
                    index = index[1:]
                if index[-1] == ' ':
                    index = index[:-1]

            if index.isdigit():
                index = int(index)
                if 0 <= index < len(mentors):
                    removed = mentors.pop(index)
                    print(f"Ментор {removed} удален.")
                else:
                    print("Неверный индекс.")
            else:
                print("Введите корректное число.")

        elif delete_choice == '2':  
            name = input("Введите имя ментора для удаления: ")
            while len(name) > 0 and (name[0] == ' ' or name[-1] == ' '):
                if name[0] == ' ':
                    name = name[1:]
                if name[-1] == ' ':
                    name = name[:-1]

            if len(name) > 0:
                name = name[0].upper() + ''.join([ch.lower() for ch in name[1:]])

            if name in mentors:
                mentors.remove(name)
                print(f"Ментор {name} удален.")
            else:
                print("Ментор с таким именем не найден.")

        else:
            print("Некорректный выбор метода удаления.")

    elif choice == '4':  
        break

    else:
        print("Неверный выбор. Попробуйте снова.")

mentors_tuple = ()
for mentor in mentors:
    mentors_tuple += (mentor,)
print("\nОкончательный список менторов:", mentors_tuple)

