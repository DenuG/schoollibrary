import sqlite3
c = sqlite3.connect('library.db')
#c.execute('ALTER TABLE books ADD idr INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL')
#c.execute('UPDATE books SET image = "171.jpg" WHERE title = "Живая Шляпа"')
c.execute('UPDATE books SET image = "22.jpg" WHERE title = "Алиса в стране чудес"')
#c.execute('UPDATE books SET image = "emblema.png" WHERE title = "10М"')
#c.execute('UPDATE books SET title = "10Б" WHERE author = "Ильмир Ильдарович"')
#c.execute('UPDATE books SET author = "Алексей Aндреевич" WHERE year = "2023"')
#c.execute('UPDATE books SET count += 2 WHERE author = "Алексей Андреевич"')
#c.execute("ALTER TABLE books DROP COLUMN id")
# c.execute('ALTER TABLE books RENAME TO old_books;')
# c.execute('CREATE TABLE books (id INTEGER PRIMARY KEY AUTOINCREMENT, title VERCHAR(255), author VARCHAR(255), description TEXT, year VARCHAR(255), image VARCHAR(255), count INTEGER);')
# c.execute('INSERT INTO books SELECT * FROM old_books;')


c.commit()