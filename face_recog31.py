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
from tkinter import ttk
import Image, ImageTk

class realpredict:
    def __init__(self, root):
        self.root = root
        root.state('zoomed')
        self.root.title("Attendance System")
        self.root.iconbitmap("img\\saslog.ico")

        img = Image.open("img\\pexels-ben-mack-6775241.jpg")
        img = img.resize((1530, 990), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        fstlbl = Label(self.root, image=self.photoimg)
        fstlbl.place(x=0, y=100, width=1530, height=990)

        # OOOOOOOOO

        img1 = Image.open("img\\6b77beffb8d54b09b7414bd72c07342e.png")
        img1 = img1.resize((100, 100), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        sndlbl = Label(self.root, image=self.photoimg1)
        sndlbl.place(x=0, y=0, width=100, height=100)

        img2 = Image.open("img\\flc_design2022053147056.png")
        img2 = img2.resize((300, 100), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img2)

        trdlbl = Label(self.root, image=self.photoimg3)
        trdlbl.place(x=620, y=0, width=300, height=100)

        head = Label(self.root, text="ATTENDANCE REPORT", font=("Tahoma", 25, "bold"), bg="black", fg="white")
        head.place(x=0, y=120, width=1530, height=40)
        back = customtkinter.CTkButton(self.root, text="Back", text_font=("Tahoma", 10, "bold"), bg_color="black",
                                       fg_color="#64b5f6", command=root.destroy)
        back.place(x=1200, y=126)

        frame = Frame(self.root, bd=2)
        frame.place(x=0, y=175, width=1530, height=650)

        RFrame1 = LabelFrame(self.root, bd=2, relief=RIDGE, font=("Tahoma", 12, "bold"), bg="#263238")
        RFrame1.place(x=0, y=180, width=1600, height=900)

        # viewtbl = customtkinter.CTkButton(RFrame1, command=self.import_csv, width=30, height=30, text="ATTENDANCE",
        #                                    text_font=("Tahoma", 10, "bold"), fg_color="#fb341c")
        # viewtbl.place(x=330, y=260)

        attnsbutton = customtkinter.CTkButton(RFrame1, command=self.attnsmark, width=625, height=30, text="ATTENDANCE",
                                              text_font=("Tahoma", 15, "bold"), fg_color="#fb341c")
        attnsbutton.place(x=730, y=290)

        down_frame = customtkinter.CTkFrame(RFrame1, bd=0, bg="White", relief=SUNKEN)
        down_frame.place(x=730, y=20, width=625, height=235)

        leftframe = customtkinter.CTkFrame(RFrame1)
        leftframe.place(x=10, y=20, width=650, height=450)

        img1 = Image.open("img\\featured_image-1.jpg")
        img1 = img1.resize((650, 450), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img1)
        self.bg_img1 = customtkinter.CTkLabel(leftframe, image=self.photoimg4, fg_color="black", bg_color="black")
        self.bg_img1.place(x=0, y=0)

        topBtmsbar = ttk.Scrollbar(down_frame, orient=HORIZONTAL)
        sideBar = ttk.Scrollbar(down_frame, orient=VERTICAL)

        self.detailtbl = ttk.Treeview(down_frame, columns=("EMPLOYEE_ID", "NAME", "DATE", "TIME"),
                                      xscrollcommand=topBtmsbar.set, yscrollcommand=sideBar.set)
        topBtmsbar.pack(side=BOTTOM, fill=X)
        sideBar.pack(side=RIGHT, fill=Y)
        topBtmsbar.config(command=self.detailtbl.xview)
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

    def attnsmark(self):
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
                                    # cv2.putText(check_img,"ATTENDANCE ALREADY MARKED",(10,400),font,1,(255,0,0),2,cv2.LINE_AA)
                                    # check=cv2.cvtColor(check_img,cv2.COLOR_BGR2RGB)
                                    # cv2.imshow(emp_name,check);
                                    mixer.music.play()
                                    break
                            else:
                                my_cursor.execute(("INSERT INTO attendance VALUES(%s, %s, %s, %s)"), mark_attendance)
                                conn.commit()
                                # curr_attendance.append(mark_attendance)
                                prev_attendance.append((emp_id,))
                                self.fetch_data()
                                mixer.init()
                                mixer.music.load("audios\\marked.mp3")
                                cv2.putText(frame, emp_name, (10, 400), font, 2, (255, 255, 255), 4, cv2.LINE_AA)
                                #check = cv2.cvtColor(check_img, cv2.COLOR_BGR2RGB)
                                #cv2.imshow(emp_name, check);
                                mixer.music.play()
                                # time.sleep(10)

                                break
                    if (flag == 0):
                        mixer.init()
                        mixer.music.load("audios\\unknown.mp3")
                        cv2.putText(frame, "UNKNOWN", (10, 400), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
                        mixer.music.play()
            #cv2.imshow("frame", frame)
            frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame2 = ImageTk.PhotoImage(Image.fromarray(frame2))
            self.bg_img1["image"] = frame2
            root.update()
            if cv2.waitKey(20) & 0xFF == ord('q'):
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

    """Warning (from warnings module):
      File "F:/2 SEM MCA/mini_project/project_face/face_recog1.py", line 46
        if face1 != ():
    DeprecationWarning: elementwise comparison failed; this will raise an error in the future.

    https://www.tutorialspoint.com/python-tkinter-how-to-export-data-from-entry-fields-to-a-csv-file
    """
