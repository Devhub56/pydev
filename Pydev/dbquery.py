#!/usr/bin/env python
import sqlite3
conn = sqlite3.connect('employees.db')
curs = conn.cursor()
query = 'SELECT * FROM employee_data WHERE ' + sys.argv[1]
print(query)
curs.execute(query)
names = [f[0] for f in curs.description]
for row in curs.fetchall():
    for pair in zip(names, row):
        print('{}: {}'.format(*pair))
    print()
