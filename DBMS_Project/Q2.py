import mysql.connector

mydb=mysql.connector.connect(host="localhost" ,user="root",passwd=None,database="store")
mycursor=mydb.cursor()

# ~~~~~~~~creating database~~~~~~~~~~~
# mycursor.execute("create database store")

# ~~~~~~~~~~~~~~creating table~~~~~~~~~~~~~~~~~
# mycursor.execute("create table customer(cust_num int,cust_lname varchar(20) ,cust_fname varchar(20),\
#  cust_balance int  ,constraint PK_CUSTOMER primary key (cust_num) )")

# ~~~~~~~~~~~~~~~~~~inseting data into table customer~~~~~~~~~~~~~~~~~~~~~~~~~
# mycursor.execute("insert into CUSTOMER values( 1  , 'yadav','prashant',150000 )    ")
# mycursor.execute("insert into CUSTOMER values( 2, 'singh','gaurav',0 )    ")
# mycursor.execute("insert into CUSTOMER values(3 , 'nandan','shivesh',900000 )    ")
# mycursor.execute("insert into CUSTOMER values(4 , 'singh','navjot',200000 )    ")
# mycursor.execute("insert into CUSTOMER values(5 , 'misra','vishal', 65000)    ")
# mycursor.execute("insert into CUSTOMER values(6 , 'misra','tarushi', 0)    ")
# mycursor.execute("insert into CUSTOMER values( 7, 'kumari','saumya',70000 )    ")
# mycursor.execute("insert into CUSTOMER values(8 , 'randhava','riya', 0)    ")
# mycursor.execute("insert into CUSTOMER values( 9, 'dicapiro','leonardo', 90000)    ")
# mycursor.execute("insert into CUSTOMER values(10 , 'maxwell','sam',50000 )    ")
# mydb.commit()

# ~~~~~~~~~~~~~~~~~~~creating table product~~~~~~~~~~~~~~~~~
# mycursor.execute("create table PRODUCT(prod_num int primary key,prod_name varchar(20),price int)")

# ~~~~~~~~~~~~~~~~inserting values into table PRODUCT~~~~~~~~~~~~~~~~~~~
# mycursor.execute("insert into PRODUCT values( 1,'mobile_cover' ,300 ) ")
# mycursor.execute("insert into PRODUCT values(2,'mobile' ,10000 ) ")
# mycursor.execute("insert into PRODUCT values(3,' tv' , 50000) ")
# mycursor.execute("insert into PRODUCT values(4,'oven ' ,10000 ) ")
# mycursor.execute("insert into PRODUCT values(5,'washing_machine ' ,25000 ) ")
# mycursor.execute("insert into PRODUCT values(6,' fridge' ,30000 ) ")
# mycursor.execute("insert into PRODUCT values(7,' watch' ,3000 ) ")
# mycursor.execute("insert into PRODUCT values(8,' sun_glass' ,8000 ) ")
# mycursor.execute("insert into PRODUCT values(9,' laptop' ,60000 ) ")
# mycursor.execute("insert into PRODUCT values(10,'book ' ,1200 ) ")
# mydb.commit()

# ~~~~~~~~~~~~~creating table invoice~~~~~~~~~~~~~~~~~~~~~
# mycursor.execute("create table INVOICE(inv_num int,prod_num int,cust_num \
# int,inv_date date,unit_sold int,inv_amount int , constraint primary key \
# (inv_num,prod_num,cust_num,inv_date),constraint foreign key (cust_num) \
# references CUSTOMER(cust_num) on delete cascade on update cascade,constraint\
#  foreign key(prod_num) references PRODUCT(prod_num) on delete cascade on update cascade   )  ")

# ~~~~~~~~~~~~~~~~~inserting values into invoice~~~~~~~~~~~~~~~~~~~~~
# mycursor.execute("insert into INVOICE values(1 ,2 ,3 , '2016-08-21' , 3,30000)")
# mycursor.execute("insert into INVOICE values( 2,3 ,3 , '2016-08-22' , 1,50000)")
# mycursor.execute("insert into INVOICE values( 3, 4, 4, '2016-08-23' , 6,60000)")
# mycursor.execute("insert into INVOICE values( 4, 5, 5, '2016-08-21' , 2,50000)")
# mycursor.execute("insert into INVOICE values( 5, 6,6 , '2016-08-25' ,1 ,30000)")
# mycursor.execute("insert into INVOICE values( 6,7 , 7, '2016-08-21' ,11 ,33000)")
# mycursor.execute("insert into INVOICE values( 7, 8,9 , '2016-08-23' ,3 ,24000)")
# mycursor.execute("insert into INVOICE values( 8, 9, 9, '2016-08-23' ,1 ,60000)")
# mycursor.execute("insert into INVOICE values( 9, 10, 10, '2016-08-23' ,10 ,12000)")
# mycursor.execute("insert into INVOICE values( 10, 1,4 , '2016-08-27' ,50 ,15000)")

# mydb.commit()


# ~~~~~~~~~~~~~~~~~~queries~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1
# mycursor.execute("select CONCAT(cust_fname,'',cust_lname) as name from \
# customer where cust_balance = 0 ")

# for x in mycursor:
#     print(x)


# 2
# mycursor.execute("CREATE TRIGGER check_age before insert on invoice for each ROW UPDATE \
# customer c SET c.cust_balance=c.cust_balance+new.inv_amount WHERE c.cust_num=new.cust_num;")
# mycursor.execute("insert into INVOICE values( 11, 10, 10, '2016-08-23' ,10 ,12000)")
# mydb.commit()
# mycursor.execute("SELECT cust_fname,cust_lname,cust_balance FROM customer where cust_num =10;")
# rec=mycursor.fetchall()
# for i in rec:
#     print(i)

# 3
# mycursor.execute("select cust_num, cust_fname \
# from customer where cust_num in(select \
# cust_num from invoice group by cust_num,inv_date,prod_num having sum(unit_sold)>3);")

# for x in mycursor:
#     print(x)

# 4
# left outer join
# mycursor.execute( " select customer.cust_num ,cust_fname , cust_lname , inv_amount ,inv_date \
# from customer left join invoice on customer.cust_num = invoice.cust_num ")

# for x in mycursor:
#     print(x)

# right outer join
# mycursor.execute("select customer.cust_num ,cust_fname , cust_lname , inv_amount ,inv_date from \
# customer right join invoice on customer.cust_num = invoice.cust_num; ")
# for x in mycursor:
#     print(x)

# full outer join
# mycursor.execute("(select customer.cust_num ,cust_fname , cust_lname , \
# inv_amount ,inv_date from customer left join invoice on customer.cust_num = invoice.cust_num) \
# union (select customer.cust_num ,cust_fname , cust_lname , inv_amount ,inv_date \
# from customer right join invoice on customer.cust_num = invoice.cust_num); ")
# for x in mycursor:
#     print(x)

# 5
# mycursor.execute("select inv_date , sum(unit_sold) \
# from invoice group by \
# inv_date order by inv_date asc;")
# for x in mycursor:
#     print(x)

# 6
# mycursor.execute("select cust_num from (select * from \
# customer where cust_balance > 10000) as gold_customer; ")
# for x in mycursor:
#     print(x)

# 7
# mycursor.execute(" alter table customer add cust_dob date;  ")
# mycursor.execute("select * from customer");
# for x in mycursor:
#     print(x)
                        
                        


