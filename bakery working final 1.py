import tkinter as tk 
import mysql.connector as mys
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess
import io

#result = subprocess.run(["python3", "tkinterproj(3).py"], capture_output=True, text=True)
'''
#------------------DATABASE CREATION-------------------------
def createdatabase():
    try:
        conn=mys.connect(host='localhost',user='root',password='icecream123')
        cur=conn.cursor()
        query="create database bakery "
        cur.execute(query)
        conn.commit()
        print("Database successfully created")
    except Exception as e:
        print(e)



#------------------TABLE CREATIONS---------------------------
#product table creation
def createtableproduct():
    try:
        conn=mys.connect(host='localhost',user='root',password='icecream123',database="bakery")
        cur=conn.cursor()
        query="create table product (pcode int primary key, pname varchar (30) not null, category varchar(30),price float, qty_weight float, descp varchar(250))"
        cur.execute(query)
        conn.commit()
        print("Table successfully created")
    except Exception as e:
        print(e)

#employee table creation
def createtableemployee():
    try:
        conn=mys.connect(host='localhost',user='root',password='icecream123',database="bakery")
        cur=conn.cursor()
        query="create table employee (empno int primary key, ename char (20) not null, sal float, job char (20) , doj date)"
        cur.execute(query)
        conn.commit()
        print("Table successfully created")
    except Exception as e:
        print(e)
        
#orders table creation
def createtableorders():
    try:
        conn=mys.connect(host='localhost',user='root',password='icecream123',database="bakery")
        cur=conn.cursor()
        query="create table orders (orderno int primary key, details varchar(50) not null, billamt float, delvdate date,cid int)"
        cur.execute(query)
        conn.commit()
        print("Table successfully created")
    except Exception as e:
        print(e)
        
#customer table creation
def createtablecustomer():
    try:
        conn=mys.connect(host='localhost',user='root',password='icecream123',database="bakery")
        cur=conn.cursor()
        query="create table customer(cid int primary key,cnam varchar(30),cphno varchar(10),cadrs varchar(50), bookeditems varchar(40))"
        cur.execute(query)
        conn.commit()
        print("Table successfully created")
    except Exception as e:
        print(e)
    
    
#users table creation
def createtableusers():
    try:
        conn=mys.connect(host='localhost',user='root',password='icecream123',database="bakery")
        cur=conn.cursor()
        query="create table customer(fname varchar(45), lname varchar(45), contact varchar(45), contact varchar(45), email varchar(45) primary key, securityQ varchar(45), securityA varchar(45), password varchar(45) "
        cur.execute(query)
        conn.commit()
        print("Table successfully created")
    except Exception as e:
        print(e)

#img table creation
def imgtable():
    try:
        conn=mys.connect(host='localhost',user='root',password='icecream123',database="bakery")
        cur=conn.cursor()
        query="create table img(pno int(3), img longblob, foreign key (pcode) references product(pcode)"
        cur.execute(query)
        conn.commit()
        print("Table successfully created")
    except Exception as e:
        print(e)

imgtable()
'''

#------------------------INSERT A PRODUCT--------------------------------
    
def insertrec():
    
    
#     photo = tk.PhotoImage(file = 'newproductbg.png') 
#     Button(image = photo) # Line required to prevent python's garbage dump function
#     Button(root, image = photo, fg = 'black', bg = 'black').place(x = 0, y = 0)
#     
    
    newprdt = tk.PhotoImage(file="newproductbg.png")
    img_label = Label(image = newprdt)
    img_label.place(x=0,y=0)
    img_label.image = newprdt
# 
    
    frame=Frame(bg="gray21")
    frame.place(x=75,y=170, width=700, height=600)
    
    
    def Clear():
        txtpno.delete(0,END)
        txtpname.delete(0,END)
        txtpcat.delete(0,END)
        txtprice.delete(0,END)
        txt.qw.delete(0,END)
        txtdesp.delete(0,END)
        txtimg.delete(0,END)
            
        
    def Insert():
        pno = txtpno.get() 
        pname = txtpname.get()
        pcat=txtpcat.get()
        price=txtprice.get()
        qw=txtqw.get()
        desc=txtdesp.get()
        img=txtimg.get()
        
        
        try:
            myconn=mys.connect(host='localhost',user="root",passwd="icecream123",database="bakery")
            if pno=="" or pname=="" or pcat=="" or price=="" or qw=="" or desc=="" or img=="":
                messagebox.showerror("Error","All fields are required!")
            else:
                mycur=myconn.cursor()
                with open(img,'rb') as file:
                    filedata=file.read()
                query1="insert into product values ({},'{}','{}',{},{},'{}','{}')".format(pno,pname,pcat,price,qw,desc,img)
                mycur.execute(query1)
                myconn.commit() 
                messagebox.showinfo("SUCESS","Product successfully added!")
                insertrec()
                
        except Exception as e:
            print(e)
         
    
    lblpno = tk.Label(frame, text ="Product Code",bg='gray21',font = ("Times New Roman Bold", 25),fg='white' ) 
    lblpno.place(x = 40, y = 30) 
    txtpno= tk.Entry(frame, width = 35,bg='gray21',font = ("Times New Roman Bold", 30),fg='white') 
    txtpno.place(x = 240, y = 30, width = 300) 
    lblpname = tk.Label(frame, text ="Product Name",bg='gray21',font = ("Times New Roman Bold", 25),fg='white') 
    lblpname.place(x = 40, y = 105) 
    txtpname = tk.Entry(frame, width = 35,bg='gray21',font = ("Times New Roman Bold", 30),fg='white') 
    txtpname.place(x = 240, y = 105, width = 300) 
    lblpcat = tk.Label(frame, text ="Category",bg='gray21',font = ("Times New Roman Bold", 25) ,fg='white') 
    lblpcat.place(x = 40, y = 180) 
    txtpcat= tk.Entry(frame, width = 35,bg='gray21',font = ("Times New Roman Bold", 25),fg='white') 
    txtpcat.place(x = 240, y =180, width = 300) 
    lblprice = tk.Label(frame, text ="Price",bg='gray21',font = ("Times New Roman Bold", 25),fg='white') 
    lblprice.place(x = 40, y = 255)
    txtprice = tk.Entry(frame, width = 35,bg='gray21',font = ("Times New Roman Bold", 25),fg='white') 
    txtprice.place(x = 240, y = 255, width = 300)
    lblqw = tk.Label(frame, text ="Quantity/Weight",bg='gray21',font = ("Times New Roman Bold", 25),fg='white' ) 
    lblqw.place(x = 40, y = 330) 
    txtqw= tk.Entry(frame, width = 35,bg='gray21',font = ("Times New Roman Bold", 30),fg='white') 
    txtqw.place(x = 240, y = 330, width = 300)
    lbldesp = tk.Label(frame, text ="Description",bg='gray21',font = ("Times New Roman Bold", 25),fg='white' ) 
    lbldesp.place(x = 40, y = 405) 
    txtdesp= tk.Entry(frame, width = 35,bg='gray21',font = ("Times New Roman Bold", 30),fg='white') 
    txtdesp.place(x = 240, y = 405, width = 300)
    lblimg = tk.Label(frame, text ="Image",bg='gray21',font = ("Times New Roman Bold", 25),fg='white' ) 
    lblimg.place(x = 40, y = 480) 
    txtimg= tk.Entry(frame, width = 35,bg='gray21',font = ("Times New Roman Bold", 30),fg='white') 
    txtimg.place(x = 240, y = 480, width = 300)
    
    btninsert = tk.Button(frame, text ="INSERT", bg='pink',font = ("Times New Roman Bold", 25),command=Insert) 
    btninsert.place(x = 280, y = 555, width = 110)
    btnclear = tk.Button(frame, text ="CLEAR", bg='pink',font = ("Times New Roman Bold", 25),command=Clear) 
    btnclear.place(x = 420, y = 555, width = 110)
    btnmain = tk.Button(frame, text ="MAIN MENU", bg='pink',font = ("Times New Roman Bold", 25),command=mainadmin) 
    btnmain.place(x = 0, y = 555, width = 250)

#--------------------------------UPDATE PRODUCT-----------------------------

def updaterec():
    updatepdt = tk.PhotoImage(file="updateimg.png")
    img_label = Label(image = updatepdt)
    img_label.grid(row=4, column=0)
    img_label.image = updatepdt
    
    
    frame=Frame(bg="tan")
    frame.place(x=780,y=255, width=670, height=560)
    
    
    
    def Clear():
        txtpno.delete(0,END)
        txtpname.delete(0,END)
        txtpcat.delete(0,END)
        txtprice.delete(0,END)
        txtqw.delete(0,END)
        txtdesp.delete(0,END)
        txtimg.delete(0,END)
        
    def Update():
        pno = txtpno.get() 
        pname = txtpname.get()
        pcat=txtpcat.get()
        price=txtprice.get()
        qw=txtqw.get()
        desc=txtdesp.get()
        img=txtimg.get()
        
        myconn=mys.connect(host='localhost',user="root",passwd="icecream123",database="bakery")
        if myconn.is_connected():
            print("connection successful")
        mycur=myconn.cursor()
        query="update product set pname='{}',category='{}',price={},qty_weight={},descp='{}',imgpath='{}' where pcode={}".format(pname,pcat,price,qw,desc,img,pno)
        mycur.execute(query)
        myconn.commit()
#         query2="update img set pcode='{}',img='{}'({},'{}')".format(pno,img)
#         mycur.execute(query2)
#         myconn.commit()
        messagebox.showinfo("PRODUCT ALERT"," PRODUCT RECORD UPDATED SUCCESSFULLY!")
        updaterec()
        
        
    def Search():
        try:
            myconn=mys.connect(host='localhost',user="root",passwd="icecream123",database="bakery")
            if myconn.is_connected():
                print("connection succssful")
            mycur=myconn.cursor()
            pno=txtpno.get()
            query1="select * from product where pcode={}".format(pno)
            mycur.execute(query1)
            rs1=mycur.fetchone()
            rs1=list(rs1)
            
#             query2="select * from img where pcode={}".format(pno)
#             mycur.execute(query2)
#             rs2=mycur.fetchone()
#             rs2=list(rs2)
            
            pcode = rs1[0] 
            pname = rs1[1]
            category=rs1[2]
            price= rs1[3]
            qty_weight= rs1[4]
            descp= rs1[5]
            img=rs1[6]
            
            if rs1==None:
                messagebox.showinfo("PRODUCT INFO","No such product found!")
            else:
                messagebox.showinfo("PRODUCT INFO"," Product found! ")
                txtpname.insert(END,pname)
                txtpcat.insert(END,category)
                txtprice.insert(END,price)
                txtqw.insert(END,qty_weight)
                txtdesp.insert(END,descp)
                txtimg.insert(END,img)
        except Exception as e:
            print(e)
             
    lblpno = tk.Label(frame, text ="Product Code",bg='tan',font = ("Times New Roman Bold", 25),fg='white' ) 
    lblpno.place(x = 40, y = 10) 
    txtpno= tk.Entry(frame, width = 35,bg='tan',font = ("Times New Roman Bold", 30),fg='white') 
    txtpno.place(x = 240, y = 10, width = 300) 
    lblpname = tk.Label(frame, text ="Product Name",bg='tan',font = ("Times New Roman Bold", 25),fg='white') 
    lblpname.place(x = 40, y = 80) 
    txtpname = tk.Entry(frame, width = 35,bg='tan',font = ("Times New Roman Bold", 30),fg='white') 
    txtpname.place(x = 240, y = 80, width = 300) 
    lblpcat = tk.Label(frame, text ="Category",bg='tan',font = ("Times New Roman Bold", 25) ,fg='white') 
    lblpcat.place(x = 40, y = 150) 
    txtpcat= tk.Entry(frame, width = 35,bg='tan',font = ("Times New Roman Bold", 25),fg='white') 
    txtpcat.place(x = 240, y =150, width = 300) 
    lblprice = tk.Label(frame, text ="Price",bg='tan',font = ("Times New Roman Bold", 25),fg='white') 
    lblprice.place(x = 40, y = 220)
    txtprice = tk.Entry(frame, width = 35,bg='tan',font = ("Times New Roman Bold", 25),fg='white') 
    txtprice.place(x = 240, y = 220, width = 300)
    lblqw = tk.Label(frame, text ="Quantity/Weight",bg='tan',font = ("Times New Roman Bold", 25),fg='white' ) 
    lblqw.place(x = 40, y = 290) 
    txtqw= tk.Entry(frame, width = 35,bg='tan',font = ("Times New Roman Bold", 30),fg='white') 
    txtqw.place(x = 240, y = 290, width = 300)
    lbldesp = tk.Label(frame, text ="Description",bg='tan',font = ("Times New Roman Bold", 25),fg='white' ) 
    lbldesp.place(x = 40, y = 360) 
    txtdesp= tk.Entry(frame, width = 35,bg='tan',font = ("Times New Roman Bold", 30),fg='white') 
    txtdesp.place(x = 240, y = 360, width = 300)
    lblimg = tk.Label(frame, text ="Image",bg='tan',font = ("Times New Roman Bold", 25),fg='white' ) 
    lblimg.place(x = 40, y = 430) 
    txtimg= tk.Entry(frame, width = 35,bg='tan',font = ("Times New Roman Bold", 30),fg='white') 
    txtimg.place(x = 240, y = 430, width = 300)

    
    btnupdate = tk.Button(frame, text ="UPDATE",bg='tan',font = ("Times New Roman Bold", 25),command=Update) 
    btnupdate.place(x = 270, y = 500, width = 120)
    btnsearch = tk.Button(frame, text ="SEARCH", bg='tan',font = ("Times New Roman Bold", 25),command=Search) 
    btnsearch.place(x = 410, y = 500, width = 120)
    btnclear = tk.Button(frame, text ="CLEAR", bg='tan',font = ("Times New Roman Bold", 25),command=Clear) 
    btnclear.place(x = 550, y = 500, width = 120)
    btnmain = tk.Button(frame, text ="MAIN MENU", bg='pink',font = ("Times New Roman Bold", 25),command=mainadmin) 
    btnmain.place(x = 2, y = 500, width = 240)
    
    
def deleterec():
    newprdt = tk.PhotoImage(file="deleteprdt.png")
    img_label = Label(image = newprdt)
    img_label.place(x=0,y=0)
    img_label.image = newprdt
# 
    
    frame=Frame(bg="rosybrown3")
    frame.place(x=740,y=175, width=700, height=600)
    
    
    
    def Clear():
        ttxtpno.delete(0,END)
        txtpname.delete(0,END)
        txtpcat.delete(0,END)
        txtprice.delete(0,END)
        txt.qw.delete(0,END)
        txtdesp.delete(0,END)
        txtimg.delete(0,END)
        
    def Delete():
        pno = txtpno.get() 
        myconn=mys.connect(host='localhost',user="root",passwd="icecream123",database="bakery")
        if myconn.is_connected():
            print("connection successful")
        mycur=myconn.cursor()
        query1="delete from product where pcode={}".format(pno)
#         query2="delete from img where pcode={}".format(pno)
        mycur.execute(query1)
        mycur.execute(query2)
#         myconn.commit()
        messagebox.showinfo("PRODUCT INFO"," PRODUCT DELETED SUCCESSFULLY")
        deleterec()
        
        
    def Search():
        try:
            myconn=mys.connect(host='localhost',user="root",passwd="icecream123",database="bakery")
            if myconn.is_connected():
                print("connection succssful")
            mycur=myconn.cursor()
            pno=txtpno.get()
            query1="select * from product where pcode={}".format(pno)
            mycur.execute(query1)
            rs1=mycur.fetchone()
            rs1=list(rs1)
            
#             query2="select * from img where pcode={}".format(pno)
#             mycur.execute(query2)
#             rs2=mycur.fetchone()
#             rs2=list(rs2)
            
            pcode = rs1[0] 
            pname = rs1[1]
            category=rs1[2]
            price= rs1[3]
            qty_weight= rs1[4]
            descp= rs1[5]
            img=rs1[6]
#             img=rs2[0]
            
            if rs==None:
                messagebox.showinfo("PRODUCT INFO","No such product found!")
            else:
                messagebox.showinfo("PRODUCT INFO"," Product found! ")
                txtpname.insert(END,pname)
                txtpcat.insert(END,category)
                txtprice.insert(END,price)
                txtqw.insert(END,qty_weight)
                txtdesp.insert(END,descp)
                txtimg.insert(END,img)
        except Exception as e:
            print(e)
            
    lblpno = tk.Label(frame, text ="Product Code",bg='rosybrown3',font = ("Times New Roman Bold", 25),fg='white' ) 
    lblpno.place(x = 40, y = 30) 
    txtpno= tk.Entry(frame, width = 35,bg='rosybrown3',font = ("Times New Roman Bold", 30),fg='white') 
    txtpno.place(x = 240, y = 30, width = 300) 
    lblpname = tk.Label(frame, text ="Product Name",bg='rosybrown3',font = ("Times New Roman Bold", 25),fg='white') 
    lblpname.place(x = 40, y = 105) 
    txtpname = tk.Entry(frame, width = 35,bg='rosybrown3',font = ("Times New Roman Bold", 30),fg='white') 
    txtpname.place(x = 240, y = 105, width = 300) 
    lblpcat = tk.Label(frame, text ="Category",bg='rosybrown3',font = ("Times New Roman Bold", 25) ,fg='white') 
    lblpcat.place(x = 40, y = 180) 
    txtpcat= tk.Entry(frame, width = 35,bg='rosybrown3',font = ("Times New Roman Bold", 25),fg='white') 
    txtpcat.place(x = 240, y =180, width = 300) 
    lblprice = tk.Label(frame, text ="Price",bg='rosybrown3',font = ("Times New Roman Bold", 25),fg='white') 
    lblprice.place(x = 40, y = 255)
    txtprice = tk.Entry(frame, width = 35,bg='rosybrown3',font = ("Times New Roman Bold", 25),fg='white') 
    txtprice.place(x = 240, y = 255, width = 300)
    lblqw = tk.Label(frame, text ="Quantity/Weight",bg='rosybrown3',font = ("Times New Roman Bold", 25),fg='white' ) 
    lblqw.place(x = 40, y = 330) 
    txtqw= tk.Entry(frame, width = 35,bg='rosybrown3',font = ("Times New Roman Bold", 30),fg='white') 
    txtqw.place(x = 240, y = 330, width = 300)
    lbldesp = tk.Label(frame, text ="Description",bg='rosybrown3',font = ("Times New Roman Bold", 25),fg='white' ) 
    lbldesp.place(x = 40, y = 405) 
    txtdesp= tk.Entry(frame, width = 35,bg='rosybrown3',font = ("Times New Roman Bold", 30),fg='white') 
    txtdesp.place(x = 240, y = 405, width = 300)
    lblimg = tk.Label(frame, text ="Image",bg='gray21',font = ("Times New Roman Bold", 25),fg='white' ) 
    lblimg.place(x = 40, y = 480) 
    txtimg= tk.Entry(frame, width = 35,bg='gray21',font = ("Times New Roman Bold", 30),fg='white') 
    txtimg.place(x = 240, y = 480, width = 300)
     
    btnupdate = tk.Button(frame, text ="DELETE",bg='tan',font = ("Times New Roman Bold", 25),command=Delete) 
    btnupdate.place(x = 280, y = 555, width = 120)
    btnsearch = tk.Button(frame, text ="SEARCH", bg='tan',font = ("Times New Roman Bold", 25),command=Search) 
    btnsearch.place(x = 420, y = 555, width = 120)
    btnclear = tk.Button(frame, text ="CLEAR", bg='tan',font = ("Times New Roman Bold", 25),command=Clear) 
    btnclear.place(x = 560, y = 555, width = 120)
    btnmain = tk.Button(frame, text ="MAIN MENU", bg='pink',font = ("Times New Roman Bold", 25),command=mainadmin) 
    btnmain.place(x = 10, y = 555, width = 240)
    


#-------------------------------------ALLL DISPLAY FUNCTIONS----------------------------------------------------

def displaymenu():
    displaymenu = tk.PhotoImage(file="displaymenu.png")
    img_label = Label(image = displaymenu)
    img_label.grid(row=4, column=0)
    img_label.image = displaymenu
    
    frame1=Frame(bg="rosybrown3")
    frame1.place(x=70,y=280, width=300, height=100)

    frame2=Frame(bg="rosybrown3")
    frame2.place(x=450,y=280, width=300, height=100)

    frame3=Frame(bg="rosybrown3")
    frame3.place(x=70,y=430, width=300, height=100)

    frame4=Frame(bg="rosybrown3")
    frame4.place(x=450,y=430, width=300, height=100)
    
    frame5=Frame(bg="rosybrown3")
    frame5.place(x=70,y=580, width=300, height=100)

    frame6=Frame(bg="rosybrown3")
    frame6.place(x=450,y=580, width=300, height=100)
    
    frame7=Frame(bg="rosybrown3")
    frame7.place(x=260,y=700, width=300, height=100)

    


    btn_displayall = tk.Button(frame1, text ="DISPLAY ALL",bg='tan',font = ("Times New Roman Bold", 25),command=displayrecs) 
    btn_displayall.place(x = 40, y = 30, width = 240)
    btn_displaycakes = tk.Button(frame2, text ="DISPLAY CAKES", bg='tan',font = ("Times New Roman Bold", 25),command=displaycakes) 
    btn_displaycakes.place(x = 40, y = 30, width = 240)
    btn_displaycupcakes = tk.Button(frame3, text ="DISPLAY CUPCAKES", bg='tan',font = ("Times New Roman Bold", 25),command=displaycupcakes) 
    btn_displaycupcakes.place(x = 35, y = 30, width = 250)
    btn_displaycookies = tk.Button(frame4, text ="DISPLAY COOKIES", bg='tan',font = ("Times New Roman Bold", 25),command=displaycookies) 
    btn_displaycookies.place(x = 40, y = 30, width = 240)
    btn_brownies = tk.Button(frame5, text ="DISPLAY BROWNIES", bg='tan',font = ("Times New Roman Bold", 25),command=displaybrownies) 
    btn_brownies.place(x = 30, y = 30, width = 260)
    btn_other = tk.Button(frame6, text ="OTHER DESSERTS", bg='tan',font = ("Times New Roman Bold", 25),command=displayother) 
    btn_other.place(x = 20, y = 30, width = 270)
    btnmain = tk.Button(frame7, text ="MAIN MENU", bg='pink',font = ("Times New Roman Bold", 25),command=mainadmin) 
    btnmain.place(x = 40, y = 30, width = 240)
    




def displaycakes():
    try:
        myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
        if myconn.is_connected():
            print("connection successful")
        mycur = myconn.cursor()
        query = "select * from product where category='Cakes'"
        mycur.execute(query)
        rs = mycur.fetchall()
        root = tk.Tk() 
        root.geometry("1550x800")
        root.title("Product Details")
        root['background'] = 'RosyBrown1'
        ttk.Label(root, text ="Product Details",font = ("Times New Roman Bold", 20)).pack()
        frame = Frame(root)
        frame.pack()
        tree = ttk.Treeview(frame, columns = (1,2,3,4,5), height = 500, show = "headings")
        tree.pack(side = 'right')
        tree.heading(1, text = "Product Code")
        tree.heading(2, text = " Product Name")
        tree.heading(3, text = "Category")
        tree.heading(4, text = "Price")
        tree.heading(5, text = "Quantity(number)/Weight(in kg)")
        tree.column(1, width = 100)
        tree.column(2, width = 250)
        tree.column(3, width = 130)
        tree.column(4, width = 130)
        tree.column(5, width = 150)
        scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scroll.pack(side = 'right', fill = 'y')

        for val in rs:
            tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4]))
                                             
  
    except Exception as e:
            print(e)
def displaycupcakes():
    try:
        myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
        if myconn.is_connected():
            print("connection successful")
        mycur = myconn.cursor()
        query = "select * from product where category='Cupcakes'"
        mycur.execute(query)
        rs = mycur.fetchall()
        root = tk.Tk() 
        root.geometry("1550x800")
        root.title("Product Details")
        root['background'] = 'RosyBrown1'
        ttk.Label(root, text ="Product Details",font = ("Times New Roman Bold", 20)).pack()
        frame = Frame(root)
        frame.pack()
        tree = ttk.Treeview(frame, columns = (1,2,3,4,5), height = 500, show = "headings")
        tree.pack(side = 'right')
        tree.heading(1, text = "Product Code")
        tree.heading(2, text = " Product Name")
        tree.heading(3, text = "Category")
        tree.heading(4, text = "Price")
        tree.heading(5, text = "Quantity(number)/Weight(in kg)")
        tree.column(1, width = 100)
        tree.column(2, width = 250)
        tree.column(3, width = 130)
        tree.column(4, width = 130)
        tree.column(5, width = 150)
        scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scroll.pack(side = 'right', fill = 'y')

        for val in rs:
            tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4]))
                                             
  
    except Exception as e:
            print(e)


def displaycookies():
    try:
        myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
        if myconn.is_connected():
            print("connection successful")
        mycur = myconn.cursor()
        query = "select * from product where category='Cookies'"
        mycur.execute(query)
        rs = mycur.fetchall()
        root = tk.Tk() 
        root.geometry("1550x800")
        root.title("Product Details")
        root['background'] = 'RosyBrown1'
        ttk.Label(root, text ="Product Details",font = ("Times New Roman Bold", 20)).pack()
        frame = Frame(root)
        frame.pack()
        tree = ttk.Treeview(frame, columns = (1,2,3,4,5), height = 500, show = "headings")
        tree.pack(side = 'right')
        tree.heading(1, text = "Product Code")
        tree.heading(2, text = " Product Name")
        tree.heading(3, text = "Category")
        tree.heading(4, text = "Price")
        tree.heading(5, text = "Quantity(number)/Weight(in kg)")
        tree.column(1, width = 100)
        tree.column(2, width = 250)
        tree.column(3, width = 130)
        tree.column(4, width = 130)
        tree.column(5, width = 150)
        scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scroll.pack(side = 'right', fill = 'y')

        for val in rs:
            tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4]))
                                             
  
    except Exception as e:
            print(e)


def displaybrownies():
    try:
        myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
        if myconn.is_connected():
            print("connection successful")
        mycur = myconn.cursor()
        query = "select * from product where category='Brownies'"
        mycur.execute(query)
        rs = mycur.fetchall()
        root = tk.Tk() 
        root.geometry("1550x800")
        root.title("Product Details")
        root['background'] = 'RosyBrown1'
        ttk.Label(root, text ="Product Details",font = ("Times New Roman Bold", 20)).pack()
        frame = Frame(root)
        frame.pack()
        tree = ttk.Treeview(frame, columns = (1,2,3,4,5), height = 500, show = "headings")
        tree.pack(side = 'right')
        tree.heading(1, text = "Product Code")
        tree.heading(2, text = " Product Name")
        tree.heading(3, text = "Category")
        tree.heading(4, text = "Price")
        tree.heading(5, text = "Quantity(number)/Weight(in kg)")
        tree.column(1, width = 100)
        tree.column(2, width = 250)
        tree.column(3, width = 130)
        tree.column(4, width = 130)
        tree.column(5, width = 150)
        scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scroll.pack(side = 'right', fill = 'y')

        for val in rs:
            tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4]))
                                             
  
    except Exception as e:
            print(e)


def displayother():
    try:
        myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
        if myconn.is_connected():
            print("connection successful")
        mycur = myconn.cursor()
        query = "select * from product where category='Other Desserts'"
        mycur.execute(query)
        rs = mycur.fetchall()
        root = tk.Tk() 
        root.geometry("1550x800")
        root.title("Product Details")
        root['background'] = 'RosyBrown1'
        ttk.Label(root, text ="Product Details",font = ("Times New Roman Bold", 20)).pack()
        frame = Frame(root)
        frame.pack()
        tree = ttk.Treeview(frame, columns = (1,2,3,4,5), height = 500, show = "headings")
        tree.pack(side = 'right')
        tree.heading(1, text = "Product Code")
        tree.heading(2, text = " Product Name")
        tree.heading(3, text = "Category")
        tree.heading(4, text = "Price")
        tree.heading(5, text = "Quantity(number)/Weight(in kg)")
        tree.column(1, width = 100)
        tree.column(2, width = 250)
        tree.column(3, width = 130)
        tree.column(4, width = 130)
        tree.column(5, width = 150)
        scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scroll.pack(side = 'right', fill = 'y')

        for val in rs:
            tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4]))
                                             
  
    except Exception as e:
            print(e)

def displayrecs():
    try:
        myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
        if myconn.is_connected():
            print("connection successful")
        mycur = myconn.cursor()
        query = "select * from product "
        mycur.execute(query)
        rs = mycur.fetchall()
        root = tk.Tk() 
        root.geometry("1550x800")
        root.title("Product Details")
        root['background'] = 'RosyBrown1'
        ttk.Label(root, text ="Product Details",font = ("Times New Roman Bold", 20)).pack()
        frame = Frame(root)
        frame.pack()
        tree = ttk.Treeview(frame, columns = (1,2,3,4,5), height = 500, show = "headings")
        tree.pack(side = 'right')
        tree.heading(1, text = "Product Code")
        tree.heading(2, text = " Product Name")
        tree.heading(3, text = "Category")
        tree.heading(4, text = "Price")
        tree.heading(5, text = "Quantity(number)/Weight(in kg)")
        tree.column(1, width = 100)
        tree.column(2, width = 250)
        tree.column(3, width = 130)
        tree.column(4, width = 130)
        tree.column(5, width = 150)
        scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scroll.pack(side = 'right', fill = 'y')

        for val in rs:
            tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4]))
                                             
  
    except Exception as e:
            print(e)


#--------------------------------------ADMIN MAIN PAGE------------------------------- 
def mainadmin():
    mainadimg = tk.PhotoImage(file="adminpagefunc.png")
    img_label = Label(image = mainadimg)
    img_label.grid(row=4, column=0)
    img_label.image = mainadimg
    
    insertbtn=Button(command=insertrec,text="Insert",font=("Times New Roman",40,"bold"),bd=3,relief=RIDGE,background="black",fg="burlywood4",activeforeground="black", activebackground="black")
    insertbtn.place(x=1050,y=150,width=200,height=50)

    updatebtn=Button(command=updaterec,text="Update",font=("Times New Roman",40,"bold"),bd=3,relief=RIDGE,background="black",fg="burlywood4",activeforeground="black", activebackground="black")
    updatebtn.place(x=1050,y=275,width=200,height=50)
    
    deletebtn=Button(command=deleterec,text="Delete",font=("Times New Roman",40,"bold"),bd=3,relief=RIDGE,background="black",fg="burlywood4",activeforeground="black", activebackground="black")
    deletebtn.place(x=1050,y=400,width=200,height=50)
    
    displaybtn=Button(command=displaymenu,text="Display",font=("Times New Roman",40,"bold"),bd=3,relief=RIDGE,background="black",fg="burlywood4",activeforeground="black", activebackground="black")
    displaybtn.place(x=1050,y=525,width=200,height=50)
    

#----------------------ADMIN LOGIN--------------------------------
def adlog():
    def adlogin():
        if txtuser.get()=="" or txtpass.get()=="":
            messagebox.showerror("Error","All fields are required!")
        elif txtuser.get()=="admindiya" and txtpass.get()=="ourbakeshop27":
            mainadmin()
        elif txtuser.get()=="admins" and txtpass.get()=="ourbakeshop27":
            mainadmin()
        else:
            messagebox.showerror("Invalid","Invalid username or password")  

    image3 = tk.PhotoImage(file="adlog.png")
    img_label = Label(image = image3)
    img_label.grid(row=4, column=0)
    img_label.image = image3
    frame=Frame(bg="tan")
    frame.place(x=620,y=190, width=360, height=470)
    
    get_str=Label(text="Get Started",font=("Times New Roman",20,"bold"),fg="black",bg='tan')
    get_str.place(x=720,y=300)
    
    
    image2 = tk.PhotoImage(file="loginaccimg.png")
    img_label = Label(image = image2)
    img_label.place(x=730,y=185,width=100,height=100)
    img_label.image = image2
    
    #usernmaelabel and entry field
    username=lbl=Label(frame,text="Username:",font=("Times New Roman",15,"bold"),fg="black",bg="tan")
    username.place(x=70,y=155)

    txtuser=ttk.Entry(frame,font=("Times New Roman",15,"bold"))
    txtuser.place(x=40,y=180,width=270)
    
    #password and entry field
    password=lbl=Label(frame,text="Password:",font=("Times New Roman",15,"bold"),fg="black",bg="tan")
    password.place(x=70,y=225)
    
    txtpass=ttk.Entry(frame,font=("Times New Roman",15,"bold"))
    txtpass.place(x=40,y=250,width=270)
   
    
    
    #LOGIN BUTTON
    loginbtn=Button(frame,command=adlogin,text="Login",font=("Times New Roman",15,"bold"),bd=3,relief=RIDGE,background="red",fg="black",activeforeground="blue", activebackground="tan")
    loginbtn.place(x=110,y=300,width=120,height=35)
#     
#     #REGISTER BUTTON
#     registerbtn=Button(frame,text="New User Register",font=("Times New Roman",15,"bold"),borderwidth=0,bg="indianred",fg="black",activeforeground="blue", activebackground="tan")
#     registerbtn.place(x=15,y=350,width=160,height=35)



#------------------------------------------------------USER FUNCTIONS-------------------------------------------------

#-------------------------------------------------------SEARCHES ------------------------------------------------------
def searchmenu():
    displaymenu = tk.PhotoImage(file="searchesmenu.png")
    img_label = Label(image = displaymenu)
    img_label.grid(row=4, column=0)
    img_label.image = displaymenu
    
    frame1=Frame(bg="gray21")
    frame1.place(x=70,y=280, width=300, height=100)

    frame2=Frame(bg="gray21")
    frame2.place(x=450,y=280, width=300, height=100)

    frame3=Frame(bg="gray21")
    frame3.place(x=70,y=430, width=300, height=100)

    frame4=Frame(bg="gray21")
    frame4.place(x=450,y=430, width=300, height=100)
    
    frame5=Frame(bg="gray21")
    frame5.place(x=70,y=580, width=300, height=100)

    frame6=Frame(bg="gray21")
    frame6.place(x=450,y=580, width=300, height=100)
    
    frame7=Frame(bg="gray21")
    frame7.place(x=260,y=700, width=300, height=100)
    
    btn_searchpname = tk.Button(frame1, text ="SEARCH BY NAME",bg='gray21',font = ("Times New Roman Bold", 25),command=searchpname) 
    btn_searchpname.place(x = 10, y = 30, width = 290)
    btn_searchprice = tk.Button(frame2, text ="SEARCH BY PRICE", bg='gray21',font = ("Times New Roman Bold", 25))
    #,command=searchprice)
    btn_searchprice.place(x=10, y = 30, width = 290)
    btn_searchcategory = tk.Button(frame3, text ="SERACH BY CATEGORY", bg='gray21',font = ("Times New Roman Bold", 25),command=mainuser)
    #,command=category) 
    btn_searchcategory.place(x = 10, y = 30, width = 290)
    
    btn_displayall = tk.Button(frame4, text ="ALL PRODUCTS",bg='gray21',font = ("Times New Roman Bold", 25),command=searchpname) 
    btn_displayall.place(x = 10, y = 30, width = 290)
    
#     btnmain = tk.Button(frame7, text ="MAIN MENU", bg='gray21',font = ("Times New Roman Bold", 25),command=mainadmin) 
#     btnmain.place(x = 10, y = 30, width = 290)
        
        
def searchpname():
    def Clear():
        ttxtpno.delete(0,END)
        txtpname.delete(0,END)
        txtpcat.delete(0,END)
        txtprice.delete(0,END)
        txt.qw.delete(0,END)
        txtdesp.delete(0,END)
        txtimg.delete(0,END)
        
    search = tk.PhotoImage(file="searchesmenu.png")
    img_label = Label(image = search)
    img_label.place(x=0,y=0)
    img_label.image = search
    
    frame=Frame(bg="gray21")
    frame.place(x=30,y=175, width=700, height=600)
    
    def Search():
        pno = txtpno.get() 
        pname = txtpname.get()
        pcat=txtpcat.get()
        price=txtprice.get()
        qw=txtqw.get()
        desc=txtdesp.get()
        img=txtimg.get()
        try:
            myconn=mys.connect(host='localhost',user="root",passwd="icecream123",database="bakery")
            if myconn.is_connected():
                print("connection succssful")
            mycur=myconn.cursor()
            pno=txtpno.get()
            query1="select * from product where pname={}".format(pname)
            mycur.execute(query1)
            rs1=mycur.fetchone()
            rs1=list(rs1)
            
            query2="select * from img where pname={}".format(pname)
            mycur.execute(query2)
            rs2=mycur.fetchone()
            rs2=list(rs2)
            
            pcode = rs1[0] 
            pname = rs1[1]
            category=rs1[2]
            price= rs1[3]
            qty_weight= rs1[4]
            descp= rs1[5]
            img=rs2[0]
            
            if rs==None:
                messagebox.showinfo("PRODUCT INFO","No such product found!")
            else:
                messagebox.showinfo("PRODUCT INFO"," Product found! ")
                txtpname.insert(END,pname)
                txtpcat.insert(END,category)
                txtprice.insert(END,price)
                txtqw.insert(END,qty_weight)
                txtdesp.insert(END,descp)
                txtimg.insert(END,img)
        except Exception as e:
            print(e)
    
    try:
        myconn=mys.connect(host='localhost',user="root",passwd="icecream123",database="bakery")
        if myconn.is_connected():
            print("connection succssful")
        mycur=myconn.cursor()
        pname=txtpname.get()
        query1="select * from product where pname={}".format(pname)
        rs1=mycur.fetchone()
        rs1=list(rs1)
            
        if rs==None:
            messagebox.showinfo("PRODUCT INFO","No such product found!")
        else:
            messagebox.showinfo("PRODUCT INFO"," Product found! ")
            txtpname.insert(END,pname)
            txtpcat.insert(END,category)
            txtprice.insert(END,price)
            txtqw.insert(END,qty_weight)
            txtdesp.insert(END,descp)
            txtimg.insert(END,img)
    except Exception as e:
        print(e)
    lblpno = tk.Label(frame, text ="Product Code",bg='gray21',font = ("Times New Roman Bold", 25),fg='white' ) 
    lblpno.place(x = 40, y = 30) 
    txtpno= tk.Entry(frame, width = 35,bg='gray21',font = ("Times New Roman Bold", 30),fg='white') 
    txtpno.place(x = 240, y = 30, width = 300) 
    lblpname = tk.Label(frame, text ="Product Name",bg='gray21',font = ("Times New Roman Bold", 25),fg='white') 
    lblpname.place(x = 40, y = 105) 
    txtpname = tk.Entry(frame, width = 35,bg='gray21',font = ("Times New Roman Bold", 30),fg='white') 
    txtpname.place(x = 240, y = 105, width = 300) 
    lblpcat = tk.Label(frame, text ="Category",bg='gray21',font = ("Times New Roman Bold", 25) ,fg='white') 
    lblpcat.place(x = 40, y = 180) 
    txtpcat= tk.Entry(frame, width = 35,bg='gray21',font = ("Times New Roman Bold", 25),fg='white') 
    txtpcat.place(x = 240, y =180, width = 300) 
    lblprice = tk.Label(frame, text ="Price",bg='gray21',font = ("Times New Roman Bold", 25),fg='white') 
    lblprice.place(x = 40, y = 255)
    txtprice = tk.Entry(frame, width = 35,bg='gray21',font = ("Times New Roman Bold", 25),fg='white') 
    txtprice.place(x = 240, y = 255, width = 300)
    lblqw = tk.Label(frame, text ="Quantity/Weight",bg='gray21',font = ("Times New Roman Bold", 25),fg='white' ) 
    lblqw.place(x = 40, y = 330) 
    txtqw= tk.Entry(frame, width = 35,bg='gray21',font = ("Times New Roman Bold", 30),fg='white') 
    txtqw.place(x = 240, y = 330, width = 300)
    lbldesp = tk.Label(frame, text ="Description",bg='gray21',font = ("Times New Roman Bold", 25),fg='white' ) 
    lbldesp.place(x = 40, y = 405) 
    txtdesp= tk.Entry(frame, width = 35,bg='gray21',font = ("Times New Roman Bold", 30),fg='white') 
    txtdesp.place(x = 240, y = 405, width = 300)
    lblimg = tk.Label(frame, text ="Image",bg='gray21',font = ("Times New Roman Bold", 25),fg='white' ) 
    lblimg.place(x = 40, y = 480) 
    txtimg= tk.Entry(frame, width = 35,bg='gray21',font = ("Times New Roman Bold", 30),fg='white') 
    txtimg.place(x = 240, y = 480, width = 300)
     
   
    btnsearch = tk.Button(frame, text ="SEARCH", bg='gray21',font = ("Times New Roman Bold", 25),command=Search) 
    btnsearch.place(x = 40, y = 555, width = 120)
    btnclear = tk.Button(frame, text ="CLEAR", bg='gray21',font = ("Times New Roman Bold", 25),command=Clear) 
    btnclear.place(x = 200, y = 555, width = 120)
    btnmain = tk.Button(frame, text ="MAIN MENU", bg='gray21',font = ("Times New Roman Bold", 25),command=searchmenu) 
    btnmain.place(x = 360, y = 555, width = 240)


#_________PRICE SEARCH
def serachprice():
    
        
    searchprice = tk.PhotoImage(file="searchesmenu.png")
    img_label = Label(image = searchprice)
    img_label.place(x=0,y=0)
    img_label.image = searchprice
    
    frame=Frame(bg="gray21")
    frame.place(x=30,y=175, width=700, height=600)
    
    def Search():
        lowerprice=txtprice.get()
        upperprice=txtprice.get()
        try:
            myconn=mys.connect(host='localhost',user="root",passwd="icecream123",database="bakery")
            if myconn.is_connected():
                print("connection succssful")
            mycur=myconn.cursor()
            pno=txtpno.get()
            query1="select * from product where price<={} and price>={}".format(upperprice,lowerprice)
            mycur.execute(query1)
            rs1=mycur.fetchall()
            rs1=list(rs1)
            
            query2="select * from img where pname={}".format(pname)
            mycur.execute(query2)
            rs2=mycur.fetchone()
            rs2=list(rs2)
            
            pcode = rs1[0] 
            pname = rs1[1]
            category=rs1[2]
            price= rs1[3]
            qty_weight= rs1[4]
            descp= rs1[5]
            img=rs2[0]
            
            if rs==None:
                messagebox.showinfo("PRODUCT INFO","No such product found!")
            else:
                messagebox.showinfo("PRODUCT INFO"," Product found! ")
                txtpname.insert(END,pname)
                txtpcat.insert(END,category)
                txtprice.insert(END,price)
                txtqw.insert(END,qty_weight)
                txtdesp.insert(END,descp)
                txtimg.insert(END,img)
        except Exception as e:
            print(e)
    
    try:
        myconn=mys.connect(host='localhost',user="root",passwd="icecream123",database="bakery")
        if myconn.is_connected():
            print("connection succssful")
        mycur=myconn.cursor()
        pname=txtpname.get()
        query1="select * from product where pname={}".format(pname)
        rs1=mycur.fetchone()
        rs1=list(rs1)
            
        if rs==None:
            messagebox.showinfo("PRODUCT INFO","No such product found!")
        else:
            messagebox.showinfo("PRODUCT INFO"," Product found! ")
            txtpname.insert(END,pname)
            txtpcat.insert(END,category)
            txtprice.insert(END,price)
            txtqw.insert(END,qty_weight)
            txtdesp.insert(END,descp)
            txtimg.insert(END,img)
    except Exception as e:
        print(e)
    
    lbllowerprice = tk.Label(frame, text ="Price",bg='gray21',font = ("Times New Roman Bold", 25),fg='white') 
    lbllowerprice.place(x = 40, y = 255)
    lblupperprice = tk.Entry(frame, width = 35,bg='gray21',font = ("Times New Roman Bold", 25),fg='white') 
    lblupperprice.place(x = 240, y = 255, width = 300)
    
   
    btnsearch = tk.Button(frame, text ="SEARCH", bg='gray21',font = ("Times New Roman Bold", 25),command=Search) 
    btnsearch.place(x = 40, y = 555, width = 120)
    btnclear = tk.Button(frame, text ="CLEAR", bg='gray21',font = ("Times New Roman Bold", 25),command=Clear) 
    btnclear.place(x = 200, y = 555, width = 120)
    btnmain = tk.Button(frame, text ="MAIN MENU", bg='gray21',font = ("Times New Roman Bold", 25),command=searchmenu) 
    btnmain.place(x = 360, y = 555, width = 240)
def display_product(p):
    
    for ele in lstpname:
        mainuser = tk.PhotoImage(file="userframe.png")
        img_label = Label(image = mainuser)
        img_label.grid(row=4, column=0)
        img_label.image = mainuser
        
        
        frame=Frame(bg="tan")
        frame.place(x=30,y=200, width=1400, height=600)

        if ele==p:
            myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
            if myconn.is_connected():
                print("connection successful")
            mycur = myconn.cursor()
            query1 = "SELECT * FROM product WHERE pname='{}'".format(p)
            mycur.execute(query1)
            rs1 = mycur.fetchall()
            pnamelbl=Label (frame, text=rs1[0][1], font=("times new roman",40,'bold') ,bg="tan", fg="black")
            pnamelbl.place(x=80,y=20)
            
            pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
            pricelbl.place(x=80,y=80)
            
            qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' kg', font=("times new roman",25) ,bg="tan", fg="black")
            qwlbl.place(x=80,y=150)
            
            desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
            desclbl.place(x=80,y=220)
            
            imgpath=str(rs1[0][6])
            
            # Create an "Add to Cart" button
            add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
            add_to_cart_button.place(x=80,y=420,width=200,height=35)
            
            # Create an main menu button
            main_menu_button = tk.Button(frame, text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white", command=mainuser)
            main_menu_button.place(x=320,y=420,width=200,height=35)
            
            print(imgpath)
            #PLACING IMAGE IN FRAME
            imgs = tk.PhotoImage(file=imgpath)
            img_label = Label(image = imgs)
            img_label.image = imgs
            img_label.place(x=400, y=150)
    mainuser = tk.PhotoImage(file="userframe.png")
    img_label = Label(image = mainuser)
    img_label.grid(row=4, column=0)
    img_label.image = mainuser
    
    
    frame=Frame(bg="tan")
    frame.place(x=30,y=200, width=1400, height=600)
    #making dictionary with pno as keys and pname as values
    lstpname=[]
    lstpno=[]
    myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
    if myconn.is_connected():
        print("connection successful")
    mycur = myconn.cursor()
    query1 = "SELECT pname FROM product WHERE category='Cakes' ORDER BY pcode ASC"
    mycur.execute(query1)
    rs1 = mycur.fetchall()
    
    for values in rs1:
        lstpname+=values

    query2 = "SELECT pcode FROM product WHERE category='Cakes' ORDER BY pcode ASC"
    mycur.execute(query2)
    rs2 = mycur.fetchall()
    nameno={}
    for values in rs2:
        lstpno+=values
    for i in range(len(lstpname)):
        nameno[lstpname[i]] = lstpno[i]
        
    for i in range(0,len(lstpname)):
        product_name = lstpname[i]
        product_button = tk.Button(frame, text=product_name , command=lambda p=product_name : display_product(p))
        product_button.pack(padx=10, pady=5, fill=tk.X)
    

#----------------------------------------USER MAIN PAGE--------------------------

def mainuser():
    mainuser = tk.PhotoImage(file="user menu.png")
    img_label = Label(image = mainuser)
    img_label.grid(row=4, column=0)
    img_label.image = mainuser
    

    
    cakesbtn=Button(text="Cakes", command=dispcakesuser,font=("Times New Roman",30,"bold"),bd=3,relief=RIDGE,background="black",fg="lightcoral",activeforeground="black", activebackground="black")
    cakesbtn.place(x=60,y=530,width=200,height=50)

    cupcakesbtn=Button(text="Cupcakes", command =dispcupcakesuser,font=("Times New Roman",30,"bold"),bd=3,relief=RIDGE,background="black",fg="lightcoral",activeforeground="black", activebackground="black")
    cupcakesbtn.place(x=340,y=530,width=200,height=50)
    
    browniesbtn=Button(text="Brownies", command =dispbrowniesuser,font=("Times New Roman",30,"bold"),bd=3,relief=RIDGE,background="black",fg="lightcoral",activeforeground="black", activebackground="black")
    browniesbtn.place(x=900,y=530,width=200,height=50)
    
    cookiesbtn=Button(text="Cookies",command=dispcookiesuser, font=("Times New Roman",30,"bold"),bd=3,relief=RIDGE,background="black",fg="lightcoral",activeforeground="black", activebackground="black")
    cookiesbtn.place(x=620,y=530,width=200,height=50)
    
    otherdesserts=Button(text="Other Desserts",command=dispother,font=("Times New Roman",30,"bold"),bd=3,relief=RIDGE,background="black",fg="lightcoral",activeforeground="black", activebackground="black")
    otherdesserts.place(x=1180,y=530,width=200,height=50)

    allprdt=Button(text="All products",font=("Times New Roman",30,"bold"),bd=3,relief=RIDGE,background="black",fg="lightcoral",activeforeground="black", activebackground="black")
    allprdt.place(x=340,y=600,width=200,height=50)

    searchbtn=Button(text="Searches",command=searchmenu,font=("Times New Roman",30,"bold"),bd=3,relief=RIDGE,background="black",fg="lightcoral",activeforeground="black", activebackground="black")
    searchbtn.place(x=60,y=600,width=200,height=50)


#-------------------------------------------------ADD TO CART FUNC-------------------------------------------------




#--------------IMAGE LOADING----------
def load_and_display_image(image_path, label_widget):
    img = Image.open(image_path)
    img = img.resize((750, 500))
    tk_image = ImageTk.PhotoImage(img)
    label_widget.config(image=tk_image)
    label_widget.image = tk_image  # Store a reference to the image
    
def display_image(image_data):
    image = Image.open(BytesIO(image_data))
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo)
    label.image = photo
    label.pack()
    
    
    
'''
import tkinter as tk
from PIL import Image, ImageTk

class ImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image in Frame Example")

        self.frame = tk.Frame(root, padx=10, pady=10)
        self.frame.pack()

        self.image_label = tk.Label(self.frame)
        self.image_label.place(x=50, y=50)  # Specify the desired coordinates

        self.load_and_display_image("path_to_your_image.png")  # Replace with the actual path

    def load_and_display_image(self, image_path):
        img = Image.open(image_path)
        img = img.resize((300, 300))
        self.tk_image = ImageTk.PhotoImage(img)  # Store the PhotoImage in an instance attribute
        self.image_label.config(image=self.tk_image)  # Configure the label's image attribute

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageApp(root)
    root.mainloop()
'''




def get_img(p):
    try:
        myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
        if myconn.is_connected():
            print("connection successful")
        mycur = myconn.cursor()
        query = "select img from img where pcode={}".format(p)
        mycur.execute(query)
        rs = mycur.fetchone()
        
        if rs.rowcount()!=0:
            img_path=rs[0]
            print(img_path)
            return img_path
    except AttributeError as e:
        print("AttributeError occurred:", e)  
    except Exception as e:
        print(e)
        
        
def get_pno():
    try:
        myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
        if myconn.is_connected():
            print("connection successful")
        mycur = myconn.cursor()
        query = "select pcode from product where pname={}".format(pname)
        mycur.execute(query)
        rs = mycur.fetchone()
        return rs
    except Exception as e:
        print(e)




    


#-------------------------------------------------DISPLAY ITMES-------------------------------------------------

def dispcakesuser():
    '''
    def displaypic(p):
        class image:
            def init(self,root,image_data):
                self.root=root
                self.image_data=image_data
                self.create_image_display()
            def create_image_display(self):
                image = Imgae.open(io.ByesIO(self.image_data))
                self.tk_image=ImageTk.PhotoImage(image)
                self.label=Label(self.root, image=self.tk_image)
                self.label.pack()
            def main(p):
                try:
                    myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
                    cur=myconn.cursor()
                    query="select imgpath from product where pname={}".format(p)
                    cur.execute()
                    row=cur.fetchone()
                    cur.close()
                    myconn.close()
                    if row:
                        image_data=row[0]
                        image_root = Toplevel()
                        image_display=ImageDisplay(image_root,image_data)
                        image_display.rootmainloop()
                    else:
                        print("Image not found")
                    cur.close()
                    myconn.close()
                except Exception as e:
                    print("Error: ",str(e))
    if __name__== "__main__":
        main(p)
    '''
    def display_product(p):

        for ele in lstpname:
            mainuser = tk.PhotoImage(file="userframe.png")
            img_label = Label(image = mainuser)
            img_label.grid(row=4, column=0)
            img_label.image = mainuser
            
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=200, width=1400, height=600)
    
            if ele==p:
                myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
                if myconn.is_connected():
                    print("connection successful")
                mycur = myconn.cursor()
                query1 = "SELECT * FROM product WHERE pname='{}'".format(p)
                mycur.execute(query1)
                rs1 = mycur.fetchall()
                pnamelbl=Label (frame, text=rs1[0][1], font=("times new roman",40,'bold') ,bg="tan", fg="black")
                pnamelbl.place(x=80,y=20)
                
                pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
                pricelbl.place(x=80,y=80)
                
                qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' kg', font=("times new roman",25) ,bg="tan", fg="black")
                qwlbl.place(x=80,y=150)
                
                desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
                desclbl.place(x=80,y=220)
                
                imgpath=str(rs1[0][6])
                print(imgpath)
                # Create an "Add to Cart" button
                add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                add_to_cart_button.place(x=80,y=420,width=200,height=35)
                
                # Create an main menu button
                main_menu_button = tk.Button(frame, text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white", command=mainuser)
                main_menu_button.place(x=320,y=420,width=200,height=35)
                
                print(imgpath)
                #PLACING IMAGE IN FRAME
                imgs = tk.PhotoImage(file=imgpath)
                img_label = Label(image = imgs)
                img_label.image = imgs
                img_label.place(x=400, y=150)
    
    mainuser = tk.PhotoImage(file="userframe.png")
    img_label = Label(image = mainuser)
    img_label.grid(row=4, column=0)
    img_label.image = mainuser
    
    
    frame=Frame(bg="tan")
    frame.place(x=30,y=200, width=1400, height=600)
    #making dictionary with pno as keys and pname as values
    lstpname=[]
    lstpno=[]
    myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
    if myconn.is_connected():
        print("connection successful")
    mycur = myconn.cursor()
    query1 = "SELECT pname FROM product WHERE category='Cakes' ORDER BY pcode ASC"
    mycur.execute(query1)
    rs1 = mycur.fetchall()
    
    for values in rs1:
        lstpname+=values

    query2 = "SELECT pcode FROM product WHERE category='Cakes' ORDER BY pcode ASC"
    mycur.execute(query2)
    rs2 = mycur.fetchall()
    nameno={}
    for values in rs2:
        lstpno+=values
    for i in range(len(lstpname)):
        nameno[lstpname[i]] = lstpno[i]
        
    for i in range(0,len(lstpname)):
        product_name = lstpname[i]
        product_button = tk.Button(frame, text=product_name , command=lambda p=product_name : display_product(p))
        product_button.pack(padx=10, pady=5, fill=tk.X)
    '''
    def display_product(p):
        if p =='Original NY Plain Cheesecake':
            
            imgcake = tk.PhotoImage(file="userframe.png")
            img_label = Label(image = imgcake)
            img_label.grid(row=3, column=0)
            img_label.image = imgcake
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=200, width=1500, height=580)
            
            pnamelbl=Label (frame, text="Original NY Plain Cheesecake", font=("times new roman", 40, "bold") ,bg="tan", fg="black")
            pnamelbl.config(anchor="n")
            pnamelbl.pack()
            
            myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
            if myconn.is_connected():
                print("connection successful")
            mycur = myconn.cursor()
            query1 = "SELECT * FROM product WHERE pname='Original NY Plain Cheesecake'"
            mycur.execute(query1)
            rs1 = mycur.fetchall()
            pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
            pricelbl.place(x=80,y=80)
            
            qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' kg', font=("times new roman",25) ,bg="tan", fg="black")
            qwlbl.place(x=80,y=150)
            
            desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
            desclbl.place(x=80,y=220)
            
            # Create an "Add to Cart" button
            add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
            add_to_cart_button.place(x=80,y=420,width=200,height=35)
            
            # Create an main menu button
            main_menu_button = tk.Button(frame, text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white", command=mainuser)
            main_menu_button.place(x=320,y=420,width=200,height=35)
            
            
            #PLACING IMAGE IN FRAME
            image_label = tk.Label(frame)
            image_label.place(x=675,y=80)

            image_path = "/Users/diyasatish/Desktop/bakery2/imagesprdt/nyog.png"  # Replace with the actual path to your image
            load_and_display_image(image_path, image_label)
                        
            
#             image_label = tk.Label(frame)
#             image_label.place(x=50,y=800)
# 
#             image_path = "/Users/diyasatish/Desktop/bakery2/imagesprdt/nyog.png"  # Replace with the actual path to your image
#             load_and_display_image(image_path, image_label)

#             image_path = "/Users/diyasatish/Desktop/bakery2/imagesprdt/nyog.png"  # Replace with the actual path to your image
#             img = Image.open(image_path)
#             img = img.resize((300, 300))  # Resize the image to fit within the frame
# 
#             # Convert the PIL image to Tkinter PhotoImage
#             tk_image = ImageTk.PhotoImage(img)
# 
#             # Create a label widget to display the image
#             image_label = tk.Label(frame, image=tk_image)
#             image_label.pack()

#             imguserframe = tk.PhotoImage(file="userframe.png")
#             img_label = Label(image = imguserframe)
#             img_label.place(frame,
#             img_label.image = imguserframe
            
            
        if p =='Strawberry Cheesecake':
            
            imgcake = tk.PhotoImage(file="strawberrycheescake.png")
            img_label = Label(image = imgcake)
            img_label.grid(row=3, column=0)
            img_label.image = imgcake
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=196, width=800, height=580)
            
            pnamelbl=Label (frame, text=p, font=("times new roman", 40, "bold") ,bg="tan", fg="black")
            pnamelbl.config(anchor="n")
            pnamelbl.pack()
            
            myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
            if myconn.is_connected():
                print("connection successful")
            mycur = myconn.cursor()
            query1 = "SELECT * FROM product WHERE pname='Strawberry Cheesecake'"
            mycur.execute(query1)
            rs1 = mycur.fetchall()
            pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
            pricelbl.place(x=80,y=80)
            
            qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' kg', font=("times new roman",25) ,bg="tan", fg="black")
            qwlbl.place(x=80,y=150)
            
            desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
            desclbl.place(x=80,y=220)
            
             # Create an "Add to Cart" button
            add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
            add_to_cart_button.place(x=80,y=420,width=200,height=35)
            
            # Create an main menu button
            main_menu_button = tk.Button(frame, command=mainuser,text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
            main_menu_button.place(x=320,y=420,width=200,height=35)
            
        
        if p =='Honey Cake':
            
            imgcake = tk.PhotoImage(file="honey cake.png")
            img_label = Label(image = imgcake)
            img_label.grid(row=3, column=0)
            img_label.image = imgcake
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=196, width=800, height=580)
            
            pnamelbl=Label (frame, text=p, font=("times new roman", 40, "bold") ,bg="tan", fg="black")
            pnamelbl.config(anchor="n")
            pnamelbl.pack()
            try:
                myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
                if myconn.is_connected():
                    print("connection successful")
                mycur = myconn.cursor()
                query1 = "SELECT * FROM product WHERE pname='Honey Cake'"
                mycur.execute(query1)
                rs1 = mycur.fetchall()
                pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
                pricelbl.place(x=80,y=80)
                
                qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' kg', font=("times new roman",25) ,bg="tan", fg="black")
                qwlbl.place(x=80,y=150)
                
                desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
                desclbl.place(x=80,y=220)
                
                # Create an "Add to Cart" button
                add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                add_to_cart_button.place(x=80,y=420,width=200,height=35)
                
                # Create an main menu button
                main_menu_button = tk.Button(frame, command=mainuser,text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                main_menu_button.place(x=320,y=420,width=200,height=35)
            
            except Exception as e:
                print(e)
        if p =='Nutella Cake':
            
            imgcake = tk.PhotoImage(file="nutella cake.png")
            img_label = Label(image = imgcake)
            img_label.grid(row=3, column=0)
            img_label.image = imgcake
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=196, width=800, height=580)
            
            pnamelbl=Label (frame, text=p, font=("times new roman", 40, "bold") ,bg="tan", fg="black")
            pnamelbl.config(anchor="n")
            pnamelbl.pack()
            try:
                myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
                if myconn.is_connected():
                    print("connection successful")
                mycur = myconn.cursor()
                query1 = "SELECT * FROM product WHERE pname='Nutella Cake'"
                mycur.execute(query1)
                rs1 = mycur.fetchall()
                pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
                pricelbl.place(x=80,y=80)
                
                qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' kg', font=("times new roman",25) ,bg="tan", fg="black")
                qwlbl.place(x=80,y=150)
                
                desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
                desclbl.place(x=80,y=220)
                # Create an "Add to Cart" button
                add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                add_to_cart_button.place(x=80,y=420,width=200,height=35)
                
                # Create an main menu button
                main_menu_button = tk.Button(frame, command=mainuser,text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                main_menu_button.place(x=320,y=420,width=200,height=35)
                
            except Exception as e:
                print(e)
                
                
                
        if p =='White Forest Cake':
            
            imgcake = tk.PhotoImage(file="white forest.png")
            img_label = Label(image = imgcake)
            img_label.grid(row=3, column=0)
            img_label.image = imgcake
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=196, width=800, height=580)
            
            pnamelbl=Label (frame, text=p, font=("times new roman", 40, "bold") ,bg="tan", fg="black")
            pnamelbl.config(anchor="n")
            pnamelbl.pack()
            try:
                myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
                if myconn.is_connected():
                    print("connection successful")
                mycur = myconn.cursor()
                query1 = "SELECT * FROM product WHERE pname='White Forest Cake'"
                mycur.execute(query1)
                rs1 = mycur.fetchall()
                pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
                pricelbl.place(x=80,y=80)
                
                qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' kg', font=("times new roman",25) ,bg="tan", fg="black")
                qwlbl.place(x=80,y=150)
                
                desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
                desclbl.place(x=80,y=220)
                
                # Create an "Add to Cart" button
                add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                add_to_cart_button.place(x=80,y=420,width=200,height=35)
                
                # Create an main menu button
                main_menu_button = tk.Button(frame, command=mainuser,text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                main_menu_button.place(x=320,y=420,width=200,height=35)
            
            except Exception as e:
                print(e)        
        
        
        if p =='Black Forest Cake':
            
            imgcake = tk.PhotoImage(file="black forest.png")
            img_label = Label(image = imgcake)
            img_label.grid(row=3, column=0)
            img_label.image = imgcake
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=196, width=800, height=580)
            
            pnamelbl=Label (frame, text=p, font=("times new roman", 40, "bold") ,bg="tan", fg="black")
            pnamelbl.config(anchor="n")
            pnamelbl.pack()
            try:
                myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
                if myconn.is_connected():
                    print("connection successful")
                mycur = myconn.cursor()
                query1 = "SELECT * FROM product WHERE pname='Black Forest Cake'"
                mycur.execute(query1)
                rs1 = mycur.fetchall()
                pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
                pricelbl.place(x=80,y=80)
                
                qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' kg', font=("times new roman",25) ,bg="tan", fg="black")
                qwlbl.place(x=80,y=150)
                
                desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
                desclbl.place(x=80,y=220)
                
                # Create an "Add to Cart" button
                add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                add_to_cart_button.place(x=80,y=420,width=200,height=35)
                
                # Create an main menu button
                main_menu_button = tk.Button(frame, command=mainuser,text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                main_menu_button.place(x=320,y=420,width=200,height=35)
            
            except Exception as e:
                print(e)     
        
        '''
        
               
    
def dispcupcakesuser():
    def display_product(p):

        for ele in lstpname:
            mainuser = tk.PhotoImage(file="userframe.png")
            img_label = Label(image = mainuser)
            img_label.grid(row=4, column=0)
            img_label.image = mainuser
            
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=200, width=1400, height=600)
    
            if ele==p:
                myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
                if myconn.is_connected():
                    print("connection successful")
                mycur = myconn.cursor()
                query1 = "SELECT * FROM product WHERE pname='{}'".format(p)
                mycur.execute(query1)
                rs1 = mycur.fetchall()
                pnamelbl=Label (frame, text=rs1[0][1], font=("times new roman",40,'bold') ,bg="tan", fg="black")
                pnamelbl.place(x=80,y=20)
                
                pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
                pricelbl.place(x=80,y=80)
                
                qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' kg', font=("times new roman",25) ,bg="tan", fg="black")
                qwlbl.place(x=80,y=150)
                
                desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
                desclbl.place(x=80,y=220)
                
                
                # Create an "Add to Cart" button
                add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                add_to_cart_button.place(x=80,y=420,width=200,height=35)
                
                # Create an main menu button
                main_menu_button = tk.Button(frame, text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white", command=mainuser)
                main_menu_button.place(x=320,y=420,width=200,height=35)
                
                imagepath=displaypic(p)
                #PLACING IMAGE IN FRAME
                imgs = tk.PhotoImage(file=imgpath)
                img_label = Label(image = imgs)
                img_label.image = imgs
                img_label.place(x=400, y=150)
    
    mainuser = tk.PhotoImage(file="userframe.png")
    img_label = Label(image = mainuser)
    img_label.grid(row=4, column=0)
    img_label.image = mainuser
    
    
    frame=Frame(bg="tan")
    frame.place(x=30,y=200, width=1400, height=600)
    #making dictionary with pno as keys and pname as values
    lstpname=[]
    lstpno=[]
    myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
    if myconn.is_connected():
        print("connection successful")
    mycur = myconn.cursor()
    query1 = "SELECT pname FROM product WHERE category='Cupcakes' ORDER BY pcode ASC"
    mycur.execute(query1)
    rs1 = mycur.fetchall()
    
    for values in rs1:
        lstpname+=values

    query2 = "SELECT pcode FROM product WHERE category='Cupcakes' ORDER BY pcode ASC"
    mycur.execute(query2)
    rs2 = mycur.fetchall()
    nameno={}
    for values in rs2:
        lstpno+=values
    for i in range(len(lstpname)):
        nameno[lstpname[i]] = lstpno[i]
        
    for i in range(0,len(lstpname)):
        product_name = lstpname[i]
        product_button = tk.Button(frame, text=product_name , command=lambda p=product_name : display_product(p))
        product_button.pack(padx=10, pady=5, fill=tk.X)
    
    '''
        
    def display_product(p):
    
        if p =='Red Velvet Cupcakes':
            
            imgcake = tk.PhotoImage(file="redvelvetcc.png")
            img_label = Label(image = imgcake)
            img_label.grid(row=3, column=0)
            img_label.image = imgcake
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=200, width=800, height=580)
            
            pnamelbl=Label (frame, text=p, font=("times new roman", 40, "bold") ,bg="tan", fg="black")
            pnamelbl.config(anchor="n")
            pnamelbl.pack()
            
            myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
            if myconn.is_connected():
                print("connection successful")
            mycur = myconn.cursor()
            query1 = "SELECT * FROM product WHERE pname='Red Velvet Cupcakes'"
            mycur.execute(query1)
            rs1 = mycur.fetchall()
            pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
            pricelbl.place(x=80,y=80)
            
            qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' cupcakes/muffins', font=("times new roman",25) ,bg="tan", fg="black")
            qwlbl.place(x=80,y=150)
            
            desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
            desclbl.place(x=80,y=220)
            
            # Create an "Add to Cart" button
            add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
            add_to_cart_button.place(x=80,y=420,width=200,height=35)
            
            # Create an main menu button
            main_menu_button = tk.Button(frame, text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white", command=mainuser)
            main_menu_button.place(x=320,y=420,width=200,height=35)
            

            
            
            
        if p =='Blueberry Muffins':
            
            imgcake = tk.PhotoImage(file="blueberrycc.png")
            img_label = Label(image = imgcake)
            img_label.grid(row=3, column=0)
            img_label.image = imgcake
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=196, width=800, height=580)
            
            pnamelbl=Label (frame, text=p, font=("times new roman", 40, "bold") ,bg="tan", fg="black")
            pnamelbl.config(anchor="n")
            pnamelbl.pack()
            
            myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
            if myconn.is_connected():
                print("connection successful")
            mycur = myconn.cursor()
            query1 = "SELECT * FROM product WHERE pname='Blueberry Muffins'"
            mycur.execute(query1)
            rs1 = mycur.fetchall()
            pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
            pricelbl.place(x=80,y=80)
            
            qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' cupcakes/muffins', font=("times new roman",25) ,bg="tan", fg="black")
            qwlbl.place(x=80,y=150)
            
            desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
            desclbl.place(x=80,y=220)
            
             # Create an "Add to Cart" button
            add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
            add_to_cart_button.place(x=80,y=420,width=200,height=35)
            
            # Create an main menu button
            main_menu_button = tk.Button(frame, command=mainuser,text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
            main_menu_button.place(x=320,y=420,width=200,height=35)
            
#         if p =='Tall Oreo Cake':
#             
#             mainuser = tk.PhotoImage(file="oreo cake.png")
#             img_label = Label(image = mainuser)
#             img_label.grid(row=3, column=0)
#             img_label.image = mainuser
#             
#             frame=Frame(bg="tan")
#             frame.place(x=30,y=196, width=800, height=580)
#             
#             pnamelbl=Label (frame, text=p, font=("times new roman", 40, "bold") ,bg="tan", fg="black")
#             pnamelbl.config(anchor="n")
#             pnamelbl.pack()
#             try:
#                 myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
#                 if myconn.is_connected():
#                     print("connection successful")
#                 mycur = myconn.cursor()
#                 query1 = "SELECT * FROM product WHERE pname='Tall Oreo Cake'"
#                 mycur.execute(query1)
#                 rs1 = mycur.fetchall()
#                 pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
#                 pricelbl.place(x=80,y=80)
#                 
#                 qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' kg', font=("times new roman",25) ,bg="tan", fg="black")
#                 qwlbl.place(x=80,y=150)
#                 
#                 desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
#                 desclbl.place(x=80,y=220)
#             
#             except Exception as e:
#                 print(e)
        if p =='Strawberry Cupcakes':
            
            imgcake = tk.PhotoImage(file="strawberrycc.png")
            img_label = Label(image = imgcake)
            img_label.grid(row=3, column=0)
            img_label.image = imgcake
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=196, width=800, height=580)
            
            pnamelbl=Label (frame, text=p, font=("times new roman", 40, "bold") ,bg="tan", fg="black")
            pnamelbl.config(anchor="n")
            pnamelbl.pack()
            try:
                myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
                if myconn.is_connected():
                    print("connection successful")
                mycur = myconn.cursor()
                query1 = "SELECT * FROM product WHERE pname='Strawberry Cupcakes'"
                mycur.execute(query1)
                rs1 = mycur.fetchall()
                pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
                pricelbl.place(x=80,y=80)
                
                qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' cupcakes/muffins', font=("times new roman",25) ,bg="tan", fg="black")
                qwlbl.place(x=80,y=150)
                
                desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
                desclbl.place(x=80,y=220)
                
                # Create an "Add to Cart" button
                add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                add_to_cart_button.place(x=80,y=420,width=200,height=35)
                
                # Create an main menu button
                main_menu_button = tk.Button(frame, command=mainuser,text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                main_menu_button.place(x=320,y=420,width=200,height=35)
            
            except Exception as e:
                print(e)
        if p =='Banana & Chocolate Muffins':
            
            imgcake = tk.PhotoImage(file="bananachococc.png")
            img_label = Label(image = imgcake)
            img_label.grid(row=3, column=0)
            img_label.image = imgcake
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=196, width=800, height=580)
            
            pnamelbl=Label (frame, text=p, font=("times new roman", 40, "bold") ,bg="tan", fg="black")
            pnamelbl.config(anchor="n")
            pnamelbl.pack()
            try:
                myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
                if myconn.is_connected():
                    print("connection successful")
                mycur = myconn.cursor()
                query1 = "SELECT * FROM product WHERE pname='Banana & Chocolate Muffins'"
                mycur.execute(query1)
                rs1 = mycur.fetchall()
                pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
                pricelbl.place(x=80,y=80)
                
                qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' cupcakes/muffins', font=("times new roman",25) ,bg="tan", fg="black")
                qwlbl.place(x=80,y=150)
                
                desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
                desclbl.place(x=80,y=220)
                # Create an "Add to Cart" button
                add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                add_to_cart_button.place(x=80,y=420,width=200,height=35)
                
                # Create an main menu button
                main_menu_button = tk.Button(frame, command=mainuser,text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                main_menu_button.place(x=320,y=420,width=200,height=35)
                
            except Exception as e:
                print(e)
                
                
                
        if p =='Oreo Cupcakes':
            
            imgcake = tk.PhotoImage(file="oreocc.png")
            img_label = Label(image = imgcake)
            img_label.grid(row=3, column=0)
            img_label.image = imgcake
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=196, width=800, height=580)
            
            pnamelbl=Label (frame, text=p, font=("times new roman", 40, "bold") ,bg="tan", fg="black")
            pnamelbl.config(anchor="n")
            pnamelbl.pack()
            try:
                myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
                if myconn.is_connected():
                    print("connection successful")
                mycur = myconn.cursor()
                query1 = "SELECT * FROM product WHERE pname='Oreo Cupcakes'"
                mycur.execute(query1)
                rs1 = mycur.fetchall()
                pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
                pricelbl.place(x=80,y=80)
                
                qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' cupcakes/muffins', font=("times new roman",25) ,bg="tan", fg="black")
                qwlbl.place(x=80,y=150)
                
                desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
                desclbl.place(x=80,y=220)
                
                # Create an "Add to Cart" button
                add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                add_to_cart_button.place(x=80,y=420,width=200,height=35)
                
                # Create an main menu button
                main_menu_button = tk.Button(frame, command=mainuser,text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                main_menu_button.place(x=320,y=420,width=200,height=35)
            
            except Exception as e:
                print(e)        
        
        
        if p =='Confetti Cupcakes':
            
            imgcake = tk.PhotoImage(file="confetticc.png")
            img_label = Label(image = imgcake)
            img_label.grid(row=3, column=0)
            img_label.image = imgcake
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=196, width=800, height=580)
            
            pnamelbl=Label (frame, text=p, font=("times new roman", 40, "bold") ,bg="tan", fg="black")
            pnamelbl.config(anchor="n")
            pnamelbl.pack()
            try:
                myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
                if myconn.is_connected():
                    print("connection successful")
                mycur = myconn.cursor()
                query1 = "SELECT * FROM product WHERE pname='Confetti Cupcakes'"
                mycur.execute(query1)
                rs1 = mycur.fetchall()
                pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
                pricelbl.place(x=80,y=80)
                
                qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' cupcakes/muffins', font=("times new roman",25) ,bg="tan", fg="black")
                qwlbl.place(x=80,y=150)
                
                desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
                desclbl.place(x=80,y=220)
                
                # Create an "Add to Cart" button
                add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                add_to_cart_button.place(x=80,y=420,width=200,height=35)
                
                # Create an main menu button
                main_menu_button = tk.Button(frame, command=mainuser,text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                main_menu_button.place(x=320,y=420,width=200,height=35)
            
            except Exception as e:
                print(e)     
        
        
        
               
    mainuser = tk.PhotoImage(file="userframe.png")
    img_label = Label(image = mainuser)
    img_label.grid(row=4, column=0)
    img_label.image = mainuser
    
    
    frame=Frame(bg="tan")
    frame.place(x=30,y=200, width=1400, height=600)
    
    
    lstpname=[]
    lstpno=[]
    myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
    if myconn.is_connected():
        print("connection successful")
    mycur = myconn.cursor()
    query1 = "SELECT pname FROM product WHERE category='Cupcakes'"
    mycur.execute(query1)
    rs1 = mycur.fetchall()
    
    for values in rs1:
        lstpname+=values

    query2 = "SELECT pcode FROM product WHERE category='Cupcakes'"
    mycur.execute(query2)
    rs2 = mycur.fetchall()
    nameno={}
    for values in rs2:
        lstpno+=values
    for i in range(len(lstpname)):
        nameno[lstpname[i]] = lstpno[i]
        
    for i in range(0,len(lstpname)):
        product_name = lstpname[i]
        product_button = tk.Button(frame, text=product_name, command=lambda p=product_name: display_product(p))
        product_button.pack(padx=10, pady=5, fill=tk.X)
    '''
 
def dispcookiesuser():
    def display_product(p):

        for ele in lstpname:
            mainuser = tk.PhotoImage(file="userframe.png")
            img_label = Label(image = mainuser)
            img_label.grid(row=4, column=0)
            img_label.image = mainuser
            
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=200, width=1400, height=600)
    
            if ele==p:
                myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
                if myconn.is_connected():
                    print("connection successful")
                mycur = myconn.cursor()
                query1 = "SELECT * FROM product WHERE pname='{}'".format(p)
                mycur.execute(query1)
                rs1 = mycur.fetchall()
                pnamelbl=Label (frame, text=rs1[0][1], font=("times new roman",40,'bold') ,bg="tan", fg="black")
                pnamelbl.place(x=80,y=20)
                
                pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
                pricelbl.place(x=80,y=80)
                
                qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' kg', font=("times new roman",25) ,bg="tan", fg="black")
                qwlbl.place(x=80,y=150)
                
                desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
                desclbl.place(x=80,y=220)
                
                imgpath=str(rs1[0][6])
                
                # Create an "Add to Cart" button
                add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                add_to_cart_button.place(x=80,y=420,width=200,height=35)
                
                # Create an main menu button
                main_menu_button = tk.Button(frame, text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white", command=mainuser)
                main_menu_button.place(x=320,y=420,width=200,height=35)
                
                print(imgpath)
                #PLACING IMAGE IN FRAME
                imgs = tk.PhotoImage(file="302-redvelvetcookies.png")
                img_label = Label(frame, image = imgs)
                img_label.image = imgs
                img_label.place(x=400, y=150)
    
    mainuser = tk.PhotoImage(file="userframe.png")
    img_label = Label(image = mainuser)
    img_label.grid(row=4, column=0)
    img_label.image = mainuser
    
    
    frame=Frame(bg="tan")
    frame.place(x=30,y=200, width=1400, height=600)
    #making dictionary with pno as keys and pname as values
    lstpname=[]
    lstpno=[]
    myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
    if myconn.is_connected():
        print("connection successful")
    mycur = myconn.cursor()
    query1 = "SELECT pname FROM product WHERE category='Cookies' ORDER BY pcode ASC"
    mycur.execute(query1)
    rs1 = mycur.fetchall()
    
    for values in rs1:
        lstpname+=values

    query2 = "SELECT pcode FROM product WHERE category='Cookies' ORDER BY pcode ASC"
    mycur.execute(query2)
    rs2 = mycur.fetchall()
    nameno={}
    for values in rs2:
        lstpno+=values
    for i in range(len(lstpname)):
        nameno[lstpname[i]] = lstpno[i]
        
    for i in range(0,len(lstpname)):
        product_name = lstpname[i]
        product_button = tk.Button(frame, text=product_name , command=lambda p=product_name : display_product(p))
        product_button.pack(padx=10, pady=5, fill=tk.X)
    
    '''
        
    def display_product(p):
    
        if p =='Chocolate Chip Cookies':
            
            imgcake = tk.PhotoImage(file="Chocolate Chip Cookies.png")
            img_label = Label(image = imgcake)
            img_label.grid(row=3, column=0)
            img_label.image = imgcake
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=200, width=800, height=580)
            
            pnamelbl=Label (frame, text=p, font=("times new roman", 40, "bold") ,bg="tan", fg="black")
            pnamelbl.config(anchor="n")
            pnamelbl.pack()
            
            myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
            if myconn.is_connected():
                print("connection successful")
            mycur = myconn.cursor()
            query1 = "SELECT * FROM product WHERE pname='Chocolate Chip Cookies'"
            mycur.execute(query1)
            rs1 = mycur.fetchall()
            pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
            pricelbl.place(x=80,y=80)
            
            qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' cookies', font=("times new roman",25) ,bg="tan", fg="black")
            qwlbl.place(x=80,y=150)
            
            desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
            desclbl.place(x=80,y=220)
            
            # Create an "Add to Cart" button
            add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
            add_to_cart_button.place(x=80,y=420,width=200,height=35)
            
            # Create an main menu button
            main_menu_button = tk.Button(frame, text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white", command=mainuser)
            main_menu_button.place(x=320,y=420,width=200,height=35)
            

            
            
            
        if p =='Red Velvet Cookies':
            
            imgcake = tk.PhotoImage(file="redvelvetcookies.png")
            img_label = Label(image = imgcake)
            img_label.grid(row=3, column=0)
            img_label.image = imgcake
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=196, width=800, height=580)
            
            pnamelbl=Label (frame, text=p, font=("times new roman", 40, "bold") ,bg="tan", fg="black")
            pnamelbl.config(anchor="n")
            pnamelbl.pack()
            
            myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
            if myconn.is_connected():
                print("connection successful")
            mycur = myconn.cursor()
            query1 = "SELECT * FROM product WHERE pname='Red Velvet Cookies'"
            mycur.execute(query1)
            rs1 = mycur.fetchall()
            pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
            pricelbl.place(x=80,y=80)
            
            qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' cookies', font=("times new roman",25) ,bg="tan", fg="black")
            qwlbl.place(x=80,y=150)
            
            desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
            desclbl.place(x=80,y=220)
            
             # Create an "Add to Cart" button
            add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
            add_to_cart_button.place(x=80,y=420,width=200,height=35)
            
            # Create an main menu button
            main_menu_button = tk.Button(frame, command=mainuser,text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
            main_menu_button.place(x=320,y=420,width=200,height=35)
            

        if p =='Baked Jam Cookies':
            
            imgcake = tk.PhotoImage(file="jamcookies.png")
            img_label = Label(image = imgcake)
            img_label.grid(row=3, column=0)
            img_label.image = imgcake
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=196, width=800, height=580)
            
            pnamelbl=Label (frame, text=p, font=("times new roman", 40, "bold") ,bg="tan", fg="black")
            pnamelbl.config(anchor="n")
            pnamelbl.pack()
            try:
                myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
                if myconn.is_connected():
                    print("connection successful")
                mycur = myconn.cursor()
                query1 = "SELECT * FROM product WHERE pname='Baked Jam Cookies'"
                mycur.execute(query1)
                rs1 = mycur.fetchall()
                pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
                pricelbl.place(x=80,y=80)
                
                qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' cookies', font=("times new roman",25) ,bg="tan", fg="black")
                qwlbl.place(x=80,y=150)
                
                desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
                desclbl.place(x=80,y=220)
                
                # Create an "Add to Cart" button
                add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                add_to_cart_button.place(x=80,y=420,width=200,height=35)
                
                # Create an main menu button
                main_menu_button = tk.Button(frame, command=mainuser,text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                main_menu_button.place(x=320,y=420,width=200,height=35)
            
            except Exception as e:
                print(e)
        if p =='Peanut Butter Cookies':
            
            imgcake = tk.PhotoImage(file="peanutbuttercookeis.png")
            img_label = Label(image = imgcake)
            img_label.grid(row=3, column=0)
            img_label.image = imgcake
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=196, width=800, height=580)
            
            pnamelbl=Label (frame, text=p, font=("times new roman", 40, "bold") ,bg="tan", fg="black")
            pnamelbl.config(anchor="n")
            pnamelbl.pack()
            try:
                myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
                if myconn.is_connected():
                    print("connection successful")
                mycur = myconn.cursor()
                query1 = "SELECT * FROM product WHERE pname='Peanut Butter Cookies'"
                mycur.execute(query1)
                rs1 = mycur.fetchall()
                pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
                pricelbl.place(x=80,y=80)
                
                qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' cookies', font=("times new roman",25) ,bg="tan", fg="black")
                qwlbl.place(x=80,y=150)
                
                desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
                desclbl.place(x=80,y=220)
                # Create an "Add to Cart" button
                add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                add_to_cart_button.place(x=80,y=420,width=200,height=35)
                
                # Create an main menu button
                main_menu_button = tk.Button(frame, command=mainuser,text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                main_menu_button.place(x=320,y=420,width=200,height=35)
                
            except Exception as e:
                print(e)
                
                
                
        if p =='M&M Cookies':
            
            imgcake = tk.PhotoImage(file="m&mcookies.png")
            img_label = Label(image = imgcake)
            img_label.grid(row=3, column=0)
            img_label.image = imgcake
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=196, width=800, height=580)
            
            pnamelbl=Label (frame, text=p, font=("times new roman", 40, "bold") ,bg="tan", fg="black")
            pnamelbl.config(anchor="n")
            pnamelbl.pack()
            try:
                myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
                if myconn.is_connected():
                    print("connection successful")
                mycur = myconn.cursor()
                query1 = "SELECT * FROM product WHERE pname='M&M Cookies'"
                mycur.execute(query1)
                rs1 = mycur.fetchall()
                pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
                pricelbl.place(x=80,y=80)
                
                qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' cookies', font=("times new roman",25) ,bg="tan", fg="black")
                qwlbl.place(x=80,y=150)
                
                desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
                desclbl.place(x=80,y=220)
                
                # Create an "Add to Cart" button
                add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                add_to_cart_button.place(x=80,y=420,width=200,height=35)
                
                # Create an main menu button
                main_menu_button = tk.Button(frame, command=mainuser,text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                main_menu_button.place(x=320,y=420,width=200,height=35)
            
            except Exception as e:
                print(e)        
        
        
        if p =='Kinder Cupcakes':
            
            imgcake = tk.PhotoImage(file="userframe.png")
            img_label = Label(image = imgcake)
            img_label.grid(row=3, column=0)
            img_label.image = imgcake
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=196, width=800, height=580)
            
            pnamelbl=Label (frame, text=p, font=("times new roman", 40, "bold") ,bg="tan", fg="black")
            pnamelbl.config(anchor="n")
            pnamelbl.pack()
            try:
                myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
                if myconn.is_connected():
                    print("connection successful")
                mycur = myconn.cursor()
                query1 = "SELECT * FROM product WHERE pname='Kinder Cupcakes'"
                mycur.execute(query1)
                rs1 = mycur.fetchall()
                pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
                pricelbl.place(x=80,y=80)
                
                qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' cookies', font=("times new roman",25) ,bg="tan", fg="black")
                qwlbl.place(x=80,y=150)
                
                desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
                desclbl.place(x=80,y=220)
                
                # Create an "Add to Cart" button
                add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                add_to_cart_button.place(x=80,y=420,width=200,height=35)
                
                # Create an main menu button
                main_menu_button = tk.Button(frame, command=mainuser,text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                main_menu_button.place(x=320,y=420,width=200,height=35)
            
            except Exception as e:
                print(e)     
    '''
def dispother():
    def display_product(p):

        for ele in lstpname:
            mainuser = tk.PhotoImage(file="userframe.png")
            img_label = Label(image = mainuser)
            img_label.grid(row=4, column=0)
            img_label.image = mainuser
            
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=200, width=1400, height=600)
    
            if ele==p:
                myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
                if myconn.is_connected():
                    print("connection successful")
                mycur = myconn.cursor()
                query1 = "SELECT * FROM product WHERE pname='{}'".format(p)
                mycur.execute(query1)
                rs1 = mycur.fetchall()
                pnamelbl=Label (frame, text=rs1[0][1], font=("times new roman",40,'bold') ,bg="tan", fg="black")
                pnamelbl.place(x=80,y=20)
                
                pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
                pricelbl.place(x=80,y=80)
                
                qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' kg', font=("times new roman",25) ,bg="tan", fg="black")
                qwlbl.place(x=80,y=150)
                
                desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
                desclbl.place(x=80,y=220)
                
                imgpath=str(rs1[0][6])
                
                # Create an "Add to Cart" button
                add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                add_to_cart_button.place(x=80,y=420,width=200,height=35)
                
                # Create an main menu button
                main_menu_button = tk.Button(frame, text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white", command=mainuser)
                main_menu_button.place(x=320,y=420,width=200,height=35)
                
                print(imgpath)
                #PLACING IMAGE IN FRAME
                imgs = tk.PhotoImage(file=imgpath)
                img_label = Label(image = imgs)
                img_label.image = imgs
                img_label.place(x=400, y=150)
    
    mainuser = tk.PhotoImage(file="userframe.png")
    img_label = Label(image = mainuser)
    img_label.grid(row=4, column=0)
    img_label.image = mainuser


    frame=Frame(bg="tan")
    frame.place(x=30,y=200, width=1400, height=600)
    #making dictionary with pno as keys and pname as values
    lstpname=[]
    lstpno=[]
    myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
    if myconn.is_connected():
        print("connection successful")
    mycur = myconn.cursor()
    query1 = "SELECT pname FROM product WHERE category='Other Desserts' ORDER BY pcode ASC"
    mycur.execute(query1)
    rs1 = mycur.fetchall()

    for values in rs1:
        lstpname+=values

    query2 = "SELECT pcode FROM product WHERE category='Other Desserts' ORDER BY pcode ASC"
    mycur.execute(query2)
    rs2 = mycur.fetchall()
    nameno={}
    for values in rs2:
        lstpno+=values
    for i in range(len(lstpname)):
        nameno[lstpname[i]] = lstpno[i]
        
    for i in range(0,len(lstpname)):
        product_name = lstpname[i]
        product_button = tk.Button(frame, text=product_name , command=lambda p=product_name : display_product(p))
        product_button.pack(padx=10, pady=5, fill=tk.X)
        
        
'''


    def display_product(p):
    
        if p =='Mango Dessert':
            
            imgcake = tk.PhotoImage(file="mangodessert.png")
            img_label = Label(image = imgcake)
            img_label.grid(row=3, column=0)
            img_label.image = imgcake
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=200, width=800, height=580)
            
            pnamelbl=Label (frame, text=p, font=("times new roman", 40, "bold") ,bg="tan", fg="black")
            pnamelbl.config(anchor="n")
            pnamelbl.pack()
            
            myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
            if myconn.is_connected():
                print("connection successful")
            mycur = myconn.cursor()
            query1 = "SELECT * FROM product WHERE pname='Mango Dessert'"
            mycur.execute(query1)
            rs1 = mycur.fetchall()
            pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
            pricelbl.place(x=80,y=80)
            
            qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' brownies', font=("times new roman",25) ,bg="tan", fg="black")
            qwlbl.place(x=80,y=150)
            
            desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
            desclbl.place(x=80,y=220)
            
            # Create an "Add to Cart" button
            add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
            add_to_cart_button.place(x=80,y=420,width=200,height=35)
            
            # Create an main menu button
            main_menu_button = tk.Button(frame, text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white", command=mainuser)
            main_menu_button.place(x=320,y=420,width=200,height=35)
            

            
            
            
        if p =='Baked Cinnamon Apple Roses':
            
            imgcake = tk.PhotoImage(file="appleroses.png")
            img_label = Label(image = imgcake)
            img_label.grid(row=3, column=0)
            img_label.image = imgcake
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=196, width=800, height=580)
            
            pnamelbl=Label (frame, text=p, font=("times new roman", 40, "bold") ,bg="tan", fg="black")
            pnamelbl.config(anchor="n")
            pnamelbl.pack()
            
            myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
            if myconn.is_connected():
                print("connection successful")
            mycur = myconn.cursor()
            query1 = "SELECT * FROM product WHERE pname='Baked Cinnamon Apple Roses'"
            mycur.execute(query1)
            rs1 = mycur.fetchall()
            pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
            pricelbl.place(x=80,y=80)
            
            qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' cupcakes/muffins', font=("times new roman",25) ,bg="tan", fg="black")
            qwlbl.place(x=80,y=150)
            
            desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
            desclbl.place(x=80,y=220)
            
             # Create an "Add to Cart" button
            add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
            add_to_cart_button.place(x=80,y=420,width=200,height=35)
            
            # Create an main menu button
            main_menu_button = tk.Button(frame, command=mainuser,text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
            main_menu_button.place(x=320,y=420,width=200,height=35)
            

        if p =='Gingerbread House':
            
            imgcake = tk.PhotoImage(file="GingerbreadHouse.png")
            img_label = Label(image = imgcake)
            img_label.grid(row=3, column=0)
            img_label.image = imgcake
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=196, width=800, height=580)
            
            pnamelbl=Label (frame, text=p, font=("times new roman", 40, "bold") ,bg="tan", fg="black")
            pnamelbl.config(anchor="n")
            pnamelbl.pack()
            try:
                myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
                if myconn.is_connected():
                    print("connection successful")
                mycur = myconn.cursor()
                query1 = "SELECT * FROM product WHERE pname='Gingerbread House'"
                mycur.execute(query1)
                rs1 = mycur.fetchall()
                pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
                pricelbl.place(x=80,y=80)
                
                qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' cupcakes/muffins', font=("times new roman",25) ,bg="tan", fg="black")
                qwlbl.place(x=80,y=150)
                
                desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
                desclbl.place(x=80,y=220)
                
                # Create an "Add to Cart" button
                add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                add_to_cart_button.place(x=80,y=420,width=200,height=35)
                
                # Create an main menu button
                main_menu_button = tk.Button(frame, command=mainuser,text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                main_menu_button.place(x=320,y=420,width=200,height=35)
            
            except Exception as e:
                print(e)
        
               
    mainuser = tk.PhotoImage(file="userframe.png")
    img_label = Label(image = mainuser)
    img_label.grid(row=4, column=0)
    img_label.image = mainuser
    
    
    frame=Frame(bg="tan")
    frame.place(x=30,y=200, width=1400, height=600)
    
    
    lstpname=[]
    lstpno=[]
    myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
    if myconn.is_connected():
        print("connection successful")
    mycur = myconn.cursor()
    query1 = "SELECT pname FROM product WHERE category='Other Desserts'"
    mycur.execute(query1)
    rs1 = mycur.fetchall()
    
    for values in rs1:
        lstpname+=values

    query2 = "SELECT pcode FROM product WHERE category='Other Desserts'"
    mycur.execute(query2)
    rs2 = mycur.fetchall()
    nameno={}
    for values in rs2:
        lstpno+=values
    for i in range(len(lstpname)):
        nameno[lstpname[i]] = lstpno[i]
        
    for i in range(0,len(lstpname)):
        product_name = lstpname[i]
        product_button = tk.Button(frame, text=product_name, command=lambda p=product_name: display_product(p))
        product_button.pack(padx=10, pady=5, fill=tk.X)
           
    '''
 
def dispbrowniesuser():
    def display_product(p):

        for ele in lstpname:
            mainuser = tk.PhotoImage(file="userframe.png")
            img_label = Label(image = mainuser)
            img_label.grid(row=4, column=0)
            img_label.image = mainuser
            
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=200, width=1400, height=600)
    
            if ele==p:
                myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
                if myconn.is_connected():
                    print("connection successful")
                mycur = myconn.cursor()
                query1 = "SELECT * FROM product WHERE pname='{}'".format(p)
                mycur.execute(query1)
                rs1 = mycur.fetchall()
                pnamelbl=Label (frame, text=rs1[0][1], font=("times new roman",40,'bold') ,bg="tan", fg="black")
                pnamelbl.place(x=80,y=20)
                
                pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
                pricelbl.place(x=80,y=80)
                
                qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' kg', font=("times new roman",25) ,bg="tan", fg="black")
                qwlbl.place(x=80,y=150)
                
                desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
                desclbl.place(x=80,y=220)
                
                imgpath=str(rs1[0][6])
                
                # Create an "Add to Cart" button
                add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                add_to_cart_button.place(x=80,y=420,width=200,height=35)
                
                # Create an main menu button
                main_menu_button = tk.Button(frame, text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white", command=mainuser)
                main_menu_button.place(x=320,y=420,width=200,height=35)
                
                print(imgpath)
                #PLACING IMAGE IN FRAME
                imgs = tk.PhotoImage(file=imgpath)
                img_label = Label(image = imgs)
                img_label.image = imgs
                img_label.place(x=400, y=150)
    
    mainuser = tk.PhotoImage(file="userframe.png")
    img_label = Label(image = mainuser)
    img_label.grid(row=4, column=0)
    img_label.image = mainuser
    
    
    frame=Frame(bg="tan")
    frame.place(x=30,y=200, width=1400, height=600)
    #making dictionary with pno as keys and pname as values
    lstpname=[]
    lstpno=[]
    myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
    if myconn.is_connected():
        print("connection successful")
    mycur = myconn.cursor()
    query1 = "SELECT pname FROM product WHERE category='Brownies' ORDER BY pcode ASC"
    mycur.execute(query1)
    rs1 = mycur.fetchall()
    
    for values in rs1:
        lstpname+=values

    query2 = "SELECT pcode FROM product WHERE category='Brownies' ORDER BY pcode ASC"
    mycur.execute(query2)
    rs2 = mycur.fetchall()
    nameno={}
    for values in rs2:
        lstpno+=values
    for i in range(len(lstpname)):
        nameno[lstpname[i]] = lstpno[i]
        
    for i in range(0,len(lstpname)):
        product_name = lstpname[i]
        product_button = tk.Button(frame, text=product_name , command=lambda p=product_name : display_product(p))
        product_button.pack(padx=10, pady=5, fill=tk.X)
    '''
        
    def display_product(p):
    
        if p =='White chocolate brownies':
            
            imgcake = tk.PhotoImage(file="whitechocob.png")
            img_label = Label(image = imgcake)
            img_label.grid(row=3, column=0)
            img_label.image = imgcake
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=200, width=800, height=580)
            
            pnamelbl=Label (frame, text=p, font=("times new roman", 40, "bold") ,bg="tan", fg="black")
            pnamelbl.config(anchor="n")
            pnamelbl.pack()
            
            myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
            if myconn.is_connected():
                print("connection successful")
            mycur = myconn.cursor()
            query1 = "SELECT * FROM product WHERE pname='White chocolate brownies'"
            mycur.execute(query1)
            rs1 = mycur.fetchall()
            pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
            pricelbl.place(x=80,y=80)
            
            qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' brownies', font=("times new roman",25) ,bg="tan", fg="black")
            qwlbl.place(x=80,y=150)
            
            desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
            desclbl.place(x=80,y=220)
            
            # Create an "Add to Cart" button
            add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
            add_to_cart_button.place(x=80,y=420,width=200,height=35)
            
            # Create an main menu button
            main_menu_button = tk.Button(frame, text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white", command=mainuser)
            main_menu_button.place(x=320,y=420,width=200,height=35)
            

            
            
            
        if p =='Milk Chocolate Brownies':
            
            imgcake = tk.PhotoImage(file="milkchocob.png")
            img_label = Label(image = imgcake)
            img_label.grid(row=3, column=0)
            img_label.image = imgcake
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=196, width=800, height=580)
            
            pnamelbl=Label (frame, text=p, font=("times new roman", 40, "bold") ,bg="tan", fg="black")
            pnamelbl.config(anchor="n")
            pnamelbl.pack()
            
            myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
            if myconn.is_connected():
                print("connection successful")
            mycur = myconn.cursor()
            query1 = "SELECT * FROM product WHERE pname='Milk Chocolate Brownies'"
            mycur.execute(query1)
            rs1 = mycur.fetchall()
            pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
            pricelbl.place(x=80,y=80)
            
            qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' cupcakes/muffins', font=("times new roman",25) ,bg="tan", fg="black")
            qwlbl.place(x=80,y=150)
            
            desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
            desclbl.place(x=80,y=220)
            
             # Create an "Add to Cart" button
            add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
            add_to_cart_button.place(x=80,y=420,width=200,height=35)
            
            # Create an main menu button
            main_menu_button = tk.Button(frame, command=mainuser,text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
            main_menu_button.place(x=320,y=420,width=200,height=35)
            

        if p =='Kinder Brownies':
            
            imgcake = tk.PhotoImage(file="kinderb.png")
            img_label = Label(image = imgcake)
            img_label.grid(row=3, column=0)
            img_label.image = imgcake
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=196, width=800, height=580)
            
            pnamelbl=Label (frame, text=p, font=("times new roman", 40, "bold") ,bg="tan", fg="black")
            pnamelbl.config(anchor="n")
            pnamelbl.pack()
            try:
                myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
                if myconn.is_connected():
                    print("connection successful")
                mycur = myconn.cursor()
                query1 = "SELECT * FROM product WHERE pname='Kinder Brownies'"
                mycur.execute(query1)
                rs1 = mycur.fetchall()
                pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
                pricelbl.place(x=80,y=80)
                
                qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' cupcakes/muffins', font=("times new roman",25) ,bg="tan", fg="black")
                qwlbl.place(x=80,y=150)
                
                desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
                desclbl.place(x=80,y=220)
                
                # Create an "Add to Cart" button
                add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                add_to_cart_button.place(x=80,y=420,width=200,height=35)
                
                # Create an main menu button
                main_menu_button = tk.Button(frame, command=mainuser,text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                main_menu_button.place(x=320,y=420,width=200,height=35)
            
            except Exception as e:
                print(e)
        if p =='M&M Brownies':
            
            imgcake = tk.PhotoImage(file="m&mb.png")
            img_label = Label(image = imgcake)
            img_label.grid(row=3, column=0)
            img_label.image = imgcake
            
            frame=Frame(bg="tan")
            frame.place(x=30,y=196, width=800, height=580)
            
            pnamelbl=Label (frame, text=p, font=("times new roman", 40, "bold") ,bg="tan", fg="black")
            pnamelbl.config(anchor="n")
            pnamelbl.pack()
            try:
                myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
                if myconn.is_connected():
                    print("connection successful")
                mycur = myconn.cursor()
                query1 = "SELECT * FROM product WHERE pname='M&M Brownies'"
                mycur.execute(query1)
                rs1 = mycur.fetchall()
                pricelbl=Label (frame, text="Price:              "+str(rs1[0][3])+' AED', font=("times new roman",25) ,bg="tan", fg="black")
                pricelbl.place(x=80,y=80)
                
                qwlbl=Label (frame, text="Weight:        "+str(rs1[0][4])+' cupcakes/muffins', font=("times new roman",25) ,bg="tan", fg="black")
                qwlbl.place(x=80,y=150)
                
                desclbl=Label (frame, text="Description:      "+rs1[0][5], font=("times new roman",25) ,bg="tan", fg="black",wraplength=600)
                desclbl.place(x=80,y=220)
                # Create an "Add to Cart" button
                add_to_cart_button = tk.Button(frame, text="Add to Cart",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                add_to_cart_button.place(x=80,y=420,width=200,height=35)
                
                # Create an main menu button
                main_menu_button = tk.Button(frame, command=mainuser,text="Main Menu",font=("Times New Roman",25,"bold"),bd=3,relief=RIDGE,background="tan",fg="black",activeforeground="blue", activebackground="white")
                main_menu_button.place(x=320,y=420,width=200,height=35)
                
            except Exception as e:
                print(e)
                
                
        
        
        
               
    mainuser = tk.PhotoImage(file="userframe.png")
    img_label = Label(image = mainuser)
    img_label.grid(row=4, column=0)
    img_label.image = mainuser
    
    
    frame=Frame(bg="tan")
    frame.place(x=30,y=200, width=1400, height=600)
    
    
    lstpname=[]
    lstpno=[]
    myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
    if myconn.is_connected():
        print("connection successful")
    mycur = myconn.cursor()
    query1 = "SELECT pname FROM product WHERE category='Brownies'"
    mycur.execute(query1)
    rs1 = mycur.fetchall()
    
    for values in rs1:
        lstpname+=values

    query2 = "SELECT pcode FROM product WHERE category='Brownies'"
    mycur.execute(query2)
    rs2 = mycur.fetchall()
    nameno={}
    for values in rs2:
        lstpno+=values
    for i in range(len(lstpname)):
        nameno[lstpname[i]] = lstpno[i]
        
    for i in range(0,len(lstpname)):
        product_name = lstpname[i]
        product_button = tk.Button(frame, text=product_name, command=lambda p=product_name: display_product(p))
        product_button.pack(padx=10, pady=5, fill=tk.X)
            
    print(nameno)
    '''

 
 

#----------------------------------------USER LOGIN-------------------------------  
def userlog():
    def userlogin():
        myconn = mys.connect(host='localhost', user="root",passwd="icecream123", database="bakery")
        if myconn.is_connected():
            print("connection successful")
        mycur = myconn.cursor()
        user=txtuser.get()
        passw=txtpass.get()
        query1 = "SELECT email,password FROM users where email='{}' and password='{}'".format(user,passw)
        mycur.execute(query1)
        rs1 = mycur.fetchone()
        u=rs1[0]
        pw=rs1[1]
        print(rs1)
        if user=="" or passw=="":
            messagebox.showerror("Error","All fields are required!")
            
        elif user==u and passw==pw :
            messagebox.showinfo("LOGIN SUCCESSFUL","The menu is going to open up")
            searchmenu()
            
        else:
            messagebox.showerror("Invalid","Invalid username or password")  
    
    #lightpink3   
    image3 = tk.PhotoImage(file="userloginimg.png")
    img_label = Label(image = image3)
    img_label.grid(row=4, column=0)
    img_label.image = image3
    frame=Frame(bg="white")
    frame.place(x=560,y=175, width=360, height=470)
    
    get_str=Label(text="Get Started",font=("Times New Roman",20,"bold"),fg="black",bg='white')
    get_str.place(x=670,y=300)
    
    
    image2 = tk.PhotoImage(file="loginaccimg.png")
    img_label = Label(image = image2)
    img_label.place(x=720,y=185,width=100,height=100)
    img_label.image = image2
    
    #usernmaelabel and entry field
    username=lbl=Label(frame,text="Username:",font=("Times New Roman",15,"bold"),fg="black",bg="white")
    username.place(x=70,y=155)

    txtuser=ttk.Entry(frame,font=("Times New Roman",15,"bold"))
    txtuser.place(x=40,y=180,width=270)
    
    
    #password and entry field
    password=lbl=Label(frame,text="Password:",font=("Times New Roman",15,"bold"),fg="black",bg="white")
    password.place(x=70,y=225)
    txtpass=ttk.Entry(frame,font=("Times New Roman",15,"bold"))
    txtpass.place(x=40,y=250,width=270)

    
    
    #LOGIN BUTTON
    loginbtn=Button(frame,command=userlogin,text="Login",font=("Times New Roman",15,"bold"),bd=3,relief=RIDGE,background="red",fg="black",activeforeground="blue", activebackground="white")
    loginbtn.place(x=110,y=300,width=120,height=35)
    
    #REGISTER BUTTON
    registerbtn=Button(frame, command=userreg, text="New User Register",font=("Times New Roman",15,"bold"),borderwidth=0,bg="indianred",fg="black",activeforeground="blue", activebackground="white")
    registerbtn.place(x=15,y=350,width=160,height=35)

#--------------------------USER REGISTER------------------------------
def userreg():
    def register_data():
        fname = fname_entry.get()
        lname = txt_lname.get()
        contact = txt_contact.get()
        email = txt_email.get()
        security_q = combo_security_Q.get()
        security_answer = txt_security.get()
        password = txt_pswd.get()
        if fname_entry.get()=="" or txt_email.get()=="" or combo_security_Q.get()=="":
            messagebox.showerror("Error","All fields are required")
            # first message can be anything second is the message that should be shown to the user
            
        elif txt_pswd.get()!=txt_confirm_pswd.get():
            messagebox.showerror("Error","Passord give in password and confirm password fields must match")
        
        else:
            #messagebox.showinfo("Success","Welcome to Le Patisserie!")
            conn=mys.connect(host='localhost',user='root',password='icecream123',database="bakery")
            mycur=conn.cursor()
            value=(txt_email.get())
            query=("select * from users where email='{}'".format(value))
            
            mycur.execute(query)
            row=mycur.fetchone()
            if row!=None:
                messagebox.showerror("Error", "User already exists, please try another email")
            else:
                query = "INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values = (fname, lname, contact, email, security_q, security_answer, password)
                mycur.execute(query, values)
                #mycur.execute("insert into users values('{}','{}','{}','{}','{}','{}','{}')".format(fname_entry.get(),txt_lname.get(),txt_contact.get(),txt_email.get(),combo_security_Q.get(),txt_security.get(),txt_pswd.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered successfully! Please login to your account by clicking the login button")     
        


    #---------------------main frame--------------------------
    frame=Frame(bg="tan")
    frame.place(x=400,y=150, width=700, height=550)
    register_lbl=Label(frame, text="REGISTER HERE", font=("times new roman",35, "bold"), fg= "black",bg="tan")
    register_lbl.place(x=20, y=20)

    #--------------------label and entry--------------------------
    
    #--------------------row1
    fname=Label (frame, text="First Name", font=("times new roman", 15, "bold") ,bg="tan", fg="black")
    fname.place (x=50, y=100)
    fname_entry=ttk.Entry(frame, textvariable=StringVar(),font=("times new roman", 15, "bold"))
    fname_entry.place (x=50,y=130, width=250)
    
    l_name=Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="tan", fg="black")
    l_name.place (x=370, y=100)
    
    txt_lname=ttk. Entry(frame, textvariable=StringVar(),font=("times new roman", 15))
    txt_lname.place(x=370, y=130, width=250)
    
    
    #--------------------row2
    contact=Label (frame, text="Contact", font=("times new roman", 15, "bold") ,bg="tan", fg="black")
    contact.place (x=50, y=170)
    
    txt_contact=ttk. Entry(frame, textvariable=StringVar(),font=("times new roman", 15))
    txt_contact.place(x=50, y=200, width=250)
    
    email=Label (frame, text="Email", font=("times new roman", 15, "bold") ,bg="tan", fg="black")
    email.place (x=370, y=170)
    
    txt_email=ttk. Entry(frame, textvariable=StringVar(),font=("times new roman", 15))
    txt_email.place(x=370, y=200, width=250)
    
    
    #------------row3
    security_Q=Label (frame, text="Security Question", font=("times new roman", 15, "bold") ,bg="tan", fg="black")
    security_Q.place(x=50, y=240)
    combo_security_Q=ttk.Combobox(frame,textvariable=StringVar(), font=("times new roman", 15, "bold"), state="readonly")   #mode read only
    combo_security_Q["values"]=("Select","Your Birth Place","Your Partner's name","Your Pet's Name")
    combo_security_Q.place(x=50, y=270,width=250)
    combo_security_Q.current(0)

    
    security_A=Label(frame,text="Security Answer", font=("times new roman",15, "bold"),bg="tan", fg="black")
    security_A. place(x=370, y=240)
    txt_security=ttk.Entry(frame, textvariable=StringVar(), font=("times new roman", 15))
    txt_security.place(x=370, y=270 ,width=250)  

    
    
    #------------------row4
    pswd=Label(frame,text="Password " , font=("times new roman", 15, "bold"), bg="tan", fg="black")
    pswd.place(x=50,y=310)
    
    txt_pswd=ttk.Entry(frame, textvariable=StringVar(), font=("times new roman", 15))
    txt_pswd.place (x=50,y=340 ,width=250)
    
    confirm_pswd=Label (frame, text= "Confirm Password", font=("times new roman", 15, "bold"),bg="tan" , fg="black")
    confirm_pswd.place(x=370,y=310)
    
    txt_confirm_pswd=ttk.Entry(frame, textvariable=IntVar(), font=("times new roman", 15))
    txt_confirm_pswd.place(x=370,y=340,width=250)
    
    
    
    #--------------Buttons---------
#     img=Image.open("registerbn.jpeg")
#     img=img.resize((200, 55), Image.LANCZOS)
#     photoimage=ImageTk.PhotoImage(img)
#     b1=Button(frame, image=photoimage, command=register_data,borderwidth=0,cursor="hand2", font=("times new roman", 15, "bold"), fg="black")
#     b1.place(x=50, y=420, width=200)
#     
#     img1=Image.open("login button.png")
#     img1=img1.resize((200, 45) , Image.LANCZOS)
#     photoimage1=ImageTk.PhotoImage(img1)
#     b1=Button(frame, image=photoimage1,borderwidth=0,cursor="hand2", font=("times new roman", 15, "bold"), fg="black")
#     b1.place(x=380,y=420, width=200)
#     
    loginbtn=Button(frame,command=userlog,text="Login",font=("Times New Roman",15,"bold"),bd=3,relief=RIDGE,background="red",fg="black",activeforeground="blue", activebackground="white")
    loginbtn.place(x=370,y=420,width=120,height=35)
    
    registerbtn=Button(frame, command=register_data, text="Register",font=("Times New Roman",15,"bold"),borderwidth=0,bg="indianred",fg="black",activeforeground="blue", activebackground="white")
    registerbtn.place(x=50,y=420,width=160,height=35)

    

#---------------------------------------------MAIN SCREEN------------------------------    
def loginscr():
#     root = tk.Tk()
#     root.geometry("1550x800") 
#     # Create a photoimage object of the image in the path
#     image1 = Image.open("mainpage.png")
#     test = ImageTk.PhotoImage(image1)
# 
#     label1 = tk.Label(image=test)
#     label1.image = test
# 
#     # Position image
#     label1.place(x=0, y=0)
# 
#     Button(image = photo) # Line required to prevent python's garbage dump function
#     Button(root, image = photo, fg = 'black', bg = 'black').place(x = 0, y = 0)

    root = tk.Tk()
    root.title('Our Bakeshop')
    image3 = tk.PhotoImage(file="mainpage.png")
    img_label = Label(image = image3)
    img_label.grid(row=4, column=0)
    img_label.image = image3

    btnlogin = tk.Button(root, text ="Admin Login", bg='thistle1',font = ("Times New Roman Bold", 20), command = adlog)
    btnlogin.place(x = 190, y = 422, width = 160)
    btnclear = tk.Button(root, text ="User Login", bg='thistle1',font = ("Times New Roman Bold", 20), command=userlog)
    btnclear.place(x = 525, y = 422, width = 160)
    root.mainloop()
    
    
loginscr()


