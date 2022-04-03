from django.test import TestCase
from django.db.models import SET_NULL as null
from catalog.models import AuthorModel as Author
from catalog.models import BookModel as Book
from catalog.models import GenreModel as Genre


class YourTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name="Alexey", last_name="Petrov")
        Genre.objects.create(name="Fantasy")
        Book.objects.create(title="2000", author=Author.objects.get(id=1), summary="2000", isbn=64383,
                            genre=Genre.objects.get(id=1))
        print("Author was created")
        print("Genre was created")
        print("Book was created")

    def setUp(self):
        print("setUp: Running")
        pass

    def tearDown(self):
        print("tearDown: Running")
        pass

    def test_max_length_first_name(self):
        author = Author.objects.get(id=1)
        field_length = author._meta.get_field('first_name').max_length
        return self.assertEquals(field_length, 100)

    def test_field_label_first_name(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        return self.assertEquals(field_label, 'first name')

    def test_length_last_name(self):
        author = Author.objects.get(id=1)
        field_length = author._meta.get_field('last_name').max_length
        return self.assertEquals(field_length, 100)

    def test_length_last_name_120(self):
        author = Author.objects.get(id=1)
        field_length = author._meta.get_field('last_name').max_length
        return self.assertEquals(field_length, 120)

    def test_verbose_name_first_name(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        return self.assertEquals(field_label, 'first name')

    def test_verbose_name_last_name(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        return self.assertEquals(field_label, 'last name')

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        return self.assertEquals(author.get_absolute_url(), '1')

    def test_title_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        return self.assertEquals(max_length, 200)

    def test_title_length(self):
        book = Book.objects.get(id=1)
        author = book._meta.get_field('author').on_delete
        return self.assertEquals(author, null)

    def test_summury_help_text(self):
        book = Book.objects.get(id=1)
        summary = book._meta.get_field('summary').help_text
        return self.assertEquals(summary, 'Краткое содержание книги')

    def test_verbose_name_isbn(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('isbn').verbose_name
        return self.assertEquals(field_label, 'ISBN')

    def test_verbose_name_genre(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('genre').verbose_name
        return self.assertEquals(field_label, 'GenreModel')


