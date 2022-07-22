import cv2
import numpy as ny
import os
import pytesseract
import warnings
import datetime
import csv
import pandas as pd
from tkinter import ttk
from PIL import ImageTk
import PIL.Image
import customtkinter
import Image, ImageTk
from tkinter import *
from tkinter import ttk, messagebox

class carpredict:
    def __init__(self,root):
        self.root=root
        self.root.state('zoomed')
        self.root.title('Number Plate Recognition')
        self.cam_start = 1
        self.root.overrideredirect(True)
        self.root.iconbitmap("img\\saslog.ico")

        image = PIL.Image.open("img\\pexels-ben-mack-6775241.jpg")  # use this
        image.resize((1530,990),PIL.Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)
        fstlbl = Label(self.root, image=self.photo)
        fstlbl.place(x=0, y=100, width=1530, height=990)

        img1 = PIL.Image.open("img\\6b77beffb8d54b09b7414bd72c07342e.png")
        img1 = img1.resize((105, 105), PIL.Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        sndlbl = Label(self.root, image=self.photoimg1)
        sndlbl.place(x=0, y=0, width=105, height=105)

        logi_in = Label(self.root, text="SMART AUTHORIZING SYSTEM", font=("Tahoma", 20, "bold"), fg="#f5f5f5",bg="#263238", width=80, height=3, bd=2)
        logi_in.place(x=100, y=0)

        head = Label(self.root, text="VEHICLE NUMBER ENTRY RECORD", font=("Tahoma", 25, "bold"), bg="#263238", fg="white")
        head.place(x=-120, y=120, width=1530, height=40)
        back = customtkinter.CTkButton(self.root, text="Back", text_font=("Tahoma", 10, "bold"), bg_color="black",
                                       fg_color="#64b5f6",command=self.back,cursor="hand2")
        back.place(x=1200, y=126)

        frame = Frame(self.root, bd=2)
        frame.place(x=0, y=175, width=1530, height=650)

        RFrame1 = LabelFrame(self.root, bd=2, relief=RIDGE, font=("Tahoma", 12, "bold"), bg="#263238")
        RFrame1.place(x=0, y=180, width=1600, height=900)

        startcam = customtkinter.CTkButton(RFrame1, command=self.cplt, width=300, height=30, text="START CAMARA",
                                           text_font=("Tahoma", 15), fg_color="#fb341c",cursor="hand2")
        startcam.place(x=730, y=290)

        stopcam = customtkinter.CTkButton(RFrame1, command=self.stopcamara, width=300, height=30, text="STOP CAMARA",
                                          text_font=("Tahoma", 15), fg_color="#fb341c",cursor="hand2")
        stopcam.place(x=1050, y=290)

        down_frame = customtkinter.CTkFrame(RFrame1)
        down_frame.place(x=730, y=20, width=625, height=235)

        leftframe = customtkinter.CTkFrame(RFrame1)
        leftframe.place(x=10, y=20, width=700, height=450)

        img10 = PIL.Image.open("img\\featured_image-1.jpg")
        img10= img10.resize((700, 450), PIL.Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img10)
        self.bg_img1 = customtkinter.CTkLabel(leftframe, image=self.photoimg4, fg_color="black", bg_color="black")
        self.bg_img1.place(x=0, y=0)

        sideBar = customtkinter.CTkScrollbar(down_frame, orientation=VERTICAL,scrollbar_hover_color='red',scrollbar_color='#263238',width=12)

        self.detailtbl = ttk.Treeview(down_frame, columns=("VEHICLE_NUMBER","ENTRY_TIME","EXIT_TIME"),
                                      yscrollcommand=sideBar.set, height=500)
        # topBtmsbar.pack(side=BOTTOM, fill=X)
        sideBar.pack(side=RIGHT, fill=Y)
        # topBtmsbar.config(command=self.detailtbl.xview)
        sideBar.config(command=self.detailtbl.yview)

        self.detailtbl.heading("VEHICLE_NUMBER", text="VEHICLE_NUMBER")
        self.detailtbl.heading("ENTRY_TIME", text="ENTRY_TIME")
        self.detailtbl.heading("EXIT_TIME",text="EXIT_TIME")
        self.detailtbl["show"] = "headings"
        self.detailtbl.column("VEHICLE_NUMBER", width=100)
        self.detailtbl.column("ENTRY_TIME", width=100)
        self.detailtbl.column("EXIT_TIME", width=100)
        self.detailtbl.pack(fill=BOTH, expand=0)

    def back(self):
        if(self.cam_start==1):
            self.root.destroy()
        else:
            messagebox.showwarning("WARNING","STOP THE CAMARA BEFORE GOING BACK", parent=self.root)

    def stopcamara(self):
        self.cam_start = 1

    def cplt(self):
        size=0
        today=datetime.date.today()
        today="entry/"+today.strftime("%d_%m_%Y")+".csv"
        print(today)
        with open(today,'a+')as file:
            writer=csv.writer(file)
            if os.path.getsize(today)==0:
                writer.writerow(['VEHICLE_NUMBER','ENTRY_TIME','EXIT_TIME'])
                size = os.path.getsize(today)
        entry_list = []
        prev_attendance = []
        with open(today, 'r+') as file:
            reader = csv.reader(file)
            if size > 37:
                for row in reader:
                    if row != []:
                        prev_attendance.append(row[0])
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

        INPUT_WIDTH=640
        INPUT_HEIGHT=640

        mod=cv2.dnn.readNetFromONNX('best.onnx')
        mod.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        mod.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

        def get_dedect(img,mod):
            image=img.copy()
            row,col,d= image.shape
            max_rc=max(row,col)
            input_image=ny.zeros((max_rc,max_rc,3),dtype=ny.uint8)
            input_image[0:row,0:col]=image

            blob=cv2.dnn.blobFromImage(input_image,1/255,(INPUT_WIDTH,INPUT_HEIGHT),swapRB=True,crop=False)
            mod.setInput(blob)
            pred=mod.forward()
            detect=pred[0]
            return input_image,detect

        def non_maxi(input_image,detect):
            boxes=[]
            confidences=[]
            img_w,img_h=input_image.shape[:2]
            xfactor=img_w/INPUT_WIDTH
            yfactor=img_h/INPUT_HEIGHT
            for i in range(len(detect)):
                row=detect[i]
                confidence=row[4]
                if confidence>0.4:
                    class_score=row[5]
                    if class_score>0.25:
                        cx,cy,w,h=row[0:4]
                        left=int((cx-0.5*w)*xfactor)
                        top=int((cy-0.5*h)*yfactor)
                        width=int(w*xfactor)
                        height=int(h*yfactor)
                        box=ny.array([left,top,width,height])
                        confidences.append(confidence)
                        boxes.append(box)
            nyboxes=ny.array(boxes).tolist()
            nyconfidences=ny.array(confidences).tolist()
            ind=cv2.dnn.NMSBoxes(nyboxes,nyconfidences,0.25,0.45)

            warnings.filterwarnings("ignore",category=DeprecationWarning)
            if ind!=():
                index=ind.flatten()

                return nyboxes,nyconfidences,index
            else:
                return nyboxes,nyconfidences,()

        def borders(image,nyboxes,nyconfidences,index):
            for i in index:
                x,y,w,h=nyboxes[i]
                bb_confi=nyconfidences[i]
                conf_text='plate: {:.0f}%'.format(bb_confi*100)
                plate_text=extract_text(image,nyboxes[i])

                cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,255),2)
                cv2.rectangle(image,(x,y-30),(x+w,y),(255,0,255),-1)
                cv2.rectangle(image,(x,y+h),(x+w,y+h+30),(0,0,0),-1)

                cv2.putText(image,conf_text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),1)
                cv2.putText(image,plate_text,(x,y+h+27),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),1)
                return image

        def predicts(img,mod):
            input_image,detect=get_dedect(img,mod)
            nyboxes,nyconfidences,index=non_maxi(input_image,detect)

            if index != ():
                result_img=borders(img,nyboxes,nyconfidences,index)

                return result_img
            else:
                return ()

        def extract_text(image,bbox):
            x,y,w,h=bbox
            roi=image[y:y+h,x:x+w]
            if 0 in roi.shape:
                return ''
            else:
                text=pytesseract.image_to_string(roi)
                text=text.strip()
                text = ''.join(char for char in text if char.isalnum())
                if text != "" and text != " ":
                    if text not in prev_attendance:
                        time1 = datetime.datetime.now()
                        #time1 = time1.strftime("%H:%M:%S")
                        i = [text, time1,"00:00:00"]
                        entry_list.append(i)
                        prev_attendance.append(text)
                    else:
                        x = prev_attendance.index(text)
                        time1 = datetime.datetime.now()
                        if time1 > entry_list[x][1] + pd.DateOffset(minutes=1):
                            entry_list[x][2]=time1.strftime("%H:%M:%S")
                return text

        cap = cv2.VideoCapture(1)
        while True:
            ret,frame=cap.read()
            cv2.imshow("frame",frame)
            if ret==False:
                messagebox.showerror("Error","UNABLE TO READ")
                break
            results=predicts(frame,mod)

            if results!=():
                cv2.namedWindow('YOLO',cv2.WINDOW_KEEPRATIO)
                cv2.imshow('YOLO',results)
            if cv2.waitKey(1) == 65:
                    break
        with open(today, 'a+', encoding='UTF8', newline='') as file:
            writer = csv.writer(file)
            for i in entry_list:
                writer.writerow(i)
        cv2.destroyAllWindows()
        cap.release()

if __name__ == '__main__':
    root = Tk()
    obj = carpredict(root)
    root.mainloop()

