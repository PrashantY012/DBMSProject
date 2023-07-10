import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd=None,database="testdatabase")
mycursor=mydb.cursor();
# mycursor.execute("create database testdatabase")
# mycursor.execute("create table testtable(name varchar(30),roll_no int ,class varchar(2), constraint pk_testtable primary key (roll_no) )")
# mycursor.execute("insert into testtable values('prashant',1,'XII')")
# mydb.commit()
# mycursor.execute("describe testtable")
# mycursor.execute("insert into testtable values('alpha',2,'XII')")
# mycursor.execute("insert into testtable values('beta',3,'XII')")
# mydb.commit()
mycursor.execute("select * from testtable ")
for x in mycursor:
    print(x)



insert into anime_writes_releases_produces values ('detective','death_note',10,1,2,3,4 )
insert into anime_writes_releases_produces values ('super_natural','aot',9,2,5,4,3 )
insert into anime_writes_releases_produces values ('action','bleach',9,3,6,4,3 )
insert into anime_writes_releases_produces values ('mystery','made_in_abyss',8,4,8,7,5 )
insert into anime_writes_releases_produces values ('action','hunterXhunter',8,5,8,6,6 ) 
insert into anime_writes_releases_produces values ('action','dbz',6,6,4,5,1 )
insert into anime_writes_releases_produces values ('adventure','pokemon',7,7,8,2,3 )
insert into anime_writes_releases_produces values ('kid','doremon',7,8,3,4,6 )