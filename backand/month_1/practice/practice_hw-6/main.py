movies = {
    "Джанго Освобожденный": {
        "Джон": 10,
        "Джек": 9
    },
    "Троя": {}
}

def find_movie(movie_name):
    return movie_name in movies

def add_movie(movie_name):
    if find_movie(movie_name):
        print("Этот фильм уже существует!")
    else:
        movies[movie_name] = {}
        print("Фильм успешно добавлен!")

def add_rating(movie_name, user_name, rating):
    if not find_movie(movie_name):
        print("Такого фильма не существует.")
    else:
        if user_name in movies[movie_name]:
            print("Этот пользователь уже оценил фильм. Пожалуйста, используйте другое имя.")
        elif rating < 0 or rating > 10:
            print("Оценка должна быть от 0 до 10.")
        else:
            movies[movie_name][user_name] = rating
            print(f"Оценка добавлена для фильма {movie_name}: {user_name} оценил его на {rating}")

def view_ratings():
    for movie, ratings in movies.items():
        if ratings:
            avg_rating = sum(ratings.values()) / len(ratings)
            print(f"{movie} имеет средний рейтинг {round(avg_rating, 1)}")
        else:
            print(f"Рейтинга для {movie} пока нет.")

while True:
    print("\nВыберите команду:")
    print("1. Добавить фильм")
    print("2. Добавить рейтинг")
    print("3. Показать рейтинги")
    print("4. Выход")

    choice = input("Введите номер команды: ").strip()

    if choice == "1":
        movie_name = input("Введите название фильма: ").strip().title()
        add_movie(movie_name)

    elif choice == "2":
        movie_name = input("Введите название фильма: ").strip().title()
        user_name = input("Введите ваше имя: ").strip()
        rating = float(input("Введите вашу оценку (0-10): "))
        add_rating(movie_name, user_name, rating)

    elif choice == "3":
        view_ratings()

    elif choice == "4":
        print("Программа завершена.")
        break

    else:
        print("Неверная команда. Пожалуйста, попробуйте снова.")
