import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="employee")

mycursor = conn.cursor()

mycursor.execute("insert into employee (name, EmployeeID, Salary)values(%s,%s,%s)", ('Cloudy', 'E007', 69000.00))
conn.commit()


