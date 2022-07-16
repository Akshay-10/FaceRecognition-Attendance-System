import os
from tkinter import messagebox
import cv2
from pygame import mixer
import warnings
from face_train import train

class facecap:
    def upimg(self,e_id):
        parent_dir = 'images\\'
        filepath=parent_dir+str(e_id)+".jpeg"
        os.remove(filepath)
    def add_img(self,e_id,i):
        flag=0
        face_cascade1 = cv2.CascadeClassifier('data\\haarcascade_frontalface_alt2.xml')
        parent_dir = 'images\\'
        cap = cv2.VideoCapture(1)
        img_id = 0
        while True:
            ret, frame = cap.read()
            face_cropped = ()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face1 = face_cascade1.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            if face1 != ():
                if(i==1):
                    facecap.upimg(self,e_id)
                for (l, t, w, h) in face1:
                    l -= 80
                    t -= 80
                    w += 150
                    h += 180
                    face_cropped = frame[t:t + h, l:l + w]
                if face_cropped is not None:
                    img_id += 1
                    face = cv2.resize(face_cropped, (450, 450))
                    file_path = parent_dir + "\\" + str(e_id) + ".jpeg"
                    cv2.imwrite(file_path, face)
                    mixer.init()

                    flag=1

            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q') or img_id >= 5:
                mixer.init()
                mixer.music.load("audios\\image_save.mp3")
                mixer.music.play()
                break
        if (flag == 1):
            messagebox.showinfo("SUCCESS", "Image Successfully Saved")
            obj=train()
            obj.__init__()
        else:
            messagebox.showerror("Error", "Image Not Recognized")
        cap.release()
        cv2.destroyAllWindows()