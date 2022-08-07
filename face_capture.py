import os
import boto3
import face_recognition
from botocore.exceptions import ClientError
from tkinter import messagebox
import cv2
from pygame import mixer
import warnings
from numpy import load
from numpy import save
from numpy import asarray


class facecap:
    def add_img(self, e_id, e_name, tu):
        global file_path, file, face
        access_key_id = 'AKIA3YJBIIAFWG56AJPE'
        secret_access_key = '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'
        bucket_name = 'smartauthorizingsys'
        client_s3 = boto3.client('s3', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
        flag = 0
        face_cascade1 = cv2.CascadeClassifier('data\\haarcascade_frontalface_alt2.xml')
        parent_dir = 'images\\'
        cap = cv2.VideoCapture(1)
        img_id = 0
        counter = 0
        face_encode = load('face.npy', allow_pickle=True)
        face_encodes=[]
        for i in face_encode:
            face_encodes.append(i)
        while True:
            ret, frame = cap.read()
            if counter > 10:
                face_cropped = ()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                face1 = face_cascade1.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
                warnings.filterwarnings("ignore", category=DeprecationWarning)
                if face1 != ():
                    for (leg, t, w, h) in face1:
                        leg -= 80
                        t -= 80
                        w += 150
                        h += 180
                        face_cropped = frame[t:t + h, leg:leg + w]
                    if face_cropped is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped, (450, 450))
                        file = str(e_id) + ".jpeg"
                        file_path = parent_dir + "/" + file
                        cv2.imwrite(file_path, face)

                        mixer.init()
                        flag = 1
            counter += 1
            #cv2.imshow("Frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q') or img_id >= 5:
                try:
                    client_s3.upload_file(file_path, bucket_name, file)
                    features = face_recognition.face_encodings(face)[0]
                    info = [e_id, e_name, features]
                    if tu == 1:
                        for j in range(0, len(face_encodes)):
                            if face_encodes[j][0] == e_id:
                                face_encodes.pop(j)
                                if(j<len(face_encodes)-1):
                                    face_encodes[j] = info
                                else:
                                    face_encodes.append(info)
                                break
                    else:
                        face_encodes.append(info)
                    face_en=asarray(face_encodes)
                    save('face.npy',face_en)
                    os.remove(file_path)
                except ClientError as e:
                    print(e)
                except Exception as e:
                    print(e)
                mixer.init()
                mixer.music.load("audios\\image_save.mp3")
                mixer.music.play()
                break
        if flag == 1:
            messagebox.showinfo("SUCCESS", "Image Successfully Saved")
        else:
            messagebox.showerror("Error", "Image Not Recognized")
        cap.release()
        cv2.destroyAllWindows()
