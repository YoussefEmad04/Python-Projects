import sqlite3
class Database:
    def __init__(self,db):#schedual
        self.con= sqlite3.connect(db)
        self.cur= self.con.cursor()



        sql="""
        CREATE TABLE IF NOT EXISTS employees(
            id Integer Primary key,
            name text,
            age text,
            job text,
            email text,
            gender text,
            mobile text,
            address text
        )
        
        """
        #attributes
        self.cur.execute(sql)#connection with data base
        self.con.commit()#connect

    def insert(self,name,age,job,email,gender,mobile,address):#function to insert data DEF ADD EMPLOYEEEE
        self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,?)",
                         (name,age,job,email,gender,mobile,address))
        self.con.commit()

    def fetch(self):#function to bring data  DEF DISPLAY ALLLL
        self.cur.execute("SELECT * FROM employees")
        rows = self.cur.fetchall()# fetch reponsible for all things inside employees rows
        return rows
    
    def remove(self,id):#function to remove data
        self.cur.execute(" delete from employees where id=?",(id,))
        self.con.commit()

    def update(self,id,name,age,job,email,gender,mobile,address):
        self.cur.execute("update employees set name=?, age=?,job=?,email=?,gender=?,mobile=?,address=? where id=?",
                         (name,age,job,email,gender,mobile,address,id))
        self.con.commit()

