from django.test import TestCase
from rest_api.models import Author, Book
from django.utils import timezone

# Create your tests here.
class AuthorTestCase(TestCase):

    def test_author_create(self):
        name = "Steven Taylor"
        date_of_birth = timezone.now()
        Author.objects.create(name=name, date_of_birth=date_of_birth)
        authors = Author.objects.all()

        self.assertEqual(len(authors), 1)
        self.assertEqual(name, authors[0].name)
        self.assertEqual(date_of_birth, authors[0].date_of_birth)

class BookTestCase(TestCase):

    def test_book_create(self):
        publish_date = timezone.now()
        name = "Random Book"
        author_name = "Steven Taylor"
        author_date_of_birth = timezone.now()
        author = Author.objects.create(name=author_name, 
                                       date_of_birth=author_date_of_birth)
        Book.objects.create(name=name, 
                            publish_data=publish_date,
                            author=author)
        books = Book.objects.all()
        db_author = Author.objects.get(name=author_name) 

        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].name, name)
        self.assertEqual(books[0].publish_data, publish_date)
        self.assertEqual(db_author, books[0].author)