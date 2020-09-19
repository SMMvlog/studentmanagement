from tkinter import *             #for form  (window)
from tkinter import ttk         #for combobox
import pyodbc
# import sql                 #for sql  pip install pyodbc
import pymysql                   #for mysql
from tkinter import messagebox 
                                            #import pymysql              #pip install pymysql
class Student:
    def __init__(self,window):
        self.window=window
        self.window.title("Student Managment System")
        self.window.geometry("1350x700+0+0")
        
        title=Label(self.window,text="Student Mangment Sytem",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="lightblue",fg="Darkblue")
        title.pack(side=TOP,fill=X)

        #==============All Variables====================

        self.Roll_No_var=StringVar()
        self.Name_var=StringVar()
        self.Email_var=StringVar()
        self.Gender_var=StringVar()
        self.contact_var=StringVar()
        self.DateOfBirth_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()
        
        #=============Student Management Frame=======================

        Management=Frame(self.window,bd=4,relief=RIDGE,bg="lightgreen")
        Management.place(x=20,y=80,width=450,height=600)

        title=Label(Management,text="Manage Student",font=("times new roman",30,"bold"),bg="lightgreen",fg="darkgreen")
        title.grid(row=0,columnspan=2,pady=20,padx=30)

        Roll_No=Label(Management,text="Roll No.",font=("times new roman",20,"bold"),bg="lightgreen",fg="Darkgreen").grid(row=1,column=0,padx=20,pady=10,sticky="w")

        Roll_No=Entry(Management,textvariable=self.Roll_No_var,bd=4,relief=GROOVE,font=("times new roman",15,"bold"))
        Roll_No.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        Name=Label(Management,text="Name:",font=("times new roman",20,"bold"),bg="lightgreen",fg="Darkgreen").grid(row=2,column=0,padx=20,pady=10,sticky="w")

        Name=Entry(Management,bd=4,textvariable=self.Name_var,relief=GROOVE,font=("times new roman",15,"bold"))
        Name.grid(row=2,column=1,pady=10,padx=20,sticky="w")
        
        Email=Label(Management,text="Email:",font=("times new roman",20,"bold"),bg="lightgreen",fg="Darkgreen").grid(row=3,column=0,padx=20,pady=10,sticky="w")
        Email=Entry(Management,textvariable=self.Email_var,bd=4,relief=GROOVE,font=("times new roman",15,"bold")).grid(row=3,column=1,padx=20,pady=10,sticky="w")

        Gender=Label(Management,text="Gender:",font=("times new roman",20,"bold"),bg="lightgreen",fg="Darkgreen").grid(row=4,column=0,padx=20,pady=10,sticky="w")
        Gender=ttk.Combobox(Management,textvariable=self.Gender_var,font=("times new roman",13,"bold"),state='readonly')
        Gender['values']=('Male','Female','Other')
        Gender.grid(row=4,column=1,padx=20,pady=10,sticky="w")

        contact=Label(Management,text="Contact:",font=("times new roman",20,"bold"),bg="lightgreen",fg="Darkgreen").grid(row=5,column=0,padx=20,pady=10,sticky="w")
        contact=Entry(Management,textvariable=self.contact_var,bd=4,relief=GROOVE,font=("times new roman",15,"bold")).grid(row=5,column=1,padx=20,pady=10,sticky="w")

        DateOfBirth=Label(Management,text="D.O.B:",font=("times new roman",20,"bold"),bg="lightgreen",fg="Darkgreen").grid(row=6,column=0,padx=20,pady=10,sticky="w")
        DateOfBirth=Entry(Management,textvariable=self.DateOfBirth_var,bd=4,relief=GROOVE,font=("times new roman",15,"bold")).grid(row=6,column=1,padx=20,pady=10,sticky="w")

        address=Label(Management,text="Address:",font=("times new roman",20,"bold"),bg="lightgreen",fg="Darkgreen").grid(row=7,column=0,padx=20,pady=10,sticky="w")
        self.address=Text(Management,width=30,height=4,font=("",10))
        self.address.grid(row=7,column=1,padx=20,pady=10,sticky="w")
         
        #================Button Frame===========================

        button=Frame(Management,bd=4,relief=RIDGE,bg="lightgreen")
        button.place(width=430,y=520,x=10)

        add=Button(button,text="Add",width=10,command=self.add_student).grid(row=0,column=0,padx=10,pady=10)
        update=Button(button,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        delete=Button(button,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clear=Button(button,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

        #=================Detail Frame============================

        detail_frame=Frame(self.window,bd=4,relief=RIDGE,bg="lightgreen")
        detail_frame.place(x=500,y=80,width=800,height=600)

        search=Label(detail_frame,text="Search By:",font=("times new roman",20,"bold"),bg="lightgreen",fg="Darkgreen").grid(row=0,column=0,padx=20,pady=10,sticky="w")
        search=ttk.Combobox(detail_frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
        search['values']=("RollNo","Name","contact")
        search.grid(row=0,column=1,padx=10,pady=10,sticky="w")

        search1=Entry(detail_frame,textvariable=self.search_txt,bd=4,relief=GROOVE,font=("times new roman",15,"bold"))
        search1.grid(row=0,column=10,padx=10,pady=10,sticky="w")
        
        search_btn=Button(detail_frame,text="Search",width=10,command=self.search_data).grid(row=0,column=2,padx=10,pady=10)
        showall_btn=Button(detail_frame,text="Show All",width=10,command=self.fetch_data).grid(row=0,column=3,padx=10,pady=10,sticky="w")

        #===============Table Frame========================

        Table=Frame(detail_frame,bd=4,relief=RIDGE,bg="lightgreen")
        Table.place(x=10,y=60,width=780,height=520)

        scroll_x=Scrollbar(Table,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table,orient=VERTICAL)
        self.student_table=ttk.Treeview(Table,columns=("Roll No.","Name","Email","Gender","Contact","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("Roll No.",text="Roll No.")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Contact",text="Contact")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Address",text="Address")
        self.student_table['show']='headings'
        self.student_table.column("Roll No.",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Contact",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Address",width=150)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        self.fetch_data()
    def add_student(self):
        if self.Roll_No_var.get()=="" or self.Name_var.get()=="" or self.Email_var.get()=="" or self.Gender_var.get()=="" or self.contact_var.get()=="" or self.DateOfBirth_var.get()=="" or self.address.get('1.0',END)=="":
            messagebox.showerror("Error","All fields are required!!!")
                 
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="student_management")
            cur=con.cursor()
            cur.execute("insert into management values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                         self.Name_var.get(),
                                                                         self.Email_var.get(),
                                                                         self.Gender_var.get(),
                                                                         self.contact_var.get(),
                                                                         self.DateOfBirth_var.get(),
                                                                         self.address.get('1.0',END)
                                                                        ))

             
             
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()   
            messagebox.showinfo("Success","Record has been Inserted")


    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="student_management")
        cur=con.cursor()
        cur.execute("Select * From management")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.Name_var.set("")
        self.Email_var.set("")
        self.Gender_var.set("")
        self.contact_var.set("")
        self.DateOfBirth_var.set("")
        self.address.delete("1.0",END)

    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents['values']
        self.Roll_No_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.DateOfBirth_var.set(row[5])
        self.address.delete("1.0",END)
        self.address.insert(END,row[6])

    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="student_management")
        cur=con.cursor()
        cur.execute("update management set Name=%s,Email=%s,Gender=%s,contact=%s,DOB=%s,address=%s where RollNo=%s",(
                                                                           self.Name_var.get(),
                                                                           self.Email_var.get(),
                                                                           self.Gender_var.get(),
                                                                           self.contact_var.get(),
                                                                           self.DateOfBirth_var.get(),
                                                                           self.address.get('1.0',END),
                                                                           self.Roll_No_var.get()
                                                                          ))

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="student_management")
        cur=con.cursor()
        cur.execute("delete from management where Roll_No=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="student_management")
        cur=con.cursor()

        cur.execute("select * from management where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert('',END,values=row)
                con.commit()
        con.close()
                    

window=Tk()
obj=Student(window)
window.mainloop()