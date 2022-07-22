from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import customtkinter
from face_capture import facecap


class attendance:

    def __init__(self, root):
        self.root=root
        self.root.state('zoomed')
        self.root.title("Attendance System")
        self.root.overrideredirect(True)
        self.root.iconbitmap("img\\saslog.ico")

        self.EMPLOYEE_ID = StringVar()
        self.NAME = StringVar()
        self.DEPARTMENT = StringVar()
        self.DESIGNATION = StringVar()
        self.JOINING_MONTH = StringVar()
        self.DOB = StringVar()
        self.GENDER = StringVar()
        self.EMAIL = StringVar()
        self.MARTIAL_STATUS = StringVar()
        self.NATIONALITY = StringVar()
        self.BLOOD_GROUP = StringVar()
        self.PHONE_NUMBER = StringVar()
        self.ADDRESS = StringVar()

        img = Image.open("img\\pexels-ben-mack-6775241.jpg")
        img = img.resize((1530, 790), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        fstlbl = Label(self.root, image=self.photoimg)
        fstlbl.place(x=0, y=0, width=1530, height=990)

        img1 = Image.open("img\\6b77beffb8d54b09b7414bd72c07342e.png")
        img1 = img1.resize((105, 105), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        sndlbl = Label(self.root, image=self.photoimg1)
        sndlbl.place(x=0, y=0, width=105, height=105)

        logi_in = Label(self.root, text="SMART AUTHORIZING SYSTEM", font=("Tahoma", 20, "bold"), fg="#f5f5f5",bg="#263238", width=80, height=3, bd=2)
        logi_in.place(x=100, y=0)


        head = Label(self.root, text="EMPLOYEE DETAILS", font=("Tahoma", 25, "bold"), bg="#263238", fg="white")
        head.place(x=0, y=120, width=1530, height=40)
        back=customtkinter.CTkButton(self.root, text="Back", text_font=("Tahoma", 10, "bold"),bg_color="#263238",fg_color="#64b5f6",command=root.destroy)
        back.place(x=1200,y=126)

        frame = Frame(self.root, bd=2)
        frame.place(x=0, y=175, width=1530, height=650)

        RFrame1 = LabelFrame(self.root, bd=2, relief=RIDGE, font=("Tahoma", 10, "bold"),
                             bg="#263238")
        RFrame1.place(x=0, y=180, width=1600, height=900)

        RFrame1 = LabelFrame(RFrame1, bd=2, relief=RIDGE, text="Employee Personal Details",font=("tahoma", 12, "bold"),
                             bg= '#515B60',fg='black')
        RFrame1.place(x=0, y=10, width=1600, height=900)


        RFrame1 = LabelFrame(RFrame1, bd=2, relief=RIDGE, background="white")
        RFrame1.place(x=5, y=5, width=1550, height=265)

        Dptlbl = Label(RFrame1, text="Department :",font=("tahoma", 10, "bold"),background="white")
        Dptlbl.grid(row=0, column=0, padx=5, sticky=W)

        Dptcom = ttk.Combobox(RFrame1, textvariable=self.DEPARTMENT, font=("Tahoma", 10), state="readonly", width=18,cursor="hand2")
        Dptcom["values"] = ("Choose Department", "IT", "Management", "Service")
        Dptcom.current(0)
        Dptcom.grid(row=0, column=1, padx=5, pady=10, sticky=W)
        ##
        Dptlbl1 =Label(RFrame1, text="Designation :",font=("tahoma", 10, "bold"),background="white")
        Dptlbl1.grid(row=0, column=2, padx=5, sticky=W)

        Dptcom1 = ttk.Combobox(RFrame1, textvariable=self.DESIGNATION, font=("Tahoma", 10), state="readonly", width=18,cursor="hand2")
        Dptcom1["values"] = (
            "Choose Designation", "Senior Manager", "Asst Manager", "HR", "TL", "Project Manager", "Developer",
            "Tester", "Trainee")
        Dptcom1.current(0)
        Dptcom1.grid(row=0, column=3, padx=5, pady=10, sticky=W)
        ##
        Dptlbl2 = Label(RFrame1, text="Joining Month :",font=("tahoma", 10, "bold"),background="white")
        Dptlbl2.grid(row=0, column=4, padx=5, sticky=W)

        Dptcom2 = ttk.Combobox(RFrame1,textvariable=self.JOINING_MONTH, font=("Tahoma", 10), state="readonly", width=18,cursor="hand2")
        Dptcom2["values"] = (
            "Choose Month", "January", "February", "March", "April", "May", "June", "July", "August", "September",
            "October", "November", "December")
        Dptcom2.current(0)
        Dptcom2.grid(row=0, column=5, padx=5, pady=10, sticky=W)

        empid = Label(RFrame1, text="EmployeeID :", font=("tahoma", 10, "bold"), background="white")
        empid.grid(row=0, column=6, padx=5, pady=10, sticky=W)
        empbox = ttk.Entry(RFrame1, textvariable=self.EMPLOYEE_ID, width=20, font=("tahoma", 10),cursor="hand2")
        empbox.grid(row=0, column=7, padx=5, sticky=W)


        empname = Label(RFrame1, text="Name :", font=("tahoma", 10, "bold"), background="white")
        empname.grid(row=1, column=0, padx=5, pady=10, sticky=W)
        empnmbox = ttk.Entry(RFrame1, textvariable=self.NAME, width=20, font=("tahoma", 10),cursor="hand2")
        empnmbox.grid(row=1, column=1, padx=5, sticky=W)

        empdob = Label(RFrame1, text="D O B :", font=("tahoma", 10, "bold"), background="white")
        empdob.grid(row=1, column=2, padx=5, pady=10, sticky=W)
        empdbbox = ttk.Entry(RFrame1, textvariable=self.DOB, width=20, font=("tahoma", 10),cursor="hand2")
        empdbbox.grid(row=1, column=3, padx=5, sticky=W)

        empmail = Label(RFrame1, text="Email :", font=("tahoma", 10, "bold"), background="white")
        empmail.grid(row=1, column=4, padx=5, pady=10, sticky=W)
        empmlbox = ttk.Entry(RFrame1, textvariable=self.EMAIL, width=20, font=("tahoma", 10),cursor="hand2")
        empmlbox.grid(row=1, column=5, padx=5, sticky=W)

        empgndr = Label(RFrame1, text="Gender :", font=("tahoma", 10, "bold"), background="white")
        empgndr.grid(row=1, column=6, padx=5, pady=10, sticky=W)
        empgdbox = ttk.Combobox(RFrame1, textvariable=self.GENDER, width=18, font=("tahoma", 10), state="readonly",cursor="hand2")
        empgdbox["values"] = ("Choose Gender", "Male", "Female")
        empgdbox.current(0)
        empgdbox.grid(row=1, column=7, padx=5, sticky=W)

        empmsts = Label(RFrame1, text="Martial Status :", font=("tahoma", 10, "bold"), background="white")
        empmsts.grid(row=2, column=0, padx=5, pady=10, sticky=W)
        empmstbox = ttk.Combobox(RFrame1, textvariable=self.MARTIAL_STATUS, width=18, font=("tahoma", 10),state="readonly",cursor="hand2")
        empmstbox["values"] = ("Choose Marital status", "Married", "Unmarried")
        empmstbox.current(0)
        empmstbox.grid(row=2, column=1, padx=5, sticky=W)

        empnal = Label(RFrame1, text="Nationality :", font=("tahoma", 10, "bold"), background="white")
        empnal.grid(row=2, column=2, padx=5, pady=10, sticky=W)
        empnlbox = ttk.Entry(RFrame1, textvariable=self.NATIONALITY, width=20, font=("tahoma", 10),cursor="hand2")
        empnlbox.grid(row=2, column=3, padx=5, sticky=W)

        empbld = Label(RFrame1, text="Blood Group :", font=("tahoma", 10, "bold"), background="white")
        empbld.grid(row=2, column=4, padx=5, pady=10, sticky=W)
        empbldbox = ttk.Entry(RFrame1, textvariable=self.BLOOD_GROUP, width=20, font=("tahoma", 10),cursor="hand2")
        empbldbox.grid(row=2, column=5, padx=5, sticky=W)

        empphn = Label(RFrame1, text="Phone No. :", font=("tahoma", 10, "bold"), background="white")
        empphn.grid(row=2, column=6, padx=5, pady=10, sticky=W)
        emppnbox = ttk.Entry(RFrame1, textvariable=self.PHONE_NUMBER, width=20, font=("tahoma", 10),cursor="hand2")
        emppnbox.grid(row=2, column=7, padx=5, sticky=W)

        empadds = Label(RFrame1, text="Address :", font=("tahoma", 10, "bold"), background="white")
        empadds.grid(row=3, column=0, padx=5, pady=10, sticky=W)
        empadsbox = ttk.Entry(RFrame1, textvariable=self.ADDRESS, width=20, font=("tahoma", 10),cursor="hand2")
        empadsbox.grid(row=3, column=1, padx=5, sticky=W)


        RFrame2 = LabelFrame(RFrame1,background="white",foreground="white",bg='grey',borderwidth=2)
        RFrame2.place(x=1150, y=5, width=150, height=160)
        image1 = Image.open("images\\1.webp")
        image1 = image1.resize((140,160), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(image1)
        self.photo=Label(RFrame2,image=self.photoimg3,background="white",width=140,height=160)
        self.photo.grid(row=0,column=0)

        btnphto = customtkinter.CTkButton(RFrame1, text="Take Photo",command=lambda :self.facecaps(empbox.get(),0),fg_color="#fb341c",text_font=("Tahoma", 10,"bold"), width=150,cursor="hand2")
        btnphto.place(x=10,y=180)

        btnphto =customtkinter.CTkButton(RFrame1, text="Update Photo",command=lambda :self.facecaps(empbox.get(),1),fg_color="#fb341c",text_font=("Tahoma", 10,"bold"), width=150,cursor="hand2")
        btnphto.place(x=200,y=180)

        btnsave = customtkinter.CTkButton(RFrame1, text="Save", command=self.add_data,fg_color="#fb341c",text_font=("Tahoma", 10,"bold"), width=150,cursor="hand2")
        btnsave.place(x=400,y=180)

        btnupdt = customtkinter.CTkButton(RFrame1, text="Update", command=self.update_data,fg_color="#fb341c",text_font=("Tahoma", 10,"bold"), width=150,cursor="hand2")
        btnupdt.place(x=600,y=180)

        btndel = customtkinter.CTkButton(RFrame1, text="Delete", command=self.delete_data,fg_color="#fb341c",text_font=("Tahoma", 10,"bold"), width=150,cursor="hand2")
        btndel.place(x=800,y=180)

        btnres = customtkinter.CTkButton(RFrame1, text="Reset", command=self.reset_data,fg_color="#fb341c",text_font=("Tahoma", 10,"bold"), width=150,cursor="hand2")
        btnres.place(x=1000,y=180)

        #btnvwe = customtkinter.CTkButton(RFrame1, text="VIEW IMAGE", command=lambda :self.choose(empbox.get()), fg_color="#fb341c",text_font=("Tahoma", 10, "bold"), width=13)
        #btnvwe.grid(row=6, column=9)

        # rFrame
        RFrame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Employee Details", font=("Tahoma", 10, "bold"),bg="#515B60",fg='black')
        RFrame.place(x=5, y=440, width=1380, height=280)

        down_frame = customtkinter.CTkFrame(RFrame, bd=0, bg="White", relief=SUNKEN)
        down_frame.place(x=2, y=5, width=1350, height=250)

        topBtmsbar = customtkinter.CTkScrollbar(down_frame, orientation=HORIZONTAL,scrollbar_hover_color='red',scrollbar_color='#263238',height=12)
        sideBar = customtkinter.CTkScrollbar(down_frame, orientation=VERTICAL,scrollbar_color='#263238',scrollbar_hover_color='red',width=12)

        self.detailtbl = ttk.Treeview(down_frame, columns=("EMPLOYEE_ID", "NAME", "DEPARTMENT", "DESIGNATION",
                                                           "JOINING_MONTH", "DOB", "GENDER", "EMAIL", "MARTIAL_STATUS",
                                                           "NATIONALITY", "BLOOD_GROUP",  "PHONE_NUMBER",
                                                           "ADDRESS"), xscrollcommand=topBtmsbar.set,yscrollcommand=sideBar.set)
        topBtmsbar.pack(side=BOTTOM, fill=X)
        sideBar.pack(side=RIGHT, fill=Y)
        topBtmsbar.config(command=self.detailtbl.xview)
        sideBar.config(command=self.detailtbl.yview)

        self.detailtbl.heading("EMPLOYEE_ID", text="EMPLOYEE_ID")
        self.detailtbl.heading("NAME", text="NAME")
        self.detailtbl.heading("DEPARTMENT", text="DEPARTMENT")
        self.detailtbl.heading("DESIGNATION", text="DESIGNATION")
        self.detailtbl.heading("JOINING_MONTH", text="JOINING_MONTH")
        self.detailtbl.heading("DOB", text="DOB")
        self.detailtbl.heading("GENDER", text="GENDER")
        self.detailtbl.heading("EMAIL", text="EMAIL")
        self.detailtbl.heading("MARTIAL_STATUS", text="MARTIAL_STATUS")
        self.detailtbl.heading("NATIONALITY", text="NATIONALITY")
        self.detailtbl.heading("BLOOD_GROUP", text="BLOOD_GROUP")
        self.detailtbl.heading("PHONE_NUMBER", text="PHONE NUMBER")
        self.detailtbl.heading("ADDRESS", text="ADDRESS")

        self.detailtbl["show"] = "headings"

        self.detailtbl.pack(fill=BOTH, expand=1)
        self.detailtbl.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.DEPARTMENT.get() == "Select Department" or self.NAME.get() == "" or self.EMPLOYEE_ID.get() == "":
            messagebox.showerror("Error", "All Fields Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(user='adminuser', password='Akshay10', host='35.90.7.49',database='sas',port='3306')
                '''conn = mysql.connector.connect(user='root', password='password', host='localhost',
                                               database='sas', auth_plugin= 'caching_sha2_password')'''
                my_cursor = conn.cursor()
                my_cursor.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.EMPLOYEE_ID.get(),
                    self.NAME.get(),
                    self.DEPARTMENT.get(),
                    self.DESIGNATION.get(),
                    self.JOINING_MONTH.get(),
                    self.DOB.get(),
                    self.GENDER.get(),
                    self.EMAIL.get(),
                    self.MARTIAL_STATUS.get(),
                    self.NATIONALITY.get(),
                    self.BLOOD_GROUP.get(),
                    self.PHONE_NUMBER.get(),
                    self.ADDRESS.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Employee details has been added Successfully", parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error", f"Due To:{str(ex)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(user='adminuser', password='Akshay10', host='35.90.7.49', database='sas',
                                       port='3306')
        '''conn = mysql.connector.connect(user='root', password='password', host='localhost', database='sas', auth_plugin='caching_sha2_password')'''
        my_cursor = conn.cursor()
        my_cursor.execute("select * from employee")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.detailtbl.delete(*self.detailtbl.get_children())
            for i in data:
                self.detailtbl.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_focus = self.detailtbl.focus()
        content = self.detailtbl.item(cursor_focus)
        data = content["values"]

        self.EMPLOYEE_ID.set(data[0]),
        self.NAME.set(data[1]),
        self.DEPARTMENT.set(data[2]),
        self.DESIGNATION.set(data[3]),
        self.JOINING_MONTH.set(data[4]),
        self.DOB.set(data[5]),
        self.GENDER.set(data[6]),
        self.EMAIL.set(data[7]),
        self.MARTIAL_STATUS.set(data[8]),
        self.NATIONALITY.set(data[9]),
        self.BLOOD_GROUP.set(data[10]),
        self.PHONE_NUMBER.set(data[11]),
        self.ADDRESS.set(data[12])
        attendance.choose(self,data[0])

    def update_data(self):
        global conn
        if self.DEPARTMENT.get() == "Select Department" or self.NAME.get() == "" or self.EMPLOYEE_ID.get() == "":
            messagebox.showerror("Error", "All Fields Required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this employee details", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(user='adminuser', password='Akshay10', host='35.90.7.49',
                                                   database='sas',
                                                   port='3306')
                    '''conn = mysql.connector.connect(user='root', password='password', host='localhost', database='sas', auth_plugin=' caching_sha2_password')'''
                    my_cursor = conn.cursor()
                    my_cursor.execute("update employee set NAME=%s,DEPARTMENT=%s,DESGNATION=%s,JOINING_MONTH=%s,DOB=%s,GENDER=%s,EMAIL=%s,MARTIAL_STATUS=%s,NATIONALITY=%s,BLOOD_GROUP=%s,PHONE_NUMBER=%s,ADDRESS=%s WHERE (EMPLOYEE_ID=%s)",(
                            self.NAME.get(),
                            self.DEPARTMENT.get(),
                            self.DESIGNATION.get(),
                            self.JOINING_MONTH.get(),
                            self.DOB.get(),
                            self.GENDER.get(),
                            self.EMAIL.get(),
                            self.MARTIAL_STATUS.get(),
                            self.NATIONALITY.get(),
                            self.BLOOD_GROUP.get(),
                            self.PHONE_NUMBER.get(),
                            self.ADDRESS.get(),
                            self.EMPLOYEE_ID.get()
                        ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success", "Details saved Successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as ex:
                messagebox.showerror("Error", f"Due To:{str(ex)}", parent=self.root)

    def delete_data(self):
        if self.EMPLOYEE_ID.get() == "":
            messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Employee_detail_delete", "Do you want to delete this employee_details", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(user='adminuser', password='Akshay10', host='35.90.7.49', database='sas',
                                                   port='3306')
                    '''conn = mysql.connector.connect(user='root', password='password', host='localhost', database='sas', auth_plugin=' caching_sha2_password')'''
                    my_cursor = conn.cursor()
                    sql = "delete from employee where employee_id=%s"
                    val = (self.EMPLOYEE_ID.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Employee_details Successfully Deleted", parent=self.root)

            except Exception as ex:
                messagebox.showerror("Error", f"Due To:{str(ex)}", parent=self.root)

    def reset_data(self):
        self.EMPLOYEE_ID.set(""),
        self.NAME.set(""),
        self.DEPARTMENT.set("Select the Department"),
        self.DESIGNATION.set("Select the Designation"),
        self.JOINING_MONTH.set(""),
        self.DOB.set(""),
        self.GENDER.set("Choose Gender"),
        self.EMAIL.set(""),
        self.MARTIAL_STATUS.set("Choose Martial status"),
        self.NATIONALITY.set(""),
        self.BLOOD_GROUP.set(""),
        self.PHONE_NUMBER.set(""),
        self.ADDRESS.set("")
        attendance.choose(self,1)

    def choose(self,value):
        path="images\\"+str(value)+".jpeg"
        opimg = ImageTk.PhotoImage(Image.open(path).resize((140,160),Image.Resampling.LANCZOS))
        self.photo.configure(image=opimg)
        self.photo.image=opimg

    def facecaps(self,value,i):
        self.new_window2=Toplevel(self.root)
        facecap.add_img(self.new_window2,value,i)
        attendance.choose(self,value)

if __name__ == '__main__':
    root = Tk()
    obj = attendance(root)
    root.mainloop()


