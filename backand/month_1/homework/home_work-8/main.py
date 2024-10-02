def guess_number():
    low, high = 1, 100 
    attempts = 0  
    guesses = []  

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Загадайте число от 1 до 100.")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    while True:
        guess = (low + high) // 2
        attempts += 1
        guesses.append(guess)
        print(f"я думаю, что это число {guess}.")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        answer = input("[да/yes] [больше/more] [меньше/less] : ").strip().lower()

        if answer in ['да', 'yes']:
            print('===========================')
            print(f"Ура! Программа угадала число {guess} за {attempts} попыток.")
            print('===========================')
            with open("results.txt", "a", encoding="UTF-8") as file:
                file.write(f"Загаданное число: {guess}\n")
                file.write(f"Количество попыток: {attempts}\n")
                file.write(f"Список всех попыток: {guesses}\n\n")
            
            break 
        elif answer in ['больше', 'more']:
            low = guess + 1 
        elif answer in ['меньше', 'less']:
            high = guess - 1 
        else:
            print("Пожалуйста, введите 'да/yes', 'больше/more', или 'меньше/less'.")
            attempts -= 1 
            guesses.pop()

guess_number()
