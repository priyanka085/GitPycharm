import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="employee")

mycursor = conn.cursor()

sql ="insert into employee (name, EmployeeID, salary) values (%s, %s, %s)"
values = [
    ('Alice', 'E006', 60000.00),
    ('Bob', 'E009', 65000.00),
    ('Charlie', 'E010', 72000.00)
]
mycursor.executemany(sql, values)
conn.commit()


