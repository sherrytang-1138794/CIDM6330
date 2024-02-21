from django.test import TestCase

from catalog.models import Author, Book, BookInstance, Genre


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        # Get an author object to test
        author = Author.objects.get(id=1)
        # Get the metadata for the required field and use it to query the required field data
        field_label = author._meta.get_field('first_name').verbose_name
        # Compare the value to the expected result
        self.assertEqual(field_label, 'first name')

    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')    
    
    def test_date_of_birth_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEqual(field_label, 'date of birth')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEqual(field_label, 'died')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_lasst_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEqual(str(author), expected_object_name)

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(author.get_absolute_url(), '/catalog/author/1')


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Book.objects.create(title='BookName', summary='BookSummary', isbn='ABCDE')

    def test_book_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_book_author_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_book_summary_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('summary').verbose_name
        self.assertEqual(field_label, 'summary')

    def test_book_isbn_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('isbn').verbose_name
        self.assertEqual(field_label, 'ISBN')

    def test_book_genre_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('genre').verbose_name
        self.assertEqual(field_label, 'genre')

    def test_book_title_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_book_summary_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('summary').max_length
        self.assertEqual(max_length, 1000)

    def test_book_isbn_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('isbn').max_length
        self.assertEqual(max_length, 13)    

    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(book.get_absolute_url(), '/catalog/book/1')


class GenreModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Genre.objects.create(name='Genre')

    def test_genre_label(self):
        genre = Genre.objects.get(id=1)
        field_label = genre._meta.get_field('name').verbose_name
        self.assertEqual(field_label, "name")

    def test_genre_max_length(self):
        genre = Genre.objects.get(id=1)
        max_length = genre._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)  

    def test_get_absolute_url(self):
        genre = Genre.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(genre.get_absolute_url(), '/catalog/genre/1')    


class BookInstanceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        BookInstance.objects.create(id='a5b29fe6-d2f6-464b-a1af-fcf07aeb3c05',
                                    imprint='Unlikely Imprint, 2016')

    def test_bookinstance_id_label(self):
        bookinstance = BookInstance.objects.get(id='a5b29fe6-d2f6-464b-a1af-fcf07aeb3c05',)
        field_label = bookinstance._meta.get_field('id').verbose_name
        self.assertEqual(field_label, "id")

    def test_bookinstance_imprint_label(self):
        bookinstance = BookInstance.objects.get(id='a5b29fe6-d2f6-464b-a1af-fcf07aeb3c05',)
        field_label = bookinstance._meta.get_field('imprint').verbose_name
        self.assertEqual(field_label, "imprint")

    def test_bookinstance_status_label(self):
        bookinstance = BookInstance.objects.get(id='a5b29fe6-d2f6-464b-a1af-fcf07aeb3c05',)
        field_label = bookinstance._meta.get_field('status').verbose_name
        self.assertEqual(field_label, "status")

    def test_imprint_max_length(self):
        bookinstance = BookInstance.objects.get(id='a5b29fe6-d2f6-464b-a1af-fcf07aeb3c05',)
        max_length = bookinstance._meta.get_field('imprint').max_length
        self.assertEqual(max_length, 200)  

    def test_status_max_length(self):
        bookinstance = BookInstance.objects.get(id='a5b29fe6-d2f6-464b-a1af-fcf07aeb3c05',)
        max_length = bookinstance._meta.get_field('status').max_length
        self.assertEqual(max_length, 1)  

    def test_get_absolute_url(self):
        bookinstance = BookInstance.objects.get(id='a5b29fe6-d2f6-464b-a1af-fcf07aeb3c05',)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(bookinstance.get_absolute_url(), '/catalog/bookinstance/a5b29fe6-d2f6-464b-a1af-fcf07aeb3c05')  
    
        
# class YourTestClass(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         print("setUpTestData: Run once to set up non-modified data for all class methods.")
#         pass

#     def setUp(self):
#         print("setUp: Run once for every test method to set up clean data.")
#         pass

#     def test_false_is_false(self):
#         print("Method: test_false_is_false.")
#         self.assertFalse(False)

#     def test_false_is_true(self):
#         print("Method: test_false_is_true.")
#         self.assertTrue(False)

#     def test_one_plus_one_equals_two(self):
#         print("Method: test_one_plus_one_equals_two.")
#         self.assertEqual(1 + 1, 2)


