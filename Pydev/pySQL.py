#!/usr/bin/env python
import sqlite3

entries=["Enter id :","Enter  First name :","Enter last name :","Enter age :","Enter Address :","Enter city :","Enter state :"]
i=0

while i<7:
        k=input([i])
        i+=1
        break

def data_entry(self,insert):
    INSERT INTO employee_data
      (id,first, last, age, address, city, state)
      values(k)

conn = sqlite3.connect('employees.db')
curs = conn.cursor()
curs.execute('''
CREATE TABLE employee_data (
id TEXT PRIMARY KEY,
first     TEXT,
lasst     TEXT,
age       TEXT,
address   TEXT,
city      TEXT,
state     TEXT,
)
''')
query = 'INSERT INTO employees values (?,?,?,?,?,?,?,?,?,?)'

conn.commit()
conn.close()
