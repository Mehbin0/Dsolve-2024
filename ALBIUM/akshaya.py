from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as s
con= s.connect(host='localhost',user='root',password='1234')
c=con.cursor()
c.execute("CREATE DATABASE IF NOT EXISTS TEACHER;")
c.execute("USE TEACHER;")
c.execute("CREATE TABLE IF NOT EXISTS T_details(TEACHER_ID INTEGER NOT NULL , TEACHER_NAME VARCHAR(50) NOT NULL,TEACHER_AGE INT NOT NULL , DEPARTMENT VARCHAR(50),ADDRESS VARCHAR(50) , PHONE_NO VARCHAR(10));")

root=Tk()
root.title("LOGIN")
root.geometry("960x435")
root.iconbitmap('Med.ico')
root.configure(bg="#f7dff4")
root.resizable(False,False)



def register_tec():
    ded1=Toplevel(root)
    ded1.title('REGISTER TEACHER')
    ded1.geometry('960x435')
    ded1.iconbitmap('Med.ico')
    ded1.config(bg='#ba95a9')
    ded1.resizable(False,False)
    img=PhotoImage(file="HOS1.png")
    Label(ded1,image=img,bg='White').place(x=1,y=1)

    head=Label(ded1,text='Regsister Teacher',bg='#753700',fg='#FFB012',font=("Times", 24, "bold italic"))
    head.place(x=350,y=20)

    def enter_(e):
        did.delete(0,'end')
    def exit_(e):
        id_=did.get()
        if id_=='':
            did.insert(0,'Teacher id')

    did=Entry(ded1,width=39,fg='black',border=0,bg='#fff0f8',font=('canela',10,'bold'))
    did.place(x=325,y=130)
    did.insert(0,'Teacher id')
    did.bind('<FocusIn>',enter_)
    did.bind('<FocusOut>',exit_)

    def enter_(e):
        dn.delete(0,'end')
    def exit_(e):
        name=dn.get()
        if name=='':
            dn.insert(0,'Teacher Name')
    dn=Entry(ded1,width=39,fg='black',border=0,bg='#fce8f3',font=('canela',10,'bold'))
    dn.place(x=325,y=155)
    dn.insert(0,'Teacher name')
    dn.bind('<FocusIn>',enter_)
    dn.bind('<FocusOut>',exit_)

    def enter_(e):
        da.delete(0,'end')
    def exit_(e):
        age=da.get()
        if age=='':
            da.insert(0,'Teacher age ')

    da=Entry(ded1,width=39,fg='black',border=0,bg='#fff0f8',font=('canela',10,'bold'))
    da.place(x=325,y=180)
    da.insert(0,'Teacher age')
    da.bind('<FocusIn>',enter_)
    da.bind('<FocusOut>',exit_)

    def enter_(e):
        dep.delete(0,'end')
    def exit_(e):
        dy=dep.get()
        if dy=='':
            dep.insert(0,'Department')

    dep=Entry(ded1,width=39,fg='black',border=0,bg='#fce8f3',font=('canela',10,'bold'))
    dep.place(x=325,y= 90)
    dep.insert(0,'Department')
    dep.bind('<FocusIn>',enter_)
    dep.bind('<FocusOut>',exit_)

    def enter_(e):
        add.delete(0,'end')
    def exit_(e):
        ads=add.get()
        if ads=='':
            add.insert(0,'Address')

    add=Entry(ded1,width=39,fg='black',border=0,bg='#fce8f3',font=('Bahnschrift',10,'bold'))
    add.place(x=325,y=210)
    add.insert(0,'Address')
    add.bind('<FocusIn>',enter_)
    add.bind('<FocusOut>',exit_)

    def enter_(e):
        phn.delete(0,'end')
    def exit_(e):
        pno=phn.get()
        if pno=='':
            phn.insert(0,'Phone no')

    phn=Entry(ded1,width=39,fg='black',border=0,bg='#fce8f3',font=('Bahnschrift',10,'bold'))
    phn.place(x=325,y=205)
    phn.insert(0,'Phone no')
    phn.bind('<FocusIn>',enter_)
    phn.bind('<FocusOut>',exit_)

    def sub_2():
        c1=con.cursor()
        d_id=did.get()
        d_nam=dn.get()
        d_age=da.get()
        de_p=dep.get()
        adss=add.get()
        phno=phn.get()
        que1="INSERT INTO T_details(TEACHER_ID,TEACHER_NAME,TEACHER_AGE,DEPARTMENT, ADDRESS, PHONE_NO) VALUES(%s,%s,%s,%s,%s,%s);"
        c1.execute(que1,(d_id,d_nam,d_age,de_p,adss,phno))
        con.commit()

    Button(ded1,width=38,pady=5,text='SUBMIT',bg='#fce8f3',fg='#900C3F',border=3,command=sub_2).place(x=324,y=311)

    def deta1():
        
        dod2=Toplevel(root)
        dod2.title('Table')
        dod2.geometry("920x435")
        dod2.iconbitmap('Med.ico')
        dod2.configure(bg='#fce8f3')
        dod2.resizable(False,False)

        img=PhotoImage(file='HOS1.png')
        Label(dod2,image=img,bg='white').place(x=0,y=0)

        colum=('TEACHER_ID','TEACHER_NAME','TEACHER_AGE','DEPARTMENT','ADDRESS','PHONE_NO')
        treeview=ttk.Treeview(dod2,height=10,show= 'headings', column= colum )

        treeview.column('TEACHER_ID',width=100,anchor=CENTER)
        treeview.column('TEACHER_NAME',width=100,anchor=CENTER)
        treeview.column('TEACHER_AGE',width=100,anchor=CENTER)
        treeview.column('DEPARTMENT',width=100,anchor=CENTER)
        treeview.column('ADDRESS',width=100,anchor=CENTER)
        treeview.column('PHONE_NO',width=100,anchor=CENTER)

        treeview.heading('TEACHER_ID',text='Teacher ID')
        treeview.heading('TEACHER_NAME',text='Teacher Name')
        treeview.heading('TEACHER_AGE',text='Teacher Age')
        treeview.heading('DEPARTMENT', text='Department')
        treeview.heading('ADDRESS', text='Address')
        treeview.heading('PHONE_NO',text='Phone No')

        treeview.pack(side=BOTTOM,fill=BOTH)
        

        c1=con.cursor()
        c1.execute('SELECT * FROM T_details')
        k=c1.fetchall()
        i=1
        for m in k :
            treeview.insert('',i,values=(m[0],m[1],m[2],m[3],m[4],m[5]))
            i+=1
        dod2.mainloop()

    Button(ded1,width=38,pady=5,text='DETAILS',bg='#fce8f3',fg='#900C3F',border=3,command=deta1).place(x=324,y=350)
    ded1.mainloop()



def signin():
    username=user.get()
    password=pas.get()

    if username=='host8435' and password=='Hos_t':
        scr=Toplevel(root)
        scr.title("Module")
        scr.geometry('920x435')
        scr.iconbitmap('Med.ico')
        scr.config(bg='white')
        scr.resizable(False,False)

        img=PhotoImage(file="HOS1.png")
        Label(scr,image=img,bg='White').place(x=0,y=0)
        
        head=Label(scr,text='Welcome to teacher registration',bg='#753700',fg='#FFB012',font=('Rockwell',33))
        head.place(x=35,y=20)
        
       
        Button(scr,width=39,pady=5,text='TEACHER REGISTRATION',bg='#FFC576',fg='#900C3F',border=3,command=register_tec).place(x=325,y=210)
        scr.mainloop()

img=PhotoImage(file="HOS1.png")
Label(root,image=img,bg='White').place(x=0,y=0)



frame=Frame(root,width=275,height=275,bg="#F1F1F1")
frame.place(x=325,y=100)

heading=Label(frame,text='Sign in',fg='#009BFF',bg='#F1F1F1',font=('Rockwell',30,'bold'))
heading.place(x=70,y=15)

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
        
user=Entry(frame,width=28,fg='black',border=0,bg='#009BFF',font=('Bahnschrift',10,'bold'))
user.place(x=40,y=110)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=198,height=1,bg='black').place(x=40,y=127)

def on_enter(e):
    pas.delete(0,'end')

def on_leave(e):
    name=pas.get()
    if name=='':
        pas.insert(0,'Password')

def show_password():
    if pas.cget('show')=='*':
        pas.config(show='')
    else:
        pas.config(show='*')

pas=Entry(frame,show='*',width=28,fg='black',border=0,bg='#009BFF',font=('Bahnschrift',10,'bold'))
pas.place(x=40,y=150)
pas.insert(0,'Password')
pas.bind('<FocusIn>',on_enter)
pas.bind('<FocusOut>',on_leave)

check_button= Checkbutton(root, text='Show Password',command=show_password)
check_button.place(x=410,y=325)

Frame(frame,width=198,height=1,bg='black').place(x=40,y=167)

Button(frame,width=20,pady=6,text='Sign in',bg='#009BFF',fg='#F1F1F1',border=0,command=signin).place(x=65,y=190)

root.mainloop()
