import mysql.connector as c;
con=c.connect(host="localhost",user="root",password="",database="testdatabase")
if con.is_connected():
    print("done")
mycur=con.cursor()
#create tables
t1="CREATE TABLE sailors (sid INT(3) PRIMARY KEY, sname VARCHAR(25), rating INT(10), dob DATE);"
mycur.execute(t1)
t2="CREATE TABLE boats (bid INT(3) PRIMARY KEY, bname VARCHAR(25), color VARCHAR(25));"
mycur.execute(t2)
t2="CREATE TABLE reserves (sid INT(3),bid INT(3), date DATE,time_slot VARCHAR(25));"
mycur.execute(t2)
a1="ALTER TABLE reserves ADD PRIMARY KEY(sid, bid, date, time_slot);"
mycur.execute(a1)
a2="ALTER TABLE reserves ADD FOREIGN KEY(sid) REFERENCES sailors(sid);"
mycur.execute(a2)
a3="ALTER TABLE reserves ADD FOREIGN KEY(bid) REFERENCES boats(bid);"
mycur.execute(a3)
#sailors
s1="INSERT INTO sailors VALUES (101, 'ram', 9, '1991-06-09')"
mycur.execute(s1)
con.commit()
s2="INSERT INTO sailors VALUES (102,'govind',9,'1976-12-09')"
mycur.execute(s2)
con.commit()
s3="INSERT INTO sailors VALUES (103, 'mohan', 8, '1984-06-27')"
mycur.execute(s3)
con.commit()
s4="INSERT INTO sailors VALUES (104, 'sam', 7, '1995-01-09')"
mycur.execute(s4)
con.commit()
s5="INSERT INTO sailors VALUES (105, 'om', 10, '1984-07-15')"
mycur.execute(s5)
con.commit()
s6="INSERT INTO sailors VALUES (106, 'darrel', 6, '1991-06-09')"
mycur.execute(s6)
con.commit()
s7="INSERT INTO sailors VALUES (107, 'michel', 8, '1991-06-09')"
mycur.execute(s7)
con.commit()
s8="INSERT INTO sailors VALUES (108, 'rohit', 9, '1991-06-09')"
mycur.execute(s8)
con.commit()
#boats
b1="INSERT INTO boats VALUES (110,'a','red')"
mycur.execute(b1)
con.commit()
b2="INSERT INTO boats VALUES (111,'b','green')"
mycur.execute(b2)
con.commit()
b3="INSERT INTO boats VALUES (112,'c','blue')"
mycur.execute(b3)
con.commit()
b4="INSERT INTO boats VALUES (113,'d','red')"
mycur.execute(b4)
con.commit()
b5="INSERT INTO boats VALUES (114,'e','green')"
mycur.execute(b5)
con.commit()
b6="INSERT INTO boats VALUES (115,'f','white')"
mycur.execute(b6)
con.commit()
#reseves
r1="INSERT INTO reserves VALUES (101, 110,'2022-09-08', '9am-6pm')"
mycur.execute(r1)
con.commit()
r2="INSERT INTO reserves VALUES (101, 111,'2022-09-08', '10am-6pm')"
mycur.execute(r2)
con.commit()
r3="INSERT INTO reserves VALUES (101, 112,'2022-10-08', '9am-6pm')"
mycur.execute(r3)
con.commit()
r4="INSERT INTO reserves VALUES (101, 113,'2022-09-27', '11am-8pm')"
mycur.execute(r4)
con.commit()
r5="INSERT INTO reserves VALUES (101, 114,'2022-10-08', '9am-6pm')"
mycur.execute(r5)
con.commit()
r6="INSERT INTO reserves VALUES (101, 115,'2022-09-08', '10am-5pm')"
mycur.execute(r6)
con.commit()
r7="INSERT INTO reserves VALUES (102, 111,'2022-06-24', '10am-6pm')"
mycur.execute(r7)
con.commit()
r8="INSERT INTO reserves VALUES (103, 110,'2022-08-07', '8am-1pm')"
mycur.execute(r8)
con.commit()
r9="INSERT INTO reserves VALUES (103, 111,'2022-08-17', '9am-3pm')"
mycur.execute(r9)
con.commit()
r10="INSERT INTO reserves VALUES (104, 113,'2022-10-08', '9am-4pm')"
mycur.execute(r10)
con.commit()
r11="INSERT INTO reserves VALUES (105, 112,'2022-11-08', '9am-8pm')"
mycur.execute(r11)
con.commit()
r12="INSERT INTO reserves VALUES (106, 115,'2022-03-08', '11am-6pm')"
mycur.execute(r12)
con.commit()
r13="INSERT INTO reserves VALUES (107, 114,'2021-08-08', '10am-6pm')"
mycur.execute(r13)
con.commit()
#create views
v1="CREATE VIEW r1 AS SELECT sid,sname,rating,dob,bid FROM sailors NATURAL JOIN reserves;"
mycur.execute(v1)
con.commit()
v2="CREATE VIEW r2 AS SELECT bid FROM boats;"
mycur.execute(v2)
con.commit()
v3="CREATE VIEW r3 AS SELECT sid,sname,rating,dob FROM r1;"
mycur.execute(v3)
con.commit()
v4="CREATE VIEW r4 AS SELECT FROM r3 CROSS JOIN r2 EXCEPT SELECT FROM r1;"
mycur.execute(v4)
con.commit()
v5="CREATE VIEW r5 AS SELECT sid,color FROM sailors NATURAL JOIN reserves NATURAL JOIN boats;"
mycur.execute(v5)
con.commit()
v6="CREATE VIEW r6 AS SELECT DISTINCT color FROM boats;"
mycur.execute(v6)
con.commit()
v7="CREATE VIEW r7 AS SELECT sid FROM r5;"
mycur.execute(v7)
con.commit()
v8="CREATE VIEW r8 AS SELECT* FROM r7 CROSS JOIN r6 EXCEPT SELECT * FROM r5;"
mycur.execute(v8)
con.commit()
#a
a="SELECT sid,sname,rating,dob FROM sailors NATURAL JOIN reserves;"
print("a")
mycur.execute(a)
rec=mycur.fetchall()
for i in rec:
    print(i)
#b
b="SELECT sname FROM sailors NATURAL JOIN reserves NATURAL JOIN boats WHERE MONTH(reserves.date)=3;"
print("b")
mycur.execute(b)
rec=mycur.fetchall()
for i in rec:
    print(i)
#c
c="SELECT sname from sailors WHERE sid IN(SELECT sid FROM r5 EXCEPT SELECT sid FROM r8);"
print("c")
mycur.execute(c)
rec=mycur.fetchall()
for i in rec:
    print(i)
#d
d="SELECT sid FROM sailors EXCEPT SELECT sid FROM sailors NATURAL JOIN reserves WHERE reserves.date>'2022-08-07';"
print("d")
mycur.execute(d)
rec=mycur.fetchall()
for i in rec:
    print(i) 
#e
e="SELECT * FROM sailors WHERE rating>(SELECT rating FROM sailors WHERE sname='mohan');"
print("e")
mycur.execute(e)
rec=mycur.fetchall()
for i in rec:
    print(i)
#f
f="SELECT sid,sname,rating,dob FROM r1 EXCEPT SELECT sid,sname,rating,dob FROM r4;"
print("f")
mycur.execute(f)
rec=mycur.fetchall()
for i in rec:
    print(i)
#g
g="SELECT sname, TIMESTAMPDIFF(YEAR,dob, CURDATE()) AS Age from sailors where dob IN(SELECT MIN(dob) FROM sailors);"
print("g")
mycur.execute(g)
rec=mycur.fetchall()
for i in rec:
    print(i)
#h
h="SELECT TIMESTAMPDIFF(YEAR,dob,CURDATE()) AS Age FROM sailors WHERE dob IN(SELECT MAX(dob) FROM sailors GROUP BY rating);"
print("h")
mycur.execute(h)
rec=mycur.fetchall()
for i in rec:
    print(i)