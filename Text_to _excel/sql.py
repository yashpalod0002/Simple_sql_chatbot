import sqlite3

##connect to sqlite
connection=sqlite3.connect("student.db")
cursor=connection.cursor()
cursor.execute("DROP TABLE IF EXISTS STUDENT")
##create a table
tabel_info="""
Create  table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(tabel_info)

cursor.execute('''Insert Into STUDENT valueS('KRISH','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT valueS('YASH','Data Science','B',110)''')
cursor.execute('''Insert Into STUDENT valueS('Aman','AI&ML','B',110)''')
cursor.execute('''Insert Into STUDENT valueS('Aman','AI','C',110)''')

print("The Inserted records are: ")

data=cursor.execute('''SELECT * FROM STUDENT''')

for row in data:
    print(row)
    

