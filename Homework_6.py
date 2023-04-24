import sqlite3

def print_students():
    '''Функция для вывода результата после исполнения SQL-команд'''
    selected_students_list = curs.fetchall()
    for student in selected_students_list:
        print(student)
    print('\n  -//-  \n')

conn = sqlite3.connect("stds.db")
curs = conn.cursor()
stud_list = [('Сергей', 'Ившин', 'теннис', 1979, 10),
             ('Алексей', 'Савко', 'футбол', 1976, 8),
             ('Светлана', 'Самородова', 'йога', 1986, 6),
             ('Валентин', 'Джунковский', 'путешествия', 1982, 12),
             ('Николай', 'Благонадеждин', 'рыбалка', 1989, 10),
             ('Анна', 'Сметанкина', 'шоппинг', 1991, 12),
             ('Наталья', 'Гарафутдинова', 'йога', 1976, 8),
             ('Александр', 'Паклин', 'фитнес', 1986, 9),
             ('Игорь', 'Тышлин', 'футбол', 1983, 10),
             ('Алексей', 'Полукханов', 'фитнес', 1973, 14),
             ]

ins = "INSERT INTO students VALUES (?, ?, ?, ?, ?)"
curs.execute('''CREATE TABLE IF NOT EXISTS
students (name TEXT,
surname TEXT,
hobby TEXT,
year_of_birth INTEGER,
test_points INTEGER)''')
curs.executemany(ins, stud_list)

curs.execute("SELECT rowid, * FROM students WHERE LENGTH(surname) > 10")
print_students()
curs.execute("UPDATE students SET name='genius' WHERE test_points > 10")
curs.execute("SELECT rowid, * FROM students WHERE name='genius'")
print_students()
curs.execute("DELETE FROM students WHERE rowid % 2 == 0")
curs.execute("SELECT rowid, * FROM students")
print_students()

curs.close()
conn.close()










