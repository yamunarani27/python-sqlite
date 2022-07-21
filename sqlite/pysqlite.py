import sqlite3


#creating connection with database and creating cursor object to communicate with database
conn=sqlite3.connect("users.db")
c=conn.cursor()


# #create a table(datatype null,text,integer,real,blob)
c.execute("""CREATE TABLE IF NOT EXISTS user(
    first_name text,
    last_name text,
    age integer
 )""")

#insert values into table
def add_record(fname,lname,age):
     conn=sqlite3.connect("users.db")
     c=conn.cursor()

     c.execute("INSERT INTO user VALUES (?,?,?)",(fname,lname,age))

     conn.commit()
     conn.close()

#insert many values into table
def addmany_records(list):
     conn=sqlite3.connect("users.db")
     c=conn.cursor()

     c.executemany("INSERT INTO user VALUES (?,?,?)",(list))

     conn.commit()
     conn.close()

#update data in the table
def update_record(nname,fname):
    conn=sqlite3.connect("users.db")
    c=conn.cursor()
    mydata=(nname,fname)
    c.execute("UPDATE user  SET first_name=? WHERE first_name=? ",mydata)

    conn.commit()
    conn.close()

 
#delete a record(for id in single digit we  can use id but if ots double digit should use (id,) or [id])
def delete_record(id):
    conn=sqlite3.connect("users.db")
    c=conn.cursor()
    
    c.execute(" DELETE from user WHERE rowid=(?)",(id,))

    conn.commit()
    conn.close()

# fetch data from table(fetchone,fetchall,fetchmany)
def fetchone_record(id):
     conn=sqlite3.connect("users.db")
     c=conn.cursor()
    
     c.execute("SELECT * FROM user WHERE rowid=? ",(id))
     print(c.fetchone())


# fetch data from table(fetchone,fetchall,fetchmany)
def fetchall_record():
     conn=sqlite3.connect("users.db")
     c=conn.cursor()
    
     c.execute("SELECT rowid,* FROM user")
     print(c.fetchall())

#displkay descending
def disp_des():
    conn=sqlite3.connect("users.db")
    c=conn.cursor()
    
    c.execute("SELECT * FROM user ORDER BY rowid DESC")
    print(c.fetchall())

#to delete a table
#c.execute(DROP TABLE user)
#commit the changes and close the connection
# conn.commit()
# conn.close()

#for parameter of unsupported type error use the id value as string when passing as arguments