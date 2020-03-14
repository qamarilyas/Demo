import mysql.connector

mydb=mysql.connector.connect(host="localhost", user="qamar", passwd="1234",database='demo')
mycursor=mydb.cursor()

#prinitng all the databases
mycursor.execute("show databases")
for i in mycursor:
    print (i)

#prinitng all the values in table
# for using table we need to mention the database name in the connect

mycursor.execute("select * from students")
for i in mycursor:
    print (i)

## There is better way, instead of using the cursor directly, We may use fecthall from cursor.
mycursor.execute("select * from students")
result=mycursor.fetchall()
#to fecth one result use fetchone
for i in result:
    print(i)