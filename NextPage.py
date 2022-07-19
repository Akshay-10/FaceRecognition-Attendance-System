from tkinter import *
from PIL import Image,ImageTk
import customtkinter
from PREDICTION import carpredict
from AttsNpage import attendance
from face_recog31 import realpredict
#from face_Recog_test import realpredict

class face_Recog:
    def __init__(self,root):
        self.root=root
        root.state('zoomed')
        self.root.title("Smart Authorizing System")
        self.root.iconbitmap("img\\saslog.ico")

        img = Image.open(r"img\\log bg.jpg")
        img.resize((500,500),Image.Resampling.LANCZOS)
        self.photoimg00 = ImageTk.PhotoImage(img)
        fstlbl = Label(self.root, image=self.photoimg00)
        fstlbl.place(x=0, y=100)

        img1=Image.open("img\\6b77beffb8d54b09b7414bd72c07342e.png")
        img1=img1.resize((105,105),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        sndlbl=Label(self.root,image=self.photoimg1)
        sndlbl.place(x=0,y=0,width=105,height=105)

        logi_in = Label(self.root, text="SMART AUTHORIZING SYSTEM", font=("Tahoma", 20, "bold"), fg="#f5f5f5", bg="#263238",width=80,height=3, bd=2)
        logi_in.place(x=100, y=0)

        #img2=Image.open("flc_design2022053147056.png")
        #img2=img2.resize((300,100),Image.ANTIALIAS)
        #self.photoimg3=ImageTk.PhotoImage(img2)
        #trdlbl=Label(self.root,image=self.photoimg3)
        #trdlbl.place(x=550,y=0,width=300,height=100)

        LFrame = customtkinter.CTkFrame(self.root, bd=0, relief=RIDGE,fg_color="#263238")
        LFrame.place(x=150, y=130, width=1100, height=550)

        imabg=Image.open(r"img\\log Offince.jpg")
        imabg=imabg.resize((500,550),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(imabg)
        bg_img1 = customtkinter.CTkLabel(LFrame, image=self.photoimg)
        bg_img1.place(x=7, y=0)

        logi_in = Label(LFrame, text="WELCOME TO S A S ! !", font=("Tahoma", 20, "bold"), fg="#f5f5f5", bg="#263238",width=30, bd=2)
        logi_in.place(x=0, y=45)

        stdimg0=Image.open("img\\emo details.jpg")
        stdimg0=stdimg0.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg0=ImageTk.PhotoImage(stdimg0)
        b1 = customtkinter.CTkButton(self.root, image=self.photoimg0,command=self.emp_details,cursor="hand2",bd=0,text="0",bg_color="#263238")
        b1.place(x=700, y=200, width=101, height=100)
        lbltxt = customtkinter.CTkLabel(self.root, text="EMP DETAILS",anchor='center',relief=SUNKEN, fg_color="#2E86C1",bg_color="#263238", text_font=("Tahoma ", 9, "bold"))
        lbltxt.place(x=700, y=295, width=101, height=30)

        stdimg = Image.open("img\\facFin.webp")
        stdimg = stdimg.resize((100, 100), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(stdimg)
        b2=customtkinter.CTkButton(self.root,image=self.photoimg4,cursor="hand2",fg_color="#F44336",command=self.attns,bg_color="#263238",bd=0,text="0")
        b2.place(x=900,y=200,width=101,height=100)
        lbltxt=customtkinter.CTkLabel(self.root,text="ATTENDANCE",anchor='center',relief=SUNKEN,fg_color="#F44336",bg_color="#263238",text_font=("Tahoma ", 9, "bold"))
        lbltxt.place(x=900,y=295,width=101,height=30)

        stdimg1 = Image.open("img\\numplt.jpg")
        stdimg1 = stdimg1.resize((100, 100), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(stdimg1)
        b3 = customtkinter.CTkButton(self.root, image=self.photoimg5,command=self.carplt,cursor="hand2",fg_color="#2E86C1",bg_color="#263238",bd=0,text="0")
        b3.place(x=1100, y=200, width=101, height=100)
        lbltxt = customtkinter.CTkLabel(self.root, text="PLATE FINDER",relief=SUNKEN,anchor='center', fg_color="#2E86C1",bg_color="#263238", text_font=("Tahoma ", 9, "bold"))
        lbltxt.place(x=1100, y=295, width=101, height=30)

        #stdimg2 = Image.open("trainimg.jpg")
        #stdimg2 = stdimg2.resize((100, 100), Image.ANTIALIAS)
        #self.photoimg6 = ImageTk.PhotoImage(stdimg2)
        #b4 = customtkinter.CTkButton(self.root, image=self.photoimg6,cursor="hand2",fg_color="#2ECC71",bg_color="#263238",text="0")
        #b4.place(x=700, y=410, width=101, height=100)
        #lbltxt = customtkinter.CTkLabel(self.root, text="TRAIN DATA",relief=SUNKEN,anchor='center', fg_color="#2ECC71",bg_color="#263238", text_font=("Tahoma ", 9, "bold"))
        #lbltxt.place(x=700, y=495, width=101, height=30)

        stdimg3 = Image.open("img\\exitimg.jpg")
        stdimg3 = stdimg3.resize((100, 100), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(stdimg3)
        b5 = customtkinter.CTkButton(self.root, image=self.photoimg7,command=quit,cursor="hand1",bg_color="#263238",fg_color="#F44336",text="0")
        b5.place(x=900, y=410, width=101, height=100)
        lbltxt = customtkinter.CTkLabel(self.root, text="EXIT",anchor='center',relief=SUNKEN, fg_color="#F44336",bg_color="#263238", text_font=("Tahoma ", 9, "bold"))
        lbltxt.place(x=900, y=495, width=101, height=30)

    def emp_details(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance(self.new_window)

    def attns(self):
        self.new_window2=Toplevel(self.root)
        self.atn=realpredict(self.new_window2)

    def carplt(self):
        self.new_window2=Toplevel(self.root)
        self.atn=carpredict(self.new_window2)

if __name__ == '__main__':
    root=Tk()
    obj=face_Recog(root)
    root.mainloop()
