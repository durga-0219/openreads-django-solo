import csv
from django.core.management.base import BaseCommand
from books.models import Book, Author

class Command(BaseCommand):
    help = 'Load books from CSV into the database'

    def handle(self, *args, **kwargs):
        with open('books/openreads_books_5000.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            count = 0
            for row in reader:
                author_name = row['Book-Author'].strip()
                title = row['Book-Title'].strip()
                year = int(row['Year-Of-Publication']) if row['Year-Of-Publication'].isdigit() else 2000
                publisher = row['Publisher'].strip()
                image_url = row['Image-URL-L'].strip()

                author, created = Author.objects.get_or_create(name=author_name)
                Book.objects.get_or_create(
                    title=title,
                    author=author,
                    year=year,
                    publisher=publisher,
                    image_url=image_url
                )
                count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {count} books into the database!'))
