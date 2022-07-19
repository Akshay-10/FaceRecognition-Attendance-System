import time
from tkinter import *
import customtkinter
import mysql.connector
from PIL import Image, ImageTk
import pickle
import datetime
import face_recognition
from numpy import load
from pygame import mixer
import warnings
import numpy as np
import onnxruntime as rt
import cv2
from tkinter import ttk, messagebox


class realpredict:
    def __init__(self, root):
        self.root = root
        root.state('zoomed')
        self.root.title("Attendance System")
        self.root.iconbitmap("img\\saslog.ico")
        self.cam_start=1
        img = Image.open("img\\pexels-ben-mack-6775241.jpg")
        img = img.resize((1530, 990), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        fstlbl = Label(self.root, image=self.photoimg)
        fstlbl.place(x=0, y=100, width=1530, height=990)

        # OOOOOOOOO

        img1 = Image.open("img\\6b77beffb8d54b09b7414bd72c07342e.png")
        img1 = img1.resize((105, 105), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        sndlbl = Label(self.root, image=self.photoimg1)
        sndlbl.place(x=0, y=0, width=105, height=105)

        logi_in = Label(self.root, text="SMART AUTHORIZING SYSTEM", font=("Tahoma", 20, "bold"), fg="#f5f5f5",bg="#263238", width=80, height=3, bd=2)
        logi_in.place(x=100, y=0)

        head = Label(self.root, text="ATTENDANCE REPORT", font=("Tahoma", 25, "bold"), bg="black", fg="white")
        head.place(x=-120, y=120, width=1530, height=40)
        back = customtkinter.CTkButton(self.root, text="Back", text_font=("Tahoma", 10, "bold"), bg_color="black",fg_color="#64b5f6", command=self.back,cursor="hand2")
        back.place(x=1200, y=126)

        frame = Frame(self.root, bd=2)
        frame.place(x=0, y=175, width=1530, height=650)

        RFrame1 = LabelFrame(self.root, bd=2, relief=RIDGE, font=("Tahoma", 12, "bold"), bg="#263238")
        RFrame1.place(x=0, y=180, width=1600, height=900)

        startcam = customtkinter.CTkButton(RFrame1, command=self.attnsmark, width=300, height=30, text="START CAMARA",text_font=("Tahoma", 15), fg_color="#fb341c",cursor="hand2")
        startcam.place(x=730, y=290)

        stopcam = customtkinter.CTkButton(RFrame1, command=self.stopcamara, width=300, height=30, text="STOP CAMARA",text_font=("Tahoma", 15), fg_color="#fb341c",cursor="hand2")
        stopcam.place(x=1050, y=290)

        down_frame = customtkinter.CTkFrame(RFrame1)
        down_frame.place(x=730, y=20, width=625, height=235)

        leftframe = customtkinter.CTkFrame(RFrame1)
        leftframe.place(x=10,y=20,width=700,height=450)

        img1 = Image.open("img\\featured_image-1.jpg")
        img1 = img1.resize((700,450), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img1)
        self.bg_img1 = customtkinter.CTkLabel(leftframe, image=self.photoimg4, fg_color="black", bg_color="black")
        self.bg_img1.place(x=0, y=0)

        #topBtmsbar = ttk.Scrollbar(down_frame, orient=HORIZONTAL)
        sideBar = ttk.Scrollbar(down_frame, orient=VERTICAL)

        self.detailtbl = ttk.Treeview(down_frame, columns=("EMPLOYEE_ID", "NAME", "DATE", "TIME"),yscrollcommand=sideBar.set,height=500)
        #topBtmsbar.pack(side=BOTTOM, fill=X)
        sideBar.pack(side=RIGHT, fill=Y)
        #topBtmsbar.config(command=self.detailtbl.xview)
        sideBar.config(command=self.detailtbl.yview)

        self.detailtbl.heading("EMPLOYEE_ID", text="EMPLOYEE_ID")
        self.detailtbl.heading("NAME", text="NAME")
        self.detailtbl.heading("DATE", text="DATE")
        self.detailtbl.heading("TIME", text="TIME")
        self.detailtbl["show"] = "headings"
        self.detailtbl.column("EMPLOYEE_ID", width=100)
        self.detailtbl.column("NAME", width=150)
        self.detailtbl.column("DATE", width=100)
        self.detailtbl.column("TIME", width=100)

        self.detailtbl.pack(fill=BOTH, expand=0)
        self.fetch_data()
        # self.detailtbl.bind("<ButtonRelease>", self.get_cursor)

    def back(self):
        if(self.cam_start==1):
            root.destroy()
        else:
            messagebox.showwarning("WARNING","STOP THE CAMARA BEFORE GOING BACK", parent=self.root)
    def fetch_data(self):
        today = datetime.date.today()
        date1 = today.strftime("%Y-%m-%d")
        conn = mysql.connector.connect(user='adminuser', password='Akshay10', host='35.90.7.49', database='sas',
                                       port='3306')
        '''conn = mysql.connector.connect(user='root', password='password', host='localhost', database='sas', auth_plugin='caching_sha2_password')'''
        my_cursor = conn.cursor()
        my_cursor.execute("select * from attendance  WHERE DATE=%s", (date1,))
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.detailtbl.delete(*self.detailtbl.get_children())
            for i in data:
                self.detailtbl.insert("", END, values=i)
            conn.commit()

    def predict(img, model_path="face_liveness.onnx"):
        dummy_face = np.expand_dims(np.array(img, dtype=np.float32), axis=0) / 255.

        providers = ['CPUExecutionProvider']
        m = rt.InferenceSession(model_path, providers=providers)
        onnx_pred = m.run(['activation_5'], {"input": dummy_face})
        liveness_score = list(onnx_pred[0][0])[1]
        return liveness_score

    def stopcamara(self):
        self.cam_start=1
    def attnsmark(self):
        self.cam_start = 0
        face_cascade1 = cv2.CascadeClassifier('data\\haarcascade_frontalface_alt2.xml')

        today = datetime.date.today()

        date1 = today.strftime("%Y-%m-%d")
        conn = mysql.connector.connect(user='adminuser', password='Akshay10', host='35.90.7.49', database='sas',
                                       port='3306')

        '''conn = mysql.connector.connect(user='root', password='password', host='localhost', database='sas',
                                       auth_plugin=' caching_sha2_password')'''
        my_cursor = conn.cursor()
        my_cursor.execute(("SELECT EMPLOYEE_ID FROM attendance WHERE DATE=%s"), (date1,))
        prev_attendance = my_cursor.fetchall()

        today = "ATTENDANCE/" + today.strftime("%d_%m_%Y") + ".csv"
        # prev_attendance=[]
        # curr_attendance=[]
        encodes = load('face.npy')
        labels = {}

        with open("labels.pickle", 'rb') as f:
            labels = pickle.load(f)

        """with open(today,'a+',encoding='UTF8',newline='')as file:
                writer=csv.writer(file)
                if os.path.getsize(today)==0:
                    writer.writerow(['ID','NAME','TIMING'])

        with open(today,'r+')as file:
            reader=csv.reader(file)
            for row in reader:
                prev_attendance.append(row)
            else:
                pass
        prev_attendance.pop(0)"""
        print(prev_attendance)

        cap = cv2.VideoCapture(1)
        while (True):
            flag = 0
            attendance_marked=0
            ret, frame = cap.read()
            #cv2.imshow("frame", frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face1 = face_cascade1.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=6)

            warnings.filterwarnings("ignore", category=DeprecationWarning)

            if face1 != ():
                for (x, y, w, h) in face1:
                    r_color = frame[y:y + h, x:x + w]
                    liveness = realpredict.predict(cv2.resize(r_color, (112, 112)))

                if liveness > 0.3:
                    cv2.imwrite('test.jpg', frame)
                    check_img = face_recognition.load_image_file('test.jpg')
                    try:
                        face_en = face_recognition.face_encodings(check_img)[0]
                    except IndexError as e:
                        continue
                    comparison = face_recognition.compare_faces(encodes, face_en, tolerance=0.5)
                    font = cv2.FONT_HERSHEY_SIMPLEX

                    for i in range(len(comparison)):
                        if comparison[i] == True:
                            flag = 1
                            emp_id = labels[i + 1][0]
                            emp_name = labels[i + 1][1]
                            timing = datetime.datetime.now()
                            time1 = timing.strftime("%H:%M:%S")

                            mark_attendance = (emp_id, emp_name, date1, time1)
                            for i in prev_attendance:
                                if (mark_attendance[0] == i[0]):
                                    mixer.init()
                                    mixer.music.load("audios\\already_marked.mp3")
                                    cv2.putText(frame,emp_name,(10,400),font,1,(0,0,0),2,cv2.LINE_AA)
                                    # check=cv2.cvtColor(check_img,cv2.COLOR_BGR2RGB)
                                    # cv2.imshow(emp_name,check);
                                    mixer.music.play()
                                    attendance_marked = 1
                                    break
                            else:
                                my_cursor.execute(("INSERT INTO attendance VALUES(%s, %s, %s, %s)"), mark_attendance)
                                conn.commit()
                                # curr_attendance.append(mark_attendance)
                                prev_attendance.append((emp_id,))
                                self.fetch_data()
                                mixer.init()
                                mixer.music.load("audios\\marked.mp3")
                                cv2.putText(frame, emp_name, (10, 400), font, 2, (0,0,0), 4, cv2.LINE_AA)
                                #check = cv2.cvtColor(check_img, cv2.COLOR_BGR2RGB)
                                #cv2.imshow(emp_name, check);
                                mixer.music.play()
                                # time.sleep(10)
                                attendance_marked=1

                                break
                    if (flag == 0):
                        mixer.init()
                        mixer.music.load("audios\\unknown.mp3")
                        cv2.putText(frame, "UNKNOWN", (10, 400), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
                        mixer.music.play()
            #cv2.imshow("frame", frame)
            frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame2 = ImageTk.PhotoImage(Image.fromarray(frame2).resize((700,500),Image.Resampling.LANCZOS))
            self.bg_img1["image"] = frame2
            root.update()
            if(attendance_marked==1):
                time.sleep(5)
            if self.cam_start==1:
                self.bg_img1["image"] = self.photoimg4
                root.update()
                break

        """print('current',curr_attendance)
        with open(today,'a+',encoding='UTF8',newline='')as file:
                writer=csv.writer(file)
                for i in curr_attendance:
                    writer.writerow(i)"""
        cap.release()
        cv2.destroyAllWindows()



if __name__ == '__main__':
    root = Tk()
    obj = realpredict(root)
    root.mainloop()