import sqlite3
conn=sqlite3.connect("connect.db")
'''#conn.execute("create table student(id int primary key,Name varchar2(20),Age int);")
conn.execute("insert into student(id,name,Age) values(401,'Maya',20);")
conn.execute("insert into student(id,name,Age) values(402,'Arav',20);")
conn.execute("insert into student(id,name,Age) values(403,'Mitra',20);")
conn.execute("insert into student(id,name,Age) values(404,'Aman',20);")
conn.execute("insert into student(id,name,Age) values(405,'Celina',20);")
conn.execute('delete from student where id=402;')
conn.execute("alter table student add rollno int")
conn.execute("select name from student name where age==20 ")
conn.commit()
conn.close()'''

#conn.execute("create table emp(eid int primary key,eName varchar2(20),eaddress varchar2(20),salary int);")
conn.execute("insert into emp values(4010,'Maya','parl street',20000);")
'''conn.execute("insert into emp(eid,ename,eaddr) values(406,'Arav''parl street',20000);")
conn.execute("insert into emp(eid,ename,Age) values(407,'Mitra''parl street',20000);")
conn.execute("insert into emp(eid,ename,Age) values(408,'Aman''parl street',20000);")
conn.execute("insert into emp(eid,ename,Age) values(409,'Celina','parl street',20000);")'''
conn.commit()
conn.close()
