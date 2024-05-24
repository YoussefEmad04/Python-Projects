from tkinter import * #all things inside library
from tkinter import ttk
from tkinter import messagebox
from db import Database
db = Database("Employee.db")



root=Tk()
root.title("Emplot managent system")
root.geometry("1310x515+0+0")#msa7t el app length width 100+100 center of program on pc
root.resizable(False,False)#m4 h2dr a8yr fe el size aw a3dl feh manual
root.configure(bg="#2c3e50")#color of program

#variable for db.py
name= StringVar()
age= StringVar()
job= StringVar()
gender= StringVar()
email= StringVar()
mobile= StringVar()

#frame for systen
entries_frame=Frame(root,bg='#2c3e50')
entries_frame.place(x=1,y=1,width=360,height=510)
title=Label(entries_frame,text='Employee_company',font=('Calibri',18,'bold'),bg='#2c3e50',fg='white')
title.place(x=10,y=1)

lableName=Label(entries_frame,text="Name",font=('Calibri',16),bg='#2c3e50',fg='white')
lableName.place(x=10,y=50)
txtName=Entry(entries_frame,textvariable=name,width=20,font=('Calibri',16))#entry ya3ni hd5l
txtName.place(x=120,y=50)

lableJob=Label(entries_frame,text="Job",font=('Calibri',16),bg='#2c3e50',fg='white')
lableJob.place(x=10,y=90)
txtJob=Entry(entries_frame,textvariable=job,width=20,font=('Calibri',16))#entry ya3ni hd5l
txtJob.place(x=120,y=90)

lableGender=Label(entries_frame,text="Gender",font=('Calibri',16),bg='#2c3e50',fg='white')
lableGender.place(x=10,y=130)
comboGender=ttk.Combobox(entries_frame,textvariable=gender,state="readonly",width=18,font=('Calibri',16))#male or female
comboGender['values']=("Male","Female")
comboGender.place(x=120,y=130)

lableAge=Label(entries_frame,text="Age",font=('Calibri',16),bg='#2c3e50',fg='white')
lableAge.place(x=10,y=170)
txtAge=Entry(entries_frame,textvariable=age,width=20,font=('Calibri',16))#entry ya3ni hd5l
txtAge.place(x=120,y=170)

lableEmail=Label(entries_frame,text="Email",font=('Calibri',16),bg='#2c3e50',fg='white')
lableEmail.place(x=10,y=210)
txtEmail=Entry(entries_frame,textvariable=email,width=20,font=('Calibri',16))#entry ya3ni hd5l
txtEmail.place(x=120,y=210)

lableMobile=Label(entries_frame,text="Mobile",font=('Calibri',16),bg='#2c3e50',fg='white')
lableMobile.place(x=10,y=250)
txtMobile=Entry(entries_frame,textvariable=mobile,width=20,font=('Calibri',16))#entry ya3ni hd5l
txtMobile.place(x=120,y=250)

lableAddress=Label(entries_frame,text="Address :",font=('Calibri',16),bg='#2c3e50',fg='white')
lableAddress.place(x=10,y=290)
txtAddress=Text(entries_frame,width=30,height=2,font=('Calibri',16))
txtAddress.place(x=10,y=330)

#two buttons hide and show with functions
def hide():
    root.geometry("360x515")
def show():
    root.geometry("1310x515+0+0")

btnhide=Button(entries_frame,text='HIDE',bg='white',bd=1,relief=SOLID,cursor='hand2',command=hide)
btnhide.place(x=270,y=10)

btnshow=Button(entries_frame,text='SHOW',bg='white',bd=1,relief=SOLID,cursor='hand2',command=show)
btnshow.place(x=310,y=10)

def getData(event):
    selected_row=tv.focus()#hyrg3li el bynat bta3t el name lma ados 3leha\
    data=tv.item(selected_row) #tv=treeview
    global row #global variable ast5dmo fe ay mkan fe el program
    row=data["values"]
    name.set(row[1])
    age.set(row[2])
    job.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    mobile.set(row[6])
    txtAddress.delete(1.0,END)#heyaa m4 satr wahed heya satren 3al address
    txtAddress.insert(END,row[7])



def displayAll():#fetchhh
    tv.delete(*tv.get_children())#get_children hy3mli delete w b3den hygebi kol haga gwa el tree view
    for row in db.fetch():
        tv.insert("",END,values=row)



def delete():
    recorded_id = row[0] #function remove in db.py 4el mkan el id eli feh index 0 
    db.remove(recorded_id)
    clear()
    displayAll()



def clear():
    name.set("")
    age.set("")
    job.set("")
    gender.set("")
    email.set("")
    mobile.set("")
    txtAddress.delete(1.0,END)

def add_employee():#inserrt
    if txtName.get() == "" or txtAge.get()=="" or txtJob.get()=="" or txtEmail.get()=="" or comboGender.get() == "" or txtAddress.get(1.0,END)=="":
        messagebox.showerror("Error","Please fill all the entry")
        return
    db.insert(
        txtName.get(),
        txtAge.get(),
        txtJob.get(),
        txtEmail.get(),
        comboGender.get(),
        txtMobile.get(),
        txtAddress.get(1.0,END))
    messagebox.showinfo("Sucess","Adedd new emplyee")
    clear()
    displayAll()

def update():
     if txtName.get() == "" or txtAge.get()=="" or txtJob.get()=="" or txtEmail.get()=="" or comboGender.get() == "" or txtAddress.get(1.0,END)=="":
        messagebox.showerror("Error","Please fill all the entry")
        return
     db.update(row[0],
        txtName.get(),
        txtAge.get(),
        txtJob.get(),
        txtEmail.get(),
        comboGender.get(),
        txtMobile.get(),
        txtAddress.get(1.0,END)
        )
     messagebox.showinfo('sucess','the employ data is update')
     clear()
     displayAll()





#buttons
btn_Frame=Frame(entries_frame,bg='white',bd=1,relief=SOLID)#relif is the shape of board
btn_Frame.place(x=10,y=400,width=335,height=100)
#dlw2ty ha3ml kol button
btnAdd=Button(btn_Frame,
text="add details",
width=14,
height=1,
font=('Calibri',16),
       fg='white',
       bg='#16a085',
       bd=0,
       command=add_employee
       ).place(x=4,y=5)


btnEdit=Button(btn_Frame,
text="update details",
width=14,
height=1,
font=('Calibri',16),
       fg='white',
       bg='#2980b9',
       bd=0,
       command=update
       ).place(x=4,y=50)

btnDelete=Button(btn_Frame,
text="Delete details",
width=14,
height=1,
font=('Calibri',16),
       fg='white',
       bg='#c0392b',
       bd=0,
       command=delete
       ).place(x=170,y=5)

btnClear=Button(btn_Frame,
text="clear details",
width=14,
height=1,
font=('Calibri',16),
       fg='white',
       bg='#f39C12',
       bd=0,
       command=clear
       ).place(x=170,y=50)

#tree frame
tree_frame=Frame(root,bg='white')
tree_frame.place(x=365,y=1,width=940,height=510)
style=ttk.Style()
style.configure("mystyle.Treeview",font=('Calibri',13),rowheight=50)
style.configure("mystyle.Treeview.Heading",font=('Calibri',13))
tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width="40")
tv.heading("2",text="Name")
tv.column("2",width="140")
tv.heading("3",text="Age")
tv.column("3",width="50")
tv.heading("4",text="job")
tv.column("4",width="120")
tv.heading("5",text="Email")
tv.column("5",width="150")
tv.heading("6",text="Gender")
tv.column("6",width="90")
tv.heading("7",text="Contact")
tv.column("7",width="150")
tv.heading("8",text="Address")
tv.column("8",width="190")
tv['show']='headings' #34an mayb2a4 feh msa7a fadya
tv.bind("<ButtonRelease-1>",getData)
tv.place(x=1,y=1,height=610,width=875)
tv.pack()

displayAll()

root.mainloop()
