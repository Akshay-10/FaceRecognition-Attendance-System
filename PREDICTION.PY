import cv2
import numpy as ny
import os
import pytesseract
import warnings
import datetime
import csv
import pandas as pd
from tkinter import ttk
from PIL import Image, ImageTk
import PIL.Image
import customtkinter
from tkinter import *
from tkinter import ttk, messagebox
import boto3
from botocore.exceptions import ClientError

class carpredict:
    def __init__(self,root):
        customtkinter.set_default_color_theme("sweetkind")
        self.root=root
        self.root.state('zoomed')
        self.root.title('Number Plate Recognition')
        self.root.overrideredirect(True)
        self.cam_start = 1
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
        back = customtkinter.CTkButton(self.root, text="Back", text_font=("Tahoma", 10, "bold"), bg_color="#263238",
                                       fg_color="#64b5f6",command=self.back,cursor="hand2")
        back.place(x=1200, y=126)

        frame = Frame(self.root, bd=2)
        frame.place(x=0, y=175, width=1530, height=650)

        RFrame1 = LabelFrame(self.root, bd=2, relief=RIDGE, font=("Tahoma", 12, "bold"), bg="#263238")
        RFrame1.place(x=0, y=180, width=1600, height=900)

        leftframe = customtkinter.CTkFrame(RFrame1)
        leftframe.place(x=10, y=20, width=700, height=450)

        img10 = PIL.Image.open("img\\play.png")
        img10= img10.resize((700, 450), PIL.Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img10)
        self.bg_img1 = customtkinter.CTkLabel(leftframe, image=self.photoimg4, fg_color="black", bg_color="black")
        self.bg_img1.place(x=0, y=0)

        startcam = customtkinter.CTkButton(RFrame1, command=self.cplt, width=300, height=30, text="START CAMARA",
                                           text_font=("Tahoma", 15), fg_color="#fb341c", cursor="hand2")
        startcam.place(x=50, y=550)

        stopcam = customtkinter.CTkButton(RFrame1, command=self.stopcamara, width=300, height=30, text="STOP CAMARA",
                                          text_font=("Tahoma", 15), fg_color="#fb341c", cursor="hand2")
        stopcam.place(x=400, y=550)

        down_frame = customtkinter.CTkFrame(RFrame1,bg_color="#263238")
        down_frame.place(x=730, y=20, width=625, height=450)
        detected = PIL.Image.open("img\\featured_image-1.jpg")
        detected = detected.resize((700, 450), PIL.Image.Resampling.LANCZOS)
        self.detected_car = ImageTk.PhotoImage(detected)
        self.detect_vehicle = customtkinter.CTkLabel(down_frame,image=self.detected_car, fg_color="black", bg_color="black")
        self.detect_vehicle.place(x=0, y=0,height=450,width=625)

    def back(self):
        if(self.cam_start==1):
            self.root.destroy()
        else:
            messagebox.showwarning("WARNING","STOP THE CAMARA BEFORE GOING BACK", parent=self.root)

    def stopcamara(self):
        self.cam_start = 1

    def get_dedect(self,img, mod):
        INPUT_WIDTH = 640
        INPUT_HEIGHT = 640
        image = img.copy()
        row, col, d = image.shape
        max_rc = max(row, col)  # it store the maximum value of row and column
        input_image = ny.zeros((max_rc, max_rc, 3), dtype=ny.uint8)
        input_image[0:row, 0:col] = image
        # the above statement is used to convert image into yolo format.
        # photo la mela image and kila blank ah erukum ethu oda output.

        blob = cv2.dnn.blobFromImage(input_image, 1 / 255, (INPUT_WIDTH, INPUT_HEIGHT), swapRB=True, crop=False)
        # input_image is a yolo format input,scale factor is 1/255,size of the image will set 640*640
        mod.setInput(blob)
        pred = mod.forward()  # pred.shape->eg:(1,25200,6)it will display the 3dimension input but we need 2dimension
        detect = pred[0]  # detect.shpaeso->eg:(25200,6),we convert into 2dimension eg:(25200,6)->(row,column) 6 is very important
        # centerX,centerY,width,heigth,confidence,probability score
        # (centerX,centerY,width,heigth)->info of bound box it is normalized by 640/640
        # confidence is basically define the detection confidence score.
        # probability score of the class.in our project we have one class that is license plate.
        return input_image, detect

    def non_maxi(self,input_image, detect):
        INPUT_WIDTH = 640
        INPUT_HEIGHT = 640
        boxes = []
        confidences = []
        img_w, img_h = input_image.shape[:2]  # it store the w,h of the yolo format image
        xfactor = img_w / INPUT_WIDTH
        yfactor = img_h / INPUT_HEIGHT
        for i in range(len(detect)):  # the detect has nearly 25220 rows and each row has 6 column.
            row = detect[i]  # each row come one by one
            confidence = row[4]  # The confidense is present in the fourth column so we assigning
            if confidence > 0.4:  # for good bounding box the confidence should be greater than 0.4
                class_score = row[5]  # class score is the probability score of the number plate
                # if print here the confidence it display few value among 225500 which confidence greater than 0.4.
                if class_score > 0.25:  # then we filter the class score is greater than 0.25 it reduce few value
                    cx, cy, w, h = row[0:4]
                    left = int((cx - 0.5 * w) * xfactor)
                    top = int((cy - 0.5 * h) * yfactor)
                    width = int(w * xfactor)
                    height = int(h * yfactor)
                    box = ny.array([left, top, width, height])
                    confidences.append(confidence)
                    boxes.append(box)
        # yolo give a multiple bounding boxes.so,we doing non maximum supresion
        nyboxes = ny.array(boxes).tolist()
        nyconfidences = ny.array(confidences).tolist()
        # the above 2 statement is cleaning our data by converting into list
        ind = cv2.dnn.NMSBoxes(nyboxes, nyconfidences, 0.25,0.45)  # it will give non repeateded bounding box and give exact number plate
        #print("index", ind)
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        if ind != ():
            index = ind.flatten()
            #print("flattern index", index)
            return nyboxes, nyconfidences, index
        else:
            return nyboxes, nyconfidences, ()

    def borders(self,image, nyboxes, nyconfidences, index):
        for i in index:
            x, y, w, h = nyboxes[i]
            bb_confi = nyconfidences[i]
            conf_text = 'plate: {:.0f}%'.format(bb_confi * 100)
            plate_text = self.extract_text(image, nyboxes[i])
            #print("hello", plate_text)
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 255), 2)  # 2 is a thickness
            cv2.rectangle(image, (x, y - 30), (x + w, y), (255, 0, 255), -1)
            cv2.rectangle(image, (x, y + h), (x + w, y + h + 30), (0, 0, 0), -1)

            cv2.putText(image, conf_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1)
            cv2.putText(image, plate_text, (x, y + h + 27), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 1)
            return image

    def predicts(self,img, mod):
        input_image, detect = self.get_dedect(img, mod)
        nyboxes, nyconfidences, index = self.non_maxi(input_image, detect)
        #print("1", index)
        if index != ():
            result_img = self.borders(img, nyboxes, nyconfidences, index)
            #print("result_img", result_img)
            return result_img
        else:
            return ()

    def extract_text(self,image, bbox):
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        x, y, w, h = bbox
        roi = image[y:y + h, x:x + w]
        if 0 in roi.shape:
            return ''
        else:
            text = pytesseract.image_to_string(roi)
            text = text.strip()
            text = ''.join(char for char in text if char.isalnum())
            if text != "" and text != " ":
                if text not in prev_attendance :
                    print("previous ",prev_attendance)
                    time1 = datetime.datetime.now()
                    time1 = time1.strftime("%Y-%m-%d %H:%M:%S.%f")
                    # time1 = time1.strftime("%H:%M:%S")
                    i = [text, time1, "00:00:00"]
                    entry_list.append(i)
                    prev_attendance.append(text)
                    print("after ",prev_attendance,"\nentry list ",entry_list)
                else:
                    x = prev_attendance.index(text)
                    time1 = datetime.datetime.now()
                    #time1 = time1.strftime("%Y-%m-%d %H:%M:%S.%f")
                    if time1 > datetime.datetime.strptime(entry_list[x][1],'%Y-%m-%d %H:%M:%S.%f') + pd.DateOffset(minutes=1):
                        entry_list[x][2] = time1
            return text
    def cplt(self):
        self.cam_start = 0
        today = datetime.date.today()
        today = "entry/" + today.strftime("%d_%m_%Y") + ".csv"
        #print(today)
        size = 0
        flag=0
        with open(today, 'a+') as file:
            writer = csv.writer(file)
            if os.path.getsize(today) == 0:
                writer.writerow(['VEHICLE_NUMBER', 'ENTRY_TIME', 'EXIT_TIME'])
                flag=1
            size = os.path.getsize(today)
        #print(os.path.getsize(today))
        global entry_list
        entry_list = []
        global prev_attendance
        prev_attendance = []

        with open(today, 'r+') as file:
            reader = csv.reader(file)
            if size > 28:
                for row in reader:
                    if row != [] and row[0]!='VEHICLE_NUMBER':
                        prev_attendance.append(row[0])
                        entry_list.append(row)
        with open(today, 'w') as file:
            writer=csv.writer(file)
            writer.writerow(['VEHICLE_NUMBER', 'ENTRY_TIME', 'EXIT_TIME'])
        mod = cv2.dnn.readNetFromONNX('best.onnx')  # mod store the model which is goiing to predict
        mod.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)  # set the backend for our model
        mod.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)  # set the target for our model
        # filter based on confidence,probability score
        cap = cv2.VideoCapture(1)
        while True:
            ret, frame = cap.read()

            if ret == False:
                print('unable to read video')
                break
            results = self.predicts(frame, mod)
            #print("results", results)
            if results != ():
                #cv2.namedWindow('YOLO', cv2.WINDOW_KEEPRATIO)
                #cv2.imshow('YOLO', results)
                frame2 = cv2.cvtColor(results, cv2.COLOR_BGR2RGB)
                frame2 = ImageTk.PhotoImage(
                    PIL.Image.fromarray(frame2).resize((700, 500), PIL.Image.Resampling.LANCZOS))
                self.detect_vehicle["image"] = frame2
                self.root.update()
            #cv2.imshow("frame", frame)

                # cv2.imshow("frame", frame)
            frame3 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame3 = ImageTk.PhotoImage(PIL.Image.fromarray(frame3).resize((700, 500), PIL.Image.Resampling.LANCZOS))
            self.bg_img1["image"] = frame3
            self.root.update()
            if self.cam_start == 1:
                self.bg_img1["image"] = self.photoimg4
                self.root.update()
                break

        with open(today, 'a+', encoding='UTF8', newline='') as file:
            writer = csv.writer(file)
            for i in entry_list:
                writer.writerow(i)

        Access_key_ID = 'AKIA3YJBIIAFWG56AJPE'
        Secret_access_key = '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'
        bucket_name = 'smartauthorizingsys'
        client_s3 = boto3.client('s3', aws_access_key_id=Access_key_ID, aws_secret_access_key=Secret_access_key)

        try:
            client_s3.upload_file('C:/Users/HP/PycharmProjects/FontendProjectH/entry/08_08_2022.csv',
                                  'sasvehicle', '08_08_2022.csv')
        except ClientError as e:
            print(e)
        except Exception as e:
            print(e)
        if flag==1:
            os.remove('C:/Users/HP/PycharmProjects/FontendProjectH/entry/07_08_2022.csv')

        cv2.destroyAllWindows()
        cap.release()

if __name__ == '__main__':
    root = Tk()
    obj = carpredict(root)
    root.mainloop()