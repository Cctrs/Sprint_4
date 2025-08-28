from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_two_books_added_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2
    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    

    # Тест, проверяющий, что добавление книги с названием в 41 символ невозможно
    def test_add_new_book_book_with_long_name_book_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Как делегировать все свои рабочие задачи?')

        assert collector.get_books_genre() == {}


    # Тест, проверяющий, что жанр книги можно добавить, если жанр есть в списке жанров
    @pytest.mark.parametrize('name,genre', [['Автотесты за 30 минут - реальность!', 'Фантастика'], 
                                             ['Пятничный крит','Ужасы'],
                                             ['Кто убил прод?','Детективы'],
                                             ['Тестирование для малышей','Мультфильмы'],
                                             ['Бизнес-требования заказчика','Комедии']])
    def test_set_book_genre_add_exist_genre_adds_genre_to_book(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.books_genre[name] in collector.genre


    # Тест, проверяющий, что если у книги не указан жанр, то он не будет выведен
    def test_get_book_genre_no_book_genre_returns_empty_string(self):
        collector = BooksCollector()
        collector.add_new_book('Жанр 404')

        assert collector.get_book_genre('Жанр 404') == ''


    # Тест, проверяющий, что можно вывести книги с определенным жанром
    def test_get_books_with_specific_genre_filter_exist_genre_returns_books_with_specific_genre(self):
        collector = BooksCollector()
        books_names = ['Автотесты за 30 минут - реальность!', 'Пятничный крит',
                        'Кто убил прод?', 'Тестирование для малышей', 'Бизнес-требования заказчика']

        for name in books_names:
            collector.add_new_book(name)
            collector.set_book_genre(name, 'Комедии')
        
        collector.set_book_genre('Пятничный крит', 'Ужасы')

        assert len(collector.get_books_with_specific_genre('Комедии')) == 4


    # Тест, проверяющий, что если в словарь с книгами не добавлены книги, то он выводится пустым
    def test_get_books_genre_zero_books_returns_empty_dict(self):
        collector = BooksCollector()

        assert collector.get_books_genre() == {}


    # Тест, проверяющий, что для детей не выводятся книги из жанров для взрослых
    @pytest.mark.parametrize('name,genre', [['Пятничный крит','Ужасы'],
                                            ['Кто убил прод?','Детективы']])
    def test_get_books_for_children_adult_book_not_shows(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert name not in collector.get_books_for_children()


    # Тест, проверяющий, что нельзя добавить в избранное книгу, которой нет в списке
    def test_add_book_in_favorites_book_not_in_books_genre_returns_empty_favorites_list(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Меня не добавить в избранное')

        assert collector.get_list_of_favorites_books() == []


    # Тест, проверяющий, что можно удалить книгу из избранного если она там есть
    def test_delete_book_from_favorites_remove_exist_book_removes_book(self):
        collector = BooksCollector()
        collector.add_new_book('Удалите это немедленно')
        collector.add_book_in_favorites('Удалите это немедленно')
        collector.delete_book_from_favorites('Удалите это немедленно')

        assert collector.get_list_of_favorites_books() == []


    # Тест, проверяющий, что можно получить список избранных книг
    def test_get_list_of_favorites_books_books_added_in_favorites_shows_books(self):
        collector = BooksCollector()
        books = ['Пайтон для начинающих', 'Пайтон для вспоминающих', 'Пайтон для забывающих']
        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)

        assert collector.get_list_of_favorites_books() == books


    # Тест, проверяющий, что если в списке избранного нет книг, то получаем пустой список
    def test_get_list_of_favorites_books_zero_books_returns_empty_list(self):
        collector = BooksCollector()

        assert collector.get_list_of_favorites_books() == []