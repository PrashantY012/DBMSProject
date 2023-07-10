import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd=None,database="project")
mycusor=mydb.cursor()

# ~~~~~~~~~~~~~~~~creating database~~~~~~~~~~~
# mycusor.execute("create database project")
# creating table manga_writer
# mycusor.execute("create table manga_writer(name varchar(20),dob date,m_id int primary key)");

# inserting values into manga writer
# mycusor.execute("insert into manga_writer values('ram','2000-02-21',1) ")
# mycusor.execute("insert into manga_writer values('ram','2000-02-23',2) ")
# mycusor.execute("insert into manga_writer values('sam','2000-02-21',3) ")
# mycusor.execute("insert into manga_writer values('max','2000-02-23',4) ")
# mycusor.execute("insert into manga_writer values('ankit','2000-02-23',5) ")
# mycusor.execute("insert into manga_writer values('max','2000-03-25',6) ")
# mycusor.execute("insert into manga_writer values('sam','2000-03-25',7) ")
# mycusor.execute("insert into manga_writer values('ankit','2000-03-25',8) ")
# mydb.commit()

# ~~~~~~~~~~~~~~creating table department~~~~~~~~~~~~~~~~
# mycusor.execute("create table department(d_name varchar(20),d_id int primary key    )")

# inserting values in table department
# mycusor.execute("insert into department values ('writing',1 ) ")
# mycusor.execute("insert into department values ('voice', 2) ")
# mycusor.execute("insert into department values ('animatio',3 ) ")
# mycusor.execute("insert into department values ('motion_art',4 ) ")
# mycusor.execute("insert into department values ('digital_imagery',5 ) ")
# mycusor.execute("insert into department values ('transport',6 ) ")
# mycusor.execute("insert into department values ('catering_crew',7 ) ")
# mycusor.execute("insert into department values ('coordinator',8 ) ")
# mydb.commit()
mycusor.execute("select* from anime_writes_releases_produces");
for x in mycusor:
    print(x)

# ~~~~~~~~~~~~~creating table release group~~~~~~~~~~~~~~~~~
# mycusor.execute("create table release_grp(platform varchar(20),release_date\
#  date, r_id int primary key     )")

# ~~~~~~~~inserting values into release group ~~~~~~~~~~~~~~
# mycusor.execute("insert into release_grp values('hotstar','2022-02-21',1)")
# mycusor.execute("insert into release_grp values('disney','2022-02-05',2)")
# mycusor.execute("insert into release_grp values('netflix','2022-02-05',3)")
# mycusor.execute("insert into release_grp values('amazon','2022-02-13',4)")
# mycusor.execute("insert into release_grp values('disney','2022-02-15',5)")
# mycusor.execute("insert into release_grp values('hotstar','2022-02-13',6)")
# mycusor.execute("insert into release_grp values('netflix','2022-02-15',7)")
# mycusor.execute("insert into release_grp values('amazon','2022-02-21',8)")
# mydb.commit()

# creating table production_team
# mycusor.execute("create table production_team (prod_name varchar(20),prod_id int primary key)")

# ~~~~~~~~~~~~~~~~~~~~~~~~~inserting into production_team values~~~~~~~~~~~~~~~~~~
# mycusor.execute(" insert into production_team values('alpha',1 )")
# mycusor.execute(" insert into production_team values('fast',2 )")
# mycusor.execute(" insert into production_team values('lion',3 )")
# mycusor.execute(" insert into production_team values('strong',4 )")
# mycusor.execute(" insert into production_team values('golden',5 )")
# mycusor.execute(" insert into production_team values('fox',6 )")
# mycusor.execute(" insert into production_team values('alpha',7 )")
# mycusor.execute(" insert into production_team values('strong',8 )")
# mydb.commit()


# create table has_department
# mycusor.execute("create table has_department(d_id int,prod_id int ,constraint primary key\
# (d_id,prod_id),constraint foreign key (d_id) references department(d_id) on delete cascade on \
# update cascade,constraint\
#  foreign key (prod_id) references production_team(prod_id)  on delete cascade on update cascade )")

# ~~~~~~~~~~~~inserting values~~~~~~~~~~~~~~~~

# mycusor.execute("insert into has_department values(1,2) " )
# mycusor.execute("insert into has_department values(6,2) " )
# mycusor.execute("insert into has_department values(8,4) " )
# mycusor.execute("insert into has_department values(5,6) " )
# mycusor.execute("insert into has_department values(6,7) " )
# mycusor.execute("insert into has_department values(5,4) " )
# mycusor.execute("insert into has_department values(8,7) " )
# mycusor.execute("insert into has_department values(1,6) " )
# mydb.commit()
# 1
# creating table emp_worksin
# mycusor.execute("create table emp_worksin(emp_id int primary key,emp_name\
#  varchar(20),dob date,d_id int,foreign key (d_id) references department(d_id)\
#   on delete cascade on update cascade       ) ")

# inserting values
# mycusor.execute("insert into emp_worksin values(1,'ram','2000-02-01',1  )")
# mycusor.execute("insert into emp_worksin values(2,'shyam','2000-02-02',1  )")
# mycusor.execute("insert into emp_worksin values(3,'mohan','2000-02-11',4  )")
# mycusor.execute("insert into emp_worksin values(4,'mohan','2000-02-05',5  )")
# mycusor.execute("insert into emp_worksin values(5,'rose','2000-02-05',4 )")
# mycusor.execute("insert into emp_worksin values(6,'shyam','2000-02-11',5  )")
# mycusor.execute("insert into emp_worksin values(7,'ram','2000-02-02',6  )")
# mycusor.execute("insert into emp_worksin values(8,'rose','2000-02-01',6  )")
# mydb.commit()


# # creating table anime_writes_releases_produces
# mycusor.execute("create table anime_writes_releases_produces\
# (genre varchar(20),name varchar(20),rating int, a_id int primary key,m_id int,r_id int,prod_id int,\
# foreign key(m_id) references manga_writer(m_id)  on delete cascade on update cascade \
# ,foreign key(r_id)\
#  references release_grp (r_id)   on delete cascade on update cascade \
# ,foreign key(prod_id) references production_team(prod_id)  \
# on delete cascade on update cascade )")

# inserting values
# mycusor.execute("  insert into anime_writes_releases_produces values ('detective','death_note',10,1,2,3,4 )")
# mycusor.execute("  insert into anime_writes_releases_produces values ('super_natural','aot',9,2,5,4,3 )")
# mycusor.execute("  insert into anime_writes_releases_produces values ('action','bleach',9,3,6,4,3 )")
# mycusor.execute("  insert into anime_writes_releases_produces values ('mystery','made_in_abyss',8,4,8,7,5 )")
# mycusor.execute("  insert into anime_writes_releases_produces values ('action','hunterXhunter',8,5,8,6,6 ) ")
# mycusor.execute("  insert into anime_writes_releases_produces values ('action','dbz',6,6,4,5,1 )")
# mycusor.execute("  insert into anime_writes_releases_produces values ('adventure','pokemon',7,7,8,2,3 )")
# mycusor.execute("  insert into anime_writes_releases_produces values ('kid','doremon',7,8,3,4,6 )")
# mydb.commit()


# Query:print the name of manga with highest rating
# mycusor.execute("select name from anime_writes_releases_produces where rating \
#     =(select MAX(rating) from  anime_writes_releases_produces)")
# for x in mycusor:
#     print(x)

# Query:print the author of the highest rated manga
# mycusor.execute("select name from manga_writer where m_id IN (\
#     select m_id from anime_writes_releases_produces where rating \
#      =(select MAX(rating) from  anime_writes_releases_produces)\
# )")
# for x in mycusor:
#     print(x)

# Query:print the name of manga with lowest rating
# mycusor.execute("select name from anime_writes_releases_produces where rating \
#     =(select MIN(rating) from  anime_writes_releases_produces)")
# for x in mycusor:
#     print(x)


# Query:print the author of the lowest rated manga
# mycusor.execute("select name from manga_writer where m_id IN (\
#     select m_id from anime_writes_releases_produces where rating \
#      =(select MIN(rating) from  anime_writes_releases_produces)\
# )")
# for x in mycusor:
#     print(x)


