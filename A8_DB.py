import sqlite3

conn=sqlite3.connect("student.db")
c=conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS STUDENT(
usn TEXT PRIMARY KEY,
name TEXT NOT NULL,
sem INTEGER NOT NULL CHECK(sem>=1),
branch TEXT NOT NULL,
cgpa REAL NOT NULL CHECK(cgpa>=0 AND cgpa<=10)
)''')



def disp():
    print("\nUSN\t\tName\t\tSem\t\tBranch\t\tCGPA")
    c.execute("SELECT * FROM STUDENT")
    rows=c.fetchall()
    for i in rows:
        print("%s\t\t%s\t\t%s\t\t%s\t\t%s"%i)

def insert():
    n=int(input("Enter no. of rows: "))
    i=0
    while i<n:
        i+=1
        try:
            usn=input("\nEnter USN : ")
            name=input("Enter Name : ")
            sem=int(input("Enter Semester : "))
            branch=input("Enter Branch: ")
            cgpa=float(input("Enter CGPA : "))
            c.execute("INSERT INTO STUDENT VALUES(?,?,?,?,?)",(usn,name,sem,branch,cgpa))
        except:
            print("Invalid Input")
            i-=1

def search():
    usn=input("\nSearch USN : ")
    c.execute("SELECT * FROM STUDENT WHERE usn=?",(usn,))
    row=c.fetchone()
    if(row!=None):
        print("\nUSN\t\tName\t\tSem\t\tBranch\t\tCGPA")
        print("%s\t\t%s\t\t%s\t\t%s\t\t%s"%row)
    else:
        print("\nInvalid USN")

def update():
    try:
        usn=input("\nUpdate USN : ")
        name=input("Enter Name : ")
        sem=int(input("Enter Semester : "))
        branch=input("Enter Branch: ")
        cgpa=float(input("Enter CGPA : "))
        c.execute("UPDATE STUDENT SET Name=?,Sem=?,branch=?,CGPA=? where usn=?",(name,sem,branch,cgpa,usn))
    except:
        print("Invalid Input")

def delete():
    try:
        usn=input("\nDelete USN : ")
        c.execute("DELETE FROM STUDENT  where usn=?",(usn,))
    except:
        print("Invalid Input")

o=0  
while o!=6:
    print('''
1. Insert
2. Search
3. Update
4. Delete
5. Display
6. Exit
''')
    o=int(input("Enter choice : "))
    if o==1:
        insert()
    elif o==2:
        search()
    elif o==3:
        update()
    elif o==4:
        delete()
    elif o==5:
        disp()
    elif o!=6:
        print("Invalid Input")
    
conn.commit()
conn.close()
