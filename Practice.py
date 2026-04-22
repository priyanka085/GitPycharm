import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="employee")

mycursor = conn.cursor()

mycursor.execute("insert into employee (name, EmployeeID, Salary)values(%s,%s,%s)", ('Mark', 'E008', 75000.00))
conn.commit()


