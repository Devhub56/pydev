#common cmds: select "title" or ["item 1","item 2"] from tablename
create table employee #unique
(first varchar(15),
 last varchar(20),
 age number(3),
 address varchar(30),
 city varchar(20),
 dept varchar(20),
 state varchar(20),
 date);
#insert data in tablename
#all strings shoul be enclosed in single''
insert into employee
  (first, last, age, address, city, state)
  values ('Mary', 'Williams', 45, '2130 Boars Nest',
          'Hazard Co', 'Georgia');
#updating db
update employee
  set age = age+1
  where first='Mary' and last='Williams';

#deleting a record , the where clause is so important as without it, the whole db is deleted
delete from employee
  where lastname = 'May';
 #delete entire tablename
 #e.g drop table employee;
SELECT name, age, salary #can add distinct to return only the unique parameters in the query
SELECT name, title, dept FROM employee WHERE title LIKE 'Pro%';

FROM employee

WHERE age > 40;
