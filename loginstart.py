from tkinter import *
import customtkinter
from tkinter import messagebox
from tkinter import ttk
from NextPage import face_Recog
import mysql.connector
from PIL import Image,ImageTk

class login_design():
    def __init__(self, root):
        self.root=root
        self.root.geometry('1100x590+180+90')
        self.root.title("login")
        self.root.overrideredirect(True)
        self.root.iconbitmap("img\\saslog.ico")

        self.user=StringVar()
        self.pasw=StringVar()
        self.comb_security=StringVar()
        self.combo_securityA=StringVar()
        self.new_pass=StringVar()

        #frame0 = customtkinter.CTkFrame(self.root, bd=0)
        #frame0.place(x=0, y=0, width=1600, height=950)
        #bgimg=Image.open("img\\pexels-ben-mack-6775241.jpg")
        #bgimg.resize((500,500),Image.Resampling.LANCZOS)
        #self.img=ImageTk.PhotoImage(bgimg)
        #lbl=Label(frame0,image=self.img)
        #lbl.place(x=0,y=0)

        frame1=customtkinter.CTkFrame(self.root, bd=0,relief=GROOVE,fg_color="#263238",bg_color="grey")
        frame1.place(x=0, y=0, width=1100, height=590)

####################
        signuptxt=customtkinter.CTkLabel(frame1,text="Sign in",text_font=("Tahoma",15,"bold"),fg_color="#263238",text_color="white")
        signuptxt.place(x=605,y=114)

        imglog = Image.open("img\\6b77beffb8d54b09b7414bd72c07342e.png")
        imglog = imglog.resize((90, 90), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(imglog)
        bg_img = customtkinter.CTkLabel(frame1, image=self.photoimg)
        bg_img.place(x=500, y=50)

        imglog1 = Image.open(r"img\\log Offince.jpg")
        imglog1 = imglog1.resize((450, 590), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(imglog1)
        bg_img1 = customtkinter.CTkLabel(frame1, image=self.photoimg1)
        bg_img1.place(x=0, y=0)

        logi_in=Label(frame1,text="W E L C O M E ! !",font=("Tahoma",20,"bold"),fg="#f5f5f5",bg="#263238",width=30,bd=2)
        logi_in.place(x=0, y=45)

        username_lbl = customtkinter.CTkLabel(frame1, text="Username", text_font=("Tahoma", 10,"bold"),text_color="white", bg_color="#263238")
        username_lbl.place(x=485, y=180)
        self.user_entry = customtkinter.CTkEntry(frame1, width=300,height=20,text_font=("Tahoma", 10),fg_color="black",text_color="white",cursor="hand2",border_width=0)
        self.user_entry.place(x=520, y=210)
########################
        pswd_lbl = customtkinter.CTkLabel(frame1, text="Password",text_font=("Tahoma", 10,"bold"), text_color="white",bg_color="#263238")
        pswd_lbl.place(x=485, y=260)
        self.pswd_entry = customtkinter.CTkEntry(frame1, width=300,height=20,text_font=("Tahoma", 10),fg_color="black", text_color="white",cursor="hand2",show="*",border_width=0)
        self.pswd_entry.place(x=520, y=290)
        ###########
        logbutton=customtkinter.CTkButton(frame1,text="Login",command=self.login,width=300,height=30,relief=RIDGE,text_font=("Tahoma", 10,"bold"), text_color="black",fg_color="#fb341c",cursor="hand2")
        logbutton.place(x=520,y=340)
##################
        fgtpass=customtkinter.CTkButton(frame1,text="forgot password ?",command=self.fgt_pass,height=0,width=0,bd=0,text_font=("Tahoma", 10,"bold"),fg_color="#263238",text_color="#fa333e",cursor="hand2")
        fgtpass.place(x=690,y=375)
########################

    def fgt_pass(self):
        self.root1 = Toplevel()
        self.root1.title("Forgot Password")
        self.root1.geometry('450x477+180+175')
        self.root1.config(bg="#263238")

        flbl = customtkinter.CTkLabel(self.root1, text="Forgot Password", text_font=("Tahoma", 10, "bold"),bg_color="#263238", fg_color="orange",width=450)
        flbl.place(x=0, y=10)

        schlbl = customtkinter.CTkLabel(self.root1, text="Email Id",text_font=("Tahoma", 10, "bold"),text_color='white',bg_color="#263238",fg_color="#263238",width=90)
        schlbl.place(x=40, y=70)
        schcomb =customtkinter.CTkEntry(self.root1, width=300,height=20,text_font=("times new roman", 10),text_color='white',border_width=0,fg_color='black',cursor="hand2")
        schcomb.place(x=55, y=100)

        anwlbl = customtkinter.CTkLabel(self.root1, text="New Password", text_font=("Tahoma", 10, "bold"),text_color='white',bg_color="#263238",fg_color="#263238",width=90)
        anwlbl.place(x=50, y=130)
        self.ans_entry = customtkinter.CTkEntry(self.root1, width=300,height=20,text_font=("times new roman", 10),text_color='white',border_width=0,fg_color='black',show='*',cursor="hand2")
        self.ans_entry.place(x=55, y=160)

        pass_lbl = customtkinter.CTkLabel(self.root1, text="Confirm Password", text_font=("Tahoma", 10, "bold"),text_color='white',bg_color="#263238",fg_color="#263238",width=90)
        pass_lbl.place(x=50, y=190)
        self.pass_entry = customtkinter.CTkEntry(self.root1, width=300,height=20,text_font=("times new roman", 10),text_color='white',border_width=0,fg_color='black',show='*',cursor="hand2")
        self.pass_entry.place(x=55, y=220)

        restbut=customtkinter.CTkButton(self.root1,text='Reset',text_font=("Tahoma", 15, "bold"),text_color='orange',bg_color="#263238",fg_color="#263238",width=1,cursor="hand2")
        restbut.place(x=280, y=250)

        connection = mysql.connector.connect(user='adminuser', password='Akshay10', host='35.90.7.49', database='sas',port='3306')
        my_cursor=connection.cursor()
        my_cursor.execute("select * from regsaved where email=%s",(self.user.get()))
        row=my_cursor.fetchone()

        if row==None:
            messagebox.showerror("Error","Please enter the valid email id")
        else:
            connection.close()

    def login(self):
        if self.user_entry.get=="" or self.pswd_entry.get()=="":
            messagebox.showerror("Error","Fill all the field")
        elif self.user_entry.get()=="Akshay10" and self.pswd_entry.get()=="sas123":
            messagebox.showinfo("Welcome", "Welcome to S A S")
            self.nxt_win=customtkinter.CTkToplevel(self.root)
            self.root=face_Recog(self.nxt_win)

        else:
            connection = mysql.connector.connect(user='adminuser', password='Akshay10', host='35.90.7.49', database='sas',port='3306')
            '''connection=mysql.connector.connect(user='adminuser', password='Akshay10', host='35.90.7.49',
                                               database='sas', auth_plugin= 'caching_sha2_password')'''
            my_cursor=connection.cursor()
            my_cursor.execute("select * from regsaved where pswd_entry=%s and user_entry=%s",(
                self.user_entry.get(),
                self.pswd_entry.get()
            ))
            row=my_cursor.fetchall()
            print(row)
            if len(row)==0:
                messagebox.showerror("Error","Invalid username or password")
            else:
                openfr_admin=messagebox.askyesno("Access only to adimin?")
                if openfr_admin>0:
                    self.nxt_win=Toplevel(self.root)
                    self.root=face_Recog(self.nxt_win)
                else:
                    if not openfr_admin:
                        return
                connection.commit()
                connection.commit()

if __name__ == '__main__':
    root=Tk()
    obj=login_design(root)
    root.mainloop()