import mysql.connector
mydb=mysql.connector.connect(host="localhost" ,passwd=None ,user="root",database="sea")
mycursor=mydb.cursor()
# ~~~~~~~~~~~~~creating database~~~~~~~~~~~~~~~~
# mycursor.execute("create database sea")

# ~~~~~~~~~~~~~creating table strucutre of table SAILORS~~~~~~~~~~~~~~~~~~~~~
# mycursor.execute("create table SAILORS (sid int,sname varchar(20),rating int,date_of\
#     _birth date,constraint PK_SAILORS primary key(sid))")

# ~~~~~~~~~~~~~~~~~~~inserting into values into SAILORS ~~~~~~~~~~~~~~~~~~~
# mycursor.execute("insert into SAILORS values(21,'prashant',9,'1998-07-21')")
# mycursor.execute("insert into SAILORS values(31,'harsh',10,'1998-08-31')")
# mycursor.execute("insert into SAILORS values(17,'pavitra',7,'1998-01-14')")
# mycursor.execute("insert into SAILORS values( 16,'ram', 6 ,'1998-12-27')")
# mycursor.execute("insert into SAILORS values( 13,'yash',8  ,'1998-12-23')")
# mycursor.execute("insert into SAILORS values( 7,'sid',5  ,'1998-11-08')") 
# mycursor.execute("insert into SAILORS values( 25,'sam',8  ,'1998-10-23')")
# mycursor.execute("insert into SAILORS values( 12,'vikas', 3 ,'1998-06-21')")
# mycursor.execute("insert into SAILORS values( 3,'kartik',6  ,'1998-04-30')")
# mycursor.execute("insert into SAILORS values( 5,'gopal', 2 ,'1998-05-11')")
# mydb.commit()

# ~~~~~~~creating table structure of table BOATS~~~~~~~~~~~~~~
# mycursor.execute("create table BOATS(bid int ,bname varchar(20),color varchar(20),constraint 
# PK_BOATS primary key(bid)   )")

# ~~~~~~~~~~~~~~~~~inserting values into table BOATS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# mycursor.execute("insert into BOATS values( 101, 'roger' ,'gold')")
# mycursor.execute("insert into BOATS values(113 , 'roger' ,'blue')")
# mycursor.execute("insert into BOATS values( 123, 'bucky' ,'green')")
# mycursor.execute("insert into BOATS values( 111, 'shank' ,'red')")
# mycursor.execute("insert into BOATS values(116 , 'beard' ,'white')")
# mycursor.execute("insert into BOATS values( 144, 'teach' ,'black')")
# mycursor.execute("insert into BOATS values( 107,'knight' ,'white')")
# mycursor.execute("insert into BOATS values( 109, 'luxury' ,'green')")
# mycursor.execute("insert into BOATS values( 151, 'classic' ,'blue')")
# mycursor.execute("insert into BOATS values( 177, 'economic' ,'yellow')")
# mydb.commit()


# ~~~~~~~~~~~~~~~~~~~~~creating table ~~~~~~~~~~~~~~~~~~~~~~~~~
# mycursor.execute("create table RESERVES ( date_reserves date, time_slot varchar(20),sid int ,bid int,
# primary key(sid,bid,date_reserves,time_slot), foreign key (sid) references SAILORS(sid) on delete cascade on update 
# cascade , foreign key (bid) references BOATS(bid)  on delete cascade on update cascade    ) ")

# ~~~~~~~~~~~~~~~~inseting values into table RESERVES~~~~~~~~~~~~~~~~
# mycursor.execute("insert into Reserves values('1998-02-24','15:00-17:00',5 , 113)")
# mydb.commit()
# mycursor.execute("insert into Reserves values('1998-01-22','12:00-03:00', 3, 177)")
# mydb.commit()
# mycursor.execute("insert into Reserves values('1998-03-16','06:00-08:00',3 ,123 )")
# mydb.commit()
# mycursor.execute("insert into Reserves values('1998-06-18','21:00-24:00', 12, 109)")
# mydb.commit()
# mycursor.execute("insert into Reserves values('1998-12-14','08:00-19:00', 12, 151)")
# mydb.commit()
# mycursor.execute("insert into Reserves values('1998-03-16','11:00-13:00', 25, 123)")
# mydb.commit()
# mycursor.execute("insert into Reserves values('1998-08-17','09:00-21:00', 25, 111)")
# mydb.commit()
# mycursor.execute("insert into Reserves values('1998-07-21','14:00-16:00', 21,111 )")
# mydb.commit()
# mycursor.execute("insert into Reserves values('1998-06-08','04:00-07:00',17 ,116 )")

# mydb.commit()

# mycursor.execute("alter table reserves add constraint foreign key(sid) references sailors(sid) ")

# ~~~~~~~~~~~~~~~~~~~~queries~~~~~~~~~~~~~~~~~~~~~~~~

# 1
# mycursor.execute("select distinct sailors.sid , sailors.sname from sailors, \
# reserves where sailors.sid=reserves.sid ")
# for x in mycursor:
#     print(x)

#2  
# mycursor.execute("select sname from sailors where sid in \
# (select distinct sid from reserves where date_reserves between '1998-03-01' AND '1998-03-31'   \
# AND bid IN   ( select bid from boats where color='red' or color ='green')  )")
    
# for x in mycursor:
#     print(x)

#3
# mycursor.execute("select sailors.sname from sailors where sailors.sid  \
# in (select reserves.sid from reserves join boats on reserves.bid = boats.bid where boats.color = 'red' and \
# reserves.sid in (select reserves.sid from reserves join boats \
# where boats.bid = reserves.bid and color = 'green' )) ")

# for x in mycursor:
#     print(x)

4
# mycursor.execute("select sid from sailors \
# where sid not in (select distinct sid from reserves where date_reserves > '2018-01-31'); ")

# for x in mycursor:
#     print(x)

5
# mycursor.execute(" select sailors.sname , sailors.sid , sailors.rating from sailors \
# where sailors.rating >\
# (select sailors.rating from sailors where sailors.sname = 'ram'); ")
# for x in mycursor:
#     print(x)


# 6
# mycursor.execute(" select sailors.sname , sailors.sid , derived.counts \
# from sailors join (select sid , count(distinct reserves.bid) as counts \
# from reserves group by reserves.sid) as derived \
# on derived.sid = sailors.sid where counts = (select count(bid) from boats);")

# for x in mycursor:
#     print(x)

# 7
# mycursor.execute("select sname , floor(datediff(current_date() , date_of_birth)/365) as age \
# from sailors where date_of_birth in\
# (select min(date_of_birth) from sailors); ")
# for x in mycursor:
#     print(x)

# 8
# mycursor.execute("select min(floor(datediff(current_date() , date_of_birth)/365)) as age\
# , rating  from sailors group by rating having count(*) > 1; ")
# for x in mycursor:
#     print(x)



