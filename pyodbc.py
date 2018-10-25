import pyodbc
server = 'alexasql.database.windows.net'
database = 'AdventureWorks2016'
username = 'cmps253'
password = 'Cmps205!'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
name = input("Please enter firstName")
cursor.execute("SELECT TOP 10 firstName, lastName from Person.Person \n WHERE firstName ="+name+";")
row = cursor.fetchone()
while row:
   print ('Firstname:'+ row[0] +"LastName: " + row[1] )
   row = cursor.fetchone()