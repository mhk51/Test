import pyodbc
outputfileHandle = open('persons.html','w',encoding = 'UTF-8')
server = 'alexasql.database.windows.net'
database = 'AdventureWorks2016'
username = 'cmps253'
password = 'Cmps205!'
driver='{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT top 10 * from Person.Person")
row = cursor.fetchone()
outputfileHandle.write("<html>\n"+"<head>"+"</head>")
outputfileHandle.write("<body>\n"+"<table border = 1>\n")
while row:
    outputfileHandle.write("<tr><td>" + row[4] + "</td><td>" + row[6] + "</tr>\n")
    row = cursor.fetchone()
outputfileHandle.write("</table>"+"</body>"+"</html>")
outputfileHandle.close()