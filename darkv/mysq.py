import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='pavan', passwd='pavan', database='vasthadb')
mycursor = mydb.cursor()
mycursor.execute("Create table beforelogin (id int auto_increment, Doctor varchar(100), Medications varchar(100), Appointment varchar(100), primary key (id))")
sql = "insert into beforelogin (Doctor, Medications, Appointment) values (%s, %s, %s)"
details = [('Dr.krishna murthy', 'cardiology', 'available'), ('Dr.Vishweshwar', 'Infected disease', 'available'), ('Dr.Veera', 'Otoaryngology','Available'), ('Dr.Jhansi', 'General surgen','Available'),('Dr.Meera','Orthopaedics', 'Available'),('Dr.Murthy', 'Endocrinology', 'Available'),('Dr.Kishore','Surgen','Available'), ('Dr.Raj kumar', 'Dentist', 'Available')]
mycursor.executemany(sql, details)
mycursor.execute("select * from vasthadb.beforelogin")
my = mycursor.fetchall()
mydb.commit()
for b in my:
    print(b)
#mycursor.execute('select Appointment from vasthadb.r')
#me = mycursor.fetchone()
#for i in me:
#    print(i)
mycursor.execute('create table logintable (id int auto_increment primary key, Doctor varchar(100), Medications varchar(100), Dates varchar(30), Price decimal(6,2) not null, Appointment boolean)')
inse = 'insert into logintable (Doctor,Medications, Dates, Price, Appointment) values (%s, %s, %s, %s, %s)'
ins = [('Dr.krishna murthy', 'cardiology', 'Oct.31, 2019', 699.99, 0), ('Dr.Vishweshwar', 'Infected disease', 'Oct.4, 2019', 899.99, 0), ('Dr.Veera', 'Otoaryngology', 'Oct.10, 2019', 599.99, 0), ('Dr.Jhansi', 'General surgen', 'Oct.14, 2019', 799.99, 0), ('Dr.Meera', 'Orthopaedics', 'oct.12, 2019', 888.99, 0), ('Dr.Murthy', 'Endocrinology', 'Oct.15, 2019', 799.99, 0), ('Dr.Kishore', 'Surgen', 'Oct.17, 2019', 999.99, 0), ('Dr.Raj kumar', 'Dentist', 'Dec.2, 2109', 899.99,0)]
mycursor.executemany(inse, ins)
mycursor.execute('select * from vasthadb.logintable')
result = mycursor.fetchall()
mydb.commit()
for i in result:
    print(i)