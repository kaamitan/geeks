import os
from time import sleep


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.read = False

    def mark_as_read(self):
        self.read = True

    def mark_as_unread(self):
        self.read = False

    def __str__(self):
        status = "Прочитана" if self.read else "Непрочитана"
        return f"'{self.title}' автор: {self.author}, год: {self.year} - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("Библиотека пуста.")
            return
        for book in self.books:
            print(book)

    def find_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def find_by_author(self, author):
        return [book for book in self.books if author.lower() in book.author.lower()]

    def mark_book_as_read(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.mark_as_read()
                print(f"Книга '{title}' отмечена как прочитанная.")
                return
        print(f"Книга '{title}' не найдена.")

    def mark_book_as_unread(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.mark_as_unread()
                print(f"Книга '{title}' отмечена как непрочитанная.")
                return
        print(f"Книга '{title}' не найдена.")

    def delete_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Книга '{title}' удалена из библиотеки.")
                return
        print(f"Книга '{title}' не найдена.")

    def filter_books_by_status(self, read_status):
        return [book for book in self.books if book.read == read_status]

    def sort_books_by_year(self):
        return sorted(self.books, key=lambda book: book.year)


def main():
    library = Library()

    while True:
        clear_screen()
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Просмотреть книги")
        print("3. Найти книгу по названию")
        print("4. Найти книгу по автору")
        print("5. Отметить книгу как прочитанную")
        print("6. Отметить книгу как непрочитанную")
        print("7. Удалить книгу")
        print("8. Фильтровать книги по статусу")
        print("9. Сортировать книги по году публикации")
        print("10. Выход")

        choice = input("Выберите действие: ")

        try:
            if choice == "1":
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                year = input("Введите год публикации: ")
                book = Book(title, author, year)
                library.add_book(book)
                print(f"Книга '{title}' добавлена.")

            elif choice == "2":
                library.list_books()

            elif choice == "3":
                title = input("Введите название книги для поиска: ")
                books = library.find_by_title(title)
                if books:
                    print("Найденные книги:")
                    for book in books:
                        print(book)
                else:
                    print("Книги не найдены.")

            elif choice == "4":
                author = input("Введите автора для поиска: ")
                books = library.find_by_author(author)
                if books:
                    print("Найденные книги:")
                    for book in books:
                        print(book)
                else:
                    print("Книги не найдены.")


            elif choice == "5":
                title = input(
                    "Введите название книги, которую хотите отметить как прочитанную: "
                )
                library.mark_book_as_read(title)

            elif choice == "6":
                title = input(
                    "Введите название книги, которую хотите отметить как непрочитанную: "
                )
                library.mark_book_as_unread(title)

            elif choice == "7":
                title = input("Введите название книги, которую хотите удалить: ")
                library.delete_book(title)

            elif choice == "8":
                status = input("Введите статус (прочитанные/непрочитанные): ")
                if status.lower() == "прочитанные":
                    books = library.filter_books_by_status(True)
                elif status.lower() == "непрочитанные":
                    books = library.filter_books_by_status(False)
                else:
                    print("Некорректный статус.")
                    continue

                if books:
                    print("Книги с заданным статусом:")
                    for book in books:
                        print(book)
                else:
                    print("Книги с заданным статусом не найдены.")

            elif choice == "9":
                sorted_books = library.sort_books_by_year()
                print("Книги, отсортированные по году публикации:")
                for book in sorted_books:
                    print(book)

            elif choice == "10":
                print("Выход из программы.")
                break

            else:
                print("Некорректный выбор. Попробуйте еще раз.")

            sleep(2)

        except KeyboardInterrupt:
            clear_screen()
            break


main()