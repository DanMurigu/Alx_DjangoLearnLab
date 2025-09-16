CREATE
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# book

# Output: <Book: 1984 by George Orwell>

RETRIEVE
book = Book.objects.get(title="1984")
# output
book.title  # '1984'
book.author  # 'George Orwell'
book.publication_year  # 1949

UPDATE
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
# output
book.title  # 'Nineteen Eighty-Four'

DELETE
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Output: 
(1, {'bookshelf.Book': 1})

Book.objects.all()
# Output: <QuerySet []>
