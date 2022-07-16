import os
import pickle
import face_recognition
from numpy import save
from numpy import asarray
import mysql.connector

class train:
    def __init__(self):
        base_dir=os.path.dirname(os.path.abspath(__file__))
        image_dir=os.path.join(base_dir,"images")

        conn = mysql.connector.connect(user='adminuser', password='Akshay10', host='35.90.7.49', database='sas',port='3306')

        '''conn = mysql.connector.connect(user='root', password='password', host='localhost', database='sas',
                                       auth_plugin=' caching_sha2_password')'''
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT EMPLOYEE_ID,NAME FROM employee")
        data = my_cursor.fetchall()
        #print(data)
        current_ids=0
        label_ids={}
        face_en=[]

        for root,dir,files in os.walk(image_dir):
            #print(files)
            for file in files:
                if file.endswith("jpg") or file.endswith("jpeg"):
                    path=os.path.join(root,file)
                    label=data[current_ids]
                    #print(label,path)
                    current_ids+=1
                    label_ids[current_ids]=label[:2]
                    path=image_dir+"/"+file
                    img=face_recognition.load_image_file(path)
                    encode=face_recognition.face_encodings(img)[0]
                    #print(encode)
                    face_en.append(encode)
        #print(face_en)
        #print("face1\n",face_en[0])
        face=asarray(face_en)
        save('face.npy',face)

        with open("labels.pickle",'wb') as f:
            pickle.dump(label_ids,f)

        print("TRAINNED SUCCESSFULLY.......")

