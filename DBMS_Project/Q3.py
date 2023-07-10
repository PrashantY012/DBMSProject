import mysql.connector
mydb=mysql.connector.connect(host="localhost" ,user="root",passwd=None,database="company" )
mycursor=mydb.cursor()

# ~~~~~~~~~~~~~~create database company~~~~~~~~~~~~~
# mycursor.execute("create database company")

# ~~~~~~~~~~~~~~~~creating table structure for table department~~~~~~~~~~~~~~~
# mycursor.execute("create table DEPARTMENT(department_id int primary key, \
# name varchar(20),location varchar(20)   )  ")

# ~~~~~~~~~~~inserting values in table department~~~~~~~~~~~~~~~~~~~~
# mycursor.execute("insert into department values( 1,'research','delhi') ")
# mycursor.execute("insert into department values( 2,'production','mumbai') ")
# mycursor.execute("insert into department values( 3,'analysis','banglore ) ")
# mycursor.execute("insert into department values( 4,'finance','gurgaon') ")
# mycursor.execute("insert into department values( 5,'assemble','taiwan') ")
# mycursor.execute("insert into department values( 6,'advertisement','mumbai') ")
# mycursor.execute("insert into department values( 7,'call','hyderabad') ")
# mycursor.execute("insert into department values( 8,'logistic','ahemdabad') ")
# mycursor.execute("insert into department values( 9,'testing','mumbai') ")
# mycursor.execute("insert into department values( 10,'company_welfare','delhi ) ")
# mydb.commit()

# ~~~~~~~~~~~~~~~~~~~~~~~~~creating table JOB~~~~~~~~~~~~~~~~~~
# mycursor.execute("create table JOB(job_id int primary key,function varchar(20) )")

# ~~~~~~~~~~~~~~~~~~~~~~~inserting values into JOB~~~~~~~~~~~~~~~~~~~~~~~~~
# mycursor.execute("insert into job values (1,'clerk') ")
# mycursor.execute("insert into job values (2,'assistant manager') ")
# mycursor.execute("insert into job values (3,'senior assistant manager') ")
# mycursor.execute("insert into job values (4,'manager') ")
# mycursor.execute("insert into job values (5,'senior manager') ")
# mycursor.execute("insert into job values (6,'superviser') ")
# mycursor.execute("insert into job values (7,'techincal assistant') ")
# mycursor.execute("insert into job values (8,'security') ")
# mydb.commit()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~creating table structure of employee~~~~~~~~~~~~~~~~~~~~~~~~~
# mycursor.execute("create table employee( employee_id int primary key\
# ,name varchar(20),DOB date,job_id int ,manager_id int,hire_date date,\
# salary int,department_id int ,foreign key (job_id) references JOB(job_id)\
# ,foreign key(department_id) references department(department_id)         )   ")

# ~~~~~~~~~~~~~~~~~~~~~~~inserting data into table ~~~~~~~~~~~~~~~~~~~~
# mycursor.execute("insert into employee values(1,'ram','1995-08-01',1,1,'2020-09-21',1000000,1 )")
# mycursor.execute("insert into employee values(2,'shaym','1995-09-15',2,2,'2021-10-22',2000000,2 )")
# mycursor.execute("insert into employee values(3,'sam','1995-01-16',3,3,'2019-11-08',3000000,3 )")
# mycursor.execute("insert into employee values(4,'sourav','1999-02-17',4,4,'2021-03-11',4000000,4 )")
# mycursor.execute("insert into employee values(5,'rudra','1995-05-19',5,5,'2022-05-21',500000, 5)")
# mycursor.execute("insert into employee values(6,'molly','1989-12-31',6,6,'2015-03-01',4500000, 6)")
# mycursor.execute("insert into employee values(7,'normie','1995-11-29',7,7,'2021-02-23',310000,7 )")
# mycursor.execute("insert into employee values(8,'nomu','1995-07-11',8,8,'2022-03-25',3200000,8 )")
# mycursor.execute("insert into employee values(9,'norman','1995-09-21',2,9,'2022-05-26',3100000,9 )")
# mycursor.execute("insert into employee values(10,'rose','1995-10-22',3,10,'2021-04-05',6000000,10 )")
# mydb.commit()

# ~~~~~~~~~~~~~~~~~~~queries~~~~~~~~~~~~~~~~

# 1
# mycursor.execute("select count(employee_id) from \
#     ( select employee_id from employee where hire_date like '%-03-%') as emp; ")

# for x in mycursor:
#     print(x)

# 2
# mycursor.execute("select * from employee where employee.salary not \
# in (select employee.salary from employee cross join employee  \
# as temp on employee.salary < temp.salary );  ")
# for x in mycursor:
#     print(x)

# 3
# mycursor.execute("select employee.department_id , sum(employee.salary) \
# from employee group by department_id;")
# for x in mycursor:
#     print(x)    

# 4
# mycursor.execute(" select department_id , sum(salary) \
# as budget from employee group by department_id \
# order by sum(salary) desc;  ")
# for x in mycursor:
#     print(x)  

# 5
# query= "create view emp_delhi as select count(distinct employee_id)from\
#  (select * from employee natural join department where location='delhi')as temp;"
# query2="select* from emp_delhi;"
# # mycursor.execute(query)
# mycursor.execute(query2)
# rec=mycursor.fetchall()
# print(rec)

# 6
# # query="create trigger verify_age before insert on employee for each \
# # row begin if new.dob>'1995-01-01' then signal sqlstate '45000'\
# # set message_text='error: age must be atleast 25 years!';end if;end;"
# query= mycursor.execute("insert into employee values(11,'rose','2000-10-22',3,10,'2021-04-05',6000000,10 )")
# mycursor.execute(query)
# rec=mycursor.fetchall()
# print(rec)