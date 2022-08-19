from tkinter import *
import customtkinter
from tkinter import messagebox
from NextPage import face_Recog
import mysql.connector
from PIL import Image,ImageTk

class login_design():
    def __init__(self, root):
        self.root=root
        self.root.geometry('1100x590+180+90')
        self.root.overrideredirect(True)
        #self.root.customtkinter.deactivate_automatic_dpi_awareness()
        self.root.title("login")
        self.root.iconbitmap("img\\saslog.ico")

        self.user=StringVar()
        self.pasw=StringVar()
        self.comb_security=StringVar()
        self.combo_securityA=StringVar()
        self.new_pass=StringVar()
        customtkinter.set_default_color_theme("sweetkind")  # Themes: blue (default), dark-blue, green4

        frame1=customtkinter.CTkFrame(self.root,relief=GROOVE,fg_color="#263238",bg_color="#263238")
        frame1.place(x=0, y=0, width=1100, height=590)
        xbut = customtkinter.CTkButton(frame1, text='x', text_font=("Tahoma", 10, "bold"), command=root.destroy,text_color='#fa333e',bg_color="#263238", fg_color="#263238", width=5)
        xbut.place(x=1072, y=0)


        signuptxt=customtkinter.CTkLabel(frame1,text="Sign in",text_font=("Tahoma",15,"bold"),fg_color="#263238",text_color="white")
        signuptxt.place(x=605,y=114)

        imglog = Image.open("img\\6b77beffb8d54b09b7414bd72c07342e.png")
        imglog = imglog.resize((90, 90), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(imglog)
        bg_img = customtkinter.CTkLabel(frame1, image=self.photoimg)
        bg_img.place(x=500, y=50)

        imglog1 = Image.open("img\\log Offince.jpg")
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
        self.root1.geometry('448x500+189+179')
        self.root1.overrideredirect(True)
        self.root1.config(bg="#263238")
        self.root1.iconbitmap("img\\saslog.ico")

        flbl = customtkinter.CTkLabel(self.root1, text="Forgot Password", text_font=("Tahoma", 10, "bold"),text_color='black',bg_color="#263238", fg_color="orange",width=419)
        flbl.place(x=0, y=10)
        xbut=customtkinter.CTkButton(self.root1,text='x',text_font=("Tahoma", 10, "bold"),text_color='#fa333e',command=self.root1.destroy,bg_color="#263238", fg_color="#263238",width=5)
        xbut.place(x=419,y=10)

        schlbl = customtkinter.CTkLabel(self.root1, text="Email Id",text_font=("Tahoma", 10, "bold"),text_color='white',bg_color="#263238",fg_color="#263238",width=90)
        schlbl.place(x=40, y=70)
        schcomb =customtkinter.CTkEntry(self.root1, width=300,height=20,text_font=("times new roman", 10),text_color='white',border_width=0,fg_color='black',cursor="hand2")
        schcomb.place(x=55, y=100)

        fgtpass = customtkinter.CTkButton(self.root1, text="verify", command=lambda: self.verify(schcomb.get()),
                                          height=0, width=0,
                                          bd=0, text_font=("Tahoma", 10, "bold"), fg_color="#263238",
                                          text_color="#fa333e", cursor="hand2")
        fgtpass.place(x=370, y=100)

        self.anwlbl = customtkinter.CTkLabel(self.root1, text="New Password", text_font=("Tahoma", 10, "bold"),
                                  text_color='white', bg_color="#263238", fg_color="#263238", width=90)

        self.ans_entry = customtkinter.CTkEntry(self.root1, width=300, height=20, text_font=("times new roman", 10),
                                                text_color='white', border_width=0, fg_color='black', show='*',
                                                cursor="hand2")

        self.pass_lbl = customtkinter.CTkLabel(self.root1, text="Confirm Password", text_font=("Tahoma", 10, "bold"),
                                               text_color='white', bg_color="#263238", fg_color="#263238", width=90)

        self.pass_entry = customtkinter.CTkEntry(self.root1, width=300, height=20, text_font=("times new roman", 10),
                                                 text_color='white', border_width=0, fg_color='black', show='*',
                                                 cursor="hand2")

        self.restbut = customtkinter.CTkButton(self.root1, text='Reset',command=lambda: self.changepassword(schcomb.get(),self.ans_entry.get(),self.pass_entry.get()), text_font=("Tahoma", 15, "bold"),
                                               text_color='orange', bg_color="#263238", fg_color="#263238", width=1,
                                               cursor="hand2")

    def verify(self,email):
        #print(email)
        connection = mysql.connector.connect(user='adminuser', password='Akshay10', host='35.90.7.49', database='sas',port='3306')
        my_cursor = connection.cursor()
        my_cursor.execute("select count(*) from regsaved where email=%s", (email,))
        row = my_cursor.fetchone()
        connection.close()
        if(row[0]==1):
            self.anwlbl.place(x=50, y=130)
            self.ans_entry.place(x=55, y=160)
            self.pass_lbl.place(x=50, y=190)
            self.pass_entry.place(x=55, y=220)
            self.restbut.place(x=280, y=250)

    def changepassword(self,email,password,c_password):
        #print(email,password,c_password)
        if(password==c_password):
            connection = mysql.connector.connect(user='adminuser', password='Akshay10', host='35.90.7.49',database='sas', port='3306')
            my_cursor = connection.cursor()
            my_cursor.execute("update regsaved set pswd_entry=%s where email=%s", (password,email))
            connection.commit()
            connection.close()
            messagebox.showinfo("SUCCESS","Successfully updated")
        else:
            messagebox.showinfo("ERROR","New Password and Conform Password is not matched")

    def login(self):
        if self.user_entry.get()=="" or self.pswd_entry.get()=="":
            messagebox.showerror("Error","Fill all the field")
        else:
            connection = mysql.connector.connect(user='adminuser', password='Akshay10', host='35.90.7.49', database='sas',port='3306')
            my_cursor=connection.cursor()
            my_cursor.execute("select count(*) from regsaved where user_entry=%s and pswd_entry=%s",(
                self.user_entry.get(),
                self.pswd_entry.get()
            ))
            row=my_cursor.fetchone()
            connection.close()
            if row==0:
                messagebox.showerror("Error","Invalid username or password")
            elif row[0]==1:
                messagebox.showinfo("Welcome", "Welcome to S A S")
                self.nxt_win = Toplevel(self.root)
                self.root = face_Recog(self.nxt_win)

if __name__ == '__main__':
    root=Tk()
    obj=login_design(root)
    root.mainloop()