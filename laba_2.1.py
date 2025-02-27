BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if isinstance(id_, int):
            self.id_ = id_
        else:
            raise TypeError("ID книги должен быть целым числом")

        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Название книги должно быть строкой")

        if isinstance(pages, int):
            self.pages = pages
        else:
            raise TypeError("Кол-во страниц книги должно быть целым числом")

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id_}, name='{self.name}', pages={self.pages})"


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
