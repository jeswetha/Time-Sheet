from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector
from operator import itemgetter
import tkinter.messagebox as m
import math
import datetime
import time
import pandas as pd
from flask_mail import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mainWindow=Tk()
mainWindow.title("Employee dash board")
mainWindow.geometry("500x500")

bixText=Label(text="Employee Dash Board", font="Verdana 20 bold")
bixText.place(x=50,y=80)

def Register():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="employee")
    mycursor = mydb.cursor()

    registerWindow = Tk()
    registerWindow.title("Register User")
    registerWindow.geometry("400x400")

    bixText = Label(registerWindow,text="Registration Form", font="Verdana 20 bold")
    bixText.place(x=50, y=40)

    name=Label(registerWindow, text="Name")
    name.place(x=90,y=100)
    email=Label(registerWindow,text="Email")
    email.place(x=90,y=140)
    password=Label(registerWindow,text="Password")
    password.place(x=90,y=180)
    repassword=Label(registerWindow,text="Confirm Password")
    repassword.place(x=80,y=220)

    e1=Entry(registerWindow)
    e1.place(x=180,y=100)

    e2 = Entry(registerWindow)
    e2.place(x=180, y=140)
    e3 = Entry(registerWindow, show="*")
    e3.place(x=180, y=180)
    e4 = Entry(registerWindow, show="*")
    e4.place(x=180, y=220)

    def clearEntryBox():
        e1.delete(first=0,last=100)
        e2.delete(first=0,last=100)
        e3.delete(first=0,last=100)
        e4.delete(first=0,last=100)
    def error():
        m.showerror(title="error",message="Password not same")

    def insert():
        email=e2.get()
        print(email)
        sql = "select * from emp"
        result = pd.read_sql_query(sql, mydb)
        email1 = result['email'].values
        print(email1)
        print(email1)
        if email in email1:
            m.showinfo(title="error", message="Email Already exists")
        elif(e1.get()=="" or email=="" or e3.get()=="" or e4.get()==""):
            m.showwarning(title="Error", message="All fields are required")
        elif e3.get() == e4.get():
            insert = ("insert into emp(name,email,pwd,cpwd) values(%s,%s,%s,%s)")
            values = [e1.get(), e2.get(), e3.get(), e4.get()]
            mycursor.execute(insert, values)
            mydb.commit()
            clearEntryBox()
            m.showinfo(title="Done", message="Account created")
        else:
            m.showinfo(title="error", message="Somthing missing")


    log1 = Button(registerWindow, cursor="hand2", text="Login Here", font=("times new roman", 10,"bold"), fg="green",command=Login)
    log1.place(x=245, y=260)

    register= Button(registerWindow,text="Register",fg="green",command=insert)
    register.place(x=175,y=260)

    btnExit = Button(registerWindow, text="EXIT WINDOW", bg="pink", command=registerWindow.destroy)
    btnExit.place(x=200, y=300)


def Login():
    print("hello")

    LoginWindow = Tk()
    LoginWindow.title("Login User")
    LoginWindow.geometry("400x400")
    bixText = Label(LoginWindow, text="Login Form", font="Verdana 20 bold")
    bixText.place(x=90, y=80)

    otp = Label(LoginWindow, text="Emp_ID")
    otp.place(x=90, y=140)
    password = Label(LoginWindow, text="Password")
    password.place(x=90, y=180)

    e2 = Entry(LoginWindow)
    e2.place(x=180, y=140)
    e3 = Entry(LoginWindow, show="*")
    e3.place(x=180, y=180)

    def clearEntryBox():

        e2.delete(first=0,last=100)
        e3.delete(first=0,last=100)

    def error():
        m.showerror(title="error",message="Password not currect")

    def login1():
                otp=e2.get()
                print(otp)
                pwd=e3.get();
                print(pwd)
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="",
                    database="employee")
                mycursor = mydb.cursor()
                print("database connected")
                mycursor.execute("select * from emp where otp=%s and pwd=%s ",(otp,pwd))
                print("********")
                row=mycursor.fetchone()
                print(row)
                if row==None:
                    m.showerror(title="error", message="Invalid Employee Id & password")
                else:
                    m.showinfo(title="success", message="Login Successfully")
                    empWindow = Tk()

                    empWindow.title("Employee Work Report")
                    empWindow.geometry("500x500")

                    bixText = Label(empWindow,text="Employee Work Sheet", font="Verdana 20 bold")
                    bixText.place(x=120, y=50)

                    name = Label(empWindow, text="Email")
                    name.place(x=90, y=100)
                    email = Label(empWindow, text="In Time")
                    email.place(x=90, y=140)
                    password = Label(empWindow, text="Out Time")
                    password.place(x=90, y=180)
                    repassword = Label(empWindow, text="Today's Work")
                    repassword.place(x=80, y=220)

                    a1 = Entry(empWindow)
                    a1.place(x=180, y=100)

                    a2 = Entry(empWindow)
                    a2.place(x=180, y=140)
                    a3 = Entry(empWindow)
                    a3.place(x=180, y=180)
                    a4 = Entry(empWindow)
                    a4.place(x=180, y=220)

                    def clearEntryBox():
                        a1.delete(first=0, last=100)
                        a2.delete(first=0, last=100)
                        a3.delete(first=0, last=100)
                        a4.delete(first=0, last=100)


                    def submit():

                        in_time=a2.get()
                        # print(type(in_time))
                        out_time=a3.get()
                        n = datetime.datetime.now()
                        print(n)
                        d = n.strftime("%d/%m/%Y")
                        print(d)
                        # print(type(out_time))
                        # print(in_time.split(':'))
                        # print(type(in_time.split(':')[0]))
                        # print(in_time.split(':')[1])
                        in_min=int(in_time.split(':')[0])*60
                        in_min=in_min+int(in_time.split(':')[1])

                        out_time.split(':')
                        out_min = int(out_time.split(':')[0]) * 60
                        out_min = out_min+int(out_time.split(':')[1])
                        work_time=out_min-in_min-60
                        work_time1=math.floor(work_time/60)
                        work_time2=work_time%60
                        w_full=str(work_time1)+':'+str(work_time2)

                        if work_time > 480:
                            e_time=work_time-480
                        else:
                            e_time=0

                        e_time1=math.floor(e_time/60)
                        e_time2=e_time%60
                        e_full=str(e_time1)+':'+str(e_time2)

                        now = datetime.datetime.now()
                        print(now.strftime("%A"))
                        day=now.strftime("%A")

                        import holidays
                        holiday_list=holidays.CountryHoliday('IN',int(now.strftime('%Y')))

                        curr=now.strftime('%Y-%m-%d')
                        if holiday_list.get(curr)==None:
                            if day in ['Sunday', 'Saturday']:
                                m.showinfo(title="Error", message="You can not submit the time sheet on a holiday")
                            else:
                                insert = ("insert into report(intime,outtime,etime,email,work,day,date) values(%s,%s,%s,%s,%s,%s,%s)")
                                values = [in_time, out_time, e_full, a1.get(), a4.get(), day,d]
                                mycursor.execute(insert, values)
                                mydb.commit()
                                clearEntryBox()
                                m.showinfo(title="Done", message="Successfully submitted your work status")
                        else:
                            m.showinfo(title="Error", message="You can not submit the time sheet on a holiday")

                    register = Button(empWindow, text="Submit", fg="green", command=submit)
                    register.place(x=175, y=260)

                    btnExit = Button(empWindow, text="EXIT WINDOW", bg="red", command=empWindow.destroy)
                    btnExit.place(x=350, y=350)

                    empWindow.mainloop()
                    m.showinfo(title="Sucess", message="Welcome")


    register = Button(LoginWindow, text="Login", fg="white",bg="black" ,command=login1)
    register.place(x=170, y=220)

    btnExit = Button(LoginWindow, text="EXIT WINDOW", bg="red", command=LoginWindow.destroy)
    btnExit.place(x=280, y=350)


def manager():
    print("hello")

    ManagerWindow = Tk()
    ManagerWindow.title("Manager Login")
    ManagerWindow.geometry("400x400")
    bixText = Label(ManagerWindow,text="Manager Login Page", font="Verdana 20 bold")
    bixText.place(x=50, y=60)

    email = Label(ManagerWindow, text="Email")
    email.place(x=90, y=140)
    password = Label(ManagerWindow, text="Password")
    password.place(x=90, y=180)

    e2 = Entry(ManagerWindow)
    e2.place(x=180, y=140)
    e3 = Entry(ManagerWindow, show="*")
    e3.place(x=180, y=180)

    def clearEntryBox():

        e2.delete(first=0,last=100)
        e3.delete(first=0,last=100)

    def error():
        m.showerror(title="error",message="Password not currect")

    def manageLog():
        email=e2.get()
        print(email)
        pwd=e3.get();
        print(pwd)
        if email=="" or pwd=="":
            m.showerror(title="Error", message="All fields are required")
        elif email=="admin@gmail.com" and pwd=="admin":
            m.showinfo(title="Success", message="Welcome Manager")
            managerWindow= Tk()

            managerWindow.title("Manager dash board")
            managerWindow.geometry("650x500")

            bixText = Label(managerWindow, text="Registered Employees Details", font="Verdana 20 bold")
            bixText.place(x=60, y=75)

            frm1=Frame(managerWindow)
            frm1.pack(side=tk.LEFT,padx=20)
            tv=ttk.Treeview(frm1,columns=(1,2,3), show="headings",height="5")
            tv.pack()

            tv.heading(1,text="S.No")
            tv.heading(2,text="Employee Name")
            tv.heading(3,text="Email")

            mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd="",
                        database="employee")
            mycursor = mydb.cursor()
            print("database connected")

            sql="select id,name,email from emp where status='pending'"
            mycursor.execute(sql)
            rows=mycursor.fetchall()
            total=mycursor.rowcount
            print("Total data entries:"+str(total))

            for i in rows:
                tv.insert('','end', values=i)
                managerWindow.resizable(False, False)
                approval = Button(managerWindow, text="Approval", fg="white",bg="black", command=Approval)
                approval.place(x=235, y=330)
                managerWindow.mainloop()
            work = Button(managerWindow, text="View Work Sheet", fg="white",bg="blue", command=View_Work_Sheet)
            work.place(x=305, y=370)

            btnExit = Button(managerWindow, text="EXIT WINDOW", bg="pink", command=managerWindow.destroy)
            btnExit.place(x=420, y=370)



        else:
            m.showinfo(title="Error", message="Invalid Email And Password")

    register = Button(ManagerWindow, text="Login", fg="white",bg="green", command=manageLog)
    register.place(x=175, y=210)

    btnExit = Button(ManagerWindow, text="EXIT WINDOW", bg="green", command=ManagerWindow.destroy)
    btnExit.place(x=300, y=350)


def Approval():

    approvalWindow = Tk()

    approvalWindow.title("Manager dash board")
    approvalWindow.geometry("400x400")

    bixText = Label(approvalWindow,text="Employee data", font="Verdana 20 bold")
    bixText.place(x=90, y=40)

    id = Label(approvalWindow, text="Id")
    id.place(x=120, y=140)

    id1 = Entry(approvalWindow)
    id1.place(x=170, y=140)

    def search():
        id=id1.get()
        print(type(id))
        searchWindow=Tk()
        searchWindow.title("Approval a record")
        searchWindow.geometry("400x400")
        bixText = Label(searchWindow, text="Employee Details", font="Verdana 20 bold")
        bixText.place(x=90, y=40)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="employee")
        mycursor = mydb.cursor()
        print("database connected")

        mycursor.execute("select * from emp where id=" + id)
        # pd.read_sql_query("select * from emp where id="+(str(id)),mydb)

        print("********")
        row = mycursor.fetchall()
        mydb.commit()
        print(row)

        id = Label(searchWindow, text="Id")
        id.place(x=90, y=100)
        name = Label(searchWindow, text="Name")
        name.place(x=90, y=140)
        email = Label(searchWindow, text="Email")
        email.place(x=90, y=180)

        a1 = Entry(searchWindow)
        a1.place(x=180, y=100)

        a2 = Entry(searchWindow)
        a2.place(x=180, y=140)
        a3 = Entry(searchWindow)
        a3.place(x=180, y=180)
        for rows in row:
            a1.insert(0,rows[0])
            a2.insert(0,rows[1])
            a3.insert(0,rows[2])
        print_records=''
        # for rows in row:
        #     print_records+=str(rows[0])+""+str(rows[1])+""+str(rows[1])
        #     print(print_records)
        def send():
            email = row[0][2]
            id=row[0][0]
            print(email)

            n = datetime.datetime.now()
            print(n)
            d = n.strftime("%d/%m/%Y")
            print(d)
            from random import getrandbits
            import random
            status = "Accepted"
            hash = random.getrandbits(20)
            print(hash)
            otp = 'Your Employee Id is'
            msg="This is an automatically generated mail. Please do not reply to this mail."

            mail_content = otp + ' ' + str(hash) + ' on ' + d+'\n'+msg
            sender_address = ''
            sender_pass = ''
            receiver_address = email
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = 'Employee Dash Board'

            message.attach(MIMEText(mail_content, 'plain'))
            session = smtplib.SMTP('smtp.gmail.com', 587)
            session.starttls()
            session.login(sender_address, sender_pass)
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
            m.showinfo(title="Sucess", message="Registration accepted")

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="employee"
            )
            mycursor = mydb.cursor()
            mycursor.execute("update emp set status='Accepted', otp=%s where id=%s",(hash, id))
            mydb.commit()

        work = Button(searchWindow, text="Send", fg="green", command=send)
        work.place(x=225, y=230)
        print("welcome")

    work = Button(approvalWindow, text="Search", fg="green", command=search)
    work.place(x=195, y=180)

    btnExit = Button(approvalWindow, text="EXIT WINDOW", bg="red", command=approvalWindow.destroy)
    btnExit.place(x=420, y=370)



def View_Work_Sheet():
    viewWindow = Tk()

    viewWindow.title("Manager dash board")
    viewWindow.geometry("1200x500")

    bixText = Label(viewWindow,text="Employees Work Status", font="Verdana 20 bold")
    bixText.place(x=330, y=80)

    frm1 = Frame(viewWindow)
    frm1.pack(side=tk.LEFT)
    tv = ttk.Treeview(frm1, columns=(1, 2, 3, 4, 5, 6), show="headings", height="5")
    tv.pack()

    tv.heading(1, text="In Time")
    tv.heading(2, text="Out Time")
    tv.heading(3, text="Over Time")
    tv.heading(4, text="Email")
    tv.heading(5, text="Work")
    tv.heading(6, text="Date")

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="employee")
    mycursor = mydb.cursor()
    print("database connected")
    sql = "select intime,outtime,etime,email,work,date from report where status='pending'"
    mycursor.execute(sql)
    rows = mycursor.fetchall()
    total = mycursor.rowcount
    print("Total data entries:" + str(total))

    for i in rows:
        tv.insert('', 'end', values=i)
        viewWindow.resizable(False, False)

    def emp_work():
        workWindow = Tk()

        workWindow.title("Employee Work Sheet")
        workWindow.geometry("600x300")

        bixText = Label(workWindow,text="Send Acceptence Mail To Employee", font="Verdana 20 bold")
        bixText.place(x=40, y=70)

        email = Label(workWindow, text="Emp_Email")
        email.place(x=120, y=140)

        id1 = Entry(workWindow)
        id1.place(x=210, y=140)

        def sendback():
            email =id1.get()
            print(email)

            n = datetime.datetime.now()
            print(n)
            d = n.strftime("%d/%m/%Y")
            print(d)
            status='Accepted'
            from random import getrandbits
            import random
            otp = 'Work status acceted '
            msg = "This is an automatically generated mail. Please do not reply to this mail."
            mail_content = otp + ' on ' + d+'\n'+msg
            sender_address = ''
            sender_pass = ''
            receiver_address = email
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = 'Employee Dash Board'

            message.attach(MIMEText(mail_content, 'plain'))
            session = smtplib.SMTP('smtp.gmail.com', 587)
            session.starttls()
            session.login(sender_address, sender_pass)
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
            m.showinfo(title="Sucess", message="Employee work status accepted")
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="employee"
            )
            mycursor = mydb.cursor()
            mycursor.execute("update report set status=%s where email=%s", (status,email))
            mydb.commit()

        work = Button(workWindow, text="Send Mail", fg="green", command=sendback)
        work.place(x=205, y=190)
        print("welcome")

        btnExit = Button(workWindow, text="EXIT WINDOW", bg="red", command=workWindow.destroy)
        btnExit.place(x=420, y=370)

    emp_work = Button(viewWindow, text="Work Status", fg="green", command=emp_work)
    emp_work.place(x=590, y=330)

goToLogin = Button(mainWindow,text="Employee", fg="green",font="Verdana 10 bold", command=Register)
goToLogin.place(x=120,y=200)
goToRegister = Button(mainWindow,text="Manager", fg="green",font="Verdana 10 bold", command=manager)
goToRegister.place(x=230,y=200)

btnExit= Button(mainWindow,text="EXIT WINDOW", bg="yellow", command=mainWindow.destroy)
btnExit.place(x=180,y=270)

mainWindow.mainloop()



