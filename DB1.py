import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mysql1210",
    database = "pythoncon",
    auth_plugin = "mysql_native_password"
)
mycur = mydb.cursor()
# s = "insert into school(rno, name, address, phone, age) values (1, 'Amit', 'abc', 123456, 12)" Static way
rno = int(input("Enter Roll number: "))
name = input("Enter Student name: ")
address = input("Enter Student Address: ")
phone = int(input("Enter Student Phone Number: "))
age = int(input("Enter Student Age: "))
s = "insert into school(rno, name, address, phone, age) values(%s, %s,%s, %s, %s)"
values = (rno, name, address, phone, age)

mycur.execute(s, values)
mydb.commit()
print("Data Successfully inserted.....")
