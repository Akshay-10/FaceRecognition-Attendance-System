import cv2
import numpy as ny
import os
import pytesseract
import warnings
import datetime
import csv
import pandas as pd
from tkinter import ttk
from PIL import Image,ImageTk
import customtkinter
import Image, ImageTk
from tkinter import *

class carpredict:
    '''def __init__(self, root):
        self.root = root
        root.state('zoomed')
        self.root.title("VEHICLE ENTRY SYSTEM")
        self.root.iconbitmap("img\\saslog.ico")
        img = Image.open("img\\pexels-ben-mack-6775241.jpg")
        img = img.resize((1530, 990), Image.ANTIALIAS)
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

        attnsbutton = customtkinter.CTkButton(RFrame1, command=self.cplt, width=625, height=30, text="START",
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

        self.detailtbl = ttk.Treeview(down_frame, columns=("VEHICLE NUMBER", "ENTRY TIME"),
                                      xscrollcommand=topBtmsbar.set, yscrollcommand=sideBar.set)
        topBtmsbar.pack(side=BOTTOM, fill=X)
        sideBar.pack(side=RIGHT, fill=Y)
        topBtmsbar.config(command=self.detailtbl.xview)
        sideBar.config(command=self.detailtbl.yview)

        self.detailtbl.heading("VEHICLE NUMBER", text="VEHICLE NUMBER")
        self.detailtbl.heading("ENTRY TIME", text="ENTRY TIME")
        self.detailtbl["show"] = "headings"
        self.detailtbl.column("VEHICLE NUMBER", width=150)
        self.detailtbl.column("ENTRY TIME", width=100)

        self.detailtbl.pack(fill=BOTH, expand=0)
        #self.fetch_data()
        # self.detailtbl.bind("<ButtonRelease>", self.get_cursor)'''

    def cplt(self):
        today = datetime.date.today()
        today = "entry/" + today.strftime("%d_%m_%Y") + ".csv"
        print(today)
        size = 0
        with open(today, 'a+') as file:
            writer = csv.writer(file)
            if os.path.getsize(today) == 0:
                writer.writerow(['VEHICLE_NUMBER', 'ENTRY_TIME', 'EXIT_TIME'])
            size = os.path.getsize(today)
        print(os.path.getsize(today))
        entry_list = []
        prev_attendance = []

        with open(today, 'r+') as file:
            reader = csv.reader(file)
            if size > 28:
                for row in reader:
                    if row != []:
                        prev_attendance.append(row[0])

        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

        INPUT_WIDTH = 640
        INPUT_HEIGHT = 640

        mod = cv2.dnn.readNetFromONNX('./Model/weights/best.onnx')  # mod store the model which is goiing to predict
        mod.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)  # set the backend for our model
        mod.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)  # set the target for our model

        def get_dedect(img, mod):
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
            detect = pred[
                0]  # detect.shpaeso->eg:(25200,6),we convert into 2dimension eg:(25200,6)->(row,column) 6 is very important
            # centerX,centerY,width,heigth,confidence,probability score
            # (centerX,centerY,width,heigth)->info of bound box it is normalized by 640/640
            # confidence is basically define the detection confidence score.
            # probability score of the class.in our project we have one class that is license plate.
            return input_image, detect

        # filter based on confidence,probability score
        def non_maxi(input_image, detect):
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
            ind = cv2.dnn.NMSBoxes(nyboxes, nyconfidences, 0.25,
                                   0.45)  # it will give non repeateded bounding box and give exact number plate
            print("index", ind)
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            if ind != ():
                index = ind.flatten()
                print("flattern index", index)
                return nyboxes, nyconfidences, index
            else:
                return nyboxes, nyconfidences, ()

        def borders(image, nyboxes, nyconfidences, index):
            for i in index:
                x, y, w, h = nyboxes[i]
                bb_confi = nyconfidences[i]
                conf_text = 'plate: {:.0f}%'.format(bb_confi * 100)
                plate_text = extract_text(image, nyboxes[i])
                print("hello", plate_text)
                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 255), 2)  # 2 is a thickness
                cv2.rectangle(image, (x, y - 30), (x + w, y), (255, 0, 255), -1)
                cv2.rectangle(image, (x, y + h), (x + w, y + h + 30), (0, 0, 0), -1)

                cv2.putText(image, conf_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1)
                cv2.putText(image, plate_text, (x, y + h + 27), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 1)
                return image

        def predicts(img, mod):
            input_image, detect = get_dedect(img, mod)
            nyboxes, nyconfidences, index = non_maxi(input_image, detect)
            print("1", index)
            if index != ():
                result_img = borders(img, nyboxes, nyconfidences, index)
                print("result_img", result_img)
                return result_img
            else:
                return ()

        def extract_text(image, bbox):
            x, y, w, h = bbox
            roi = image[y:y + h, x:x + w]
            if 0 in roi.shape:
                return ''
            else:
                # reader=easyocr.Reader(['en'])
                # text=reader.readtext(roi)
                text = pytesseract.image_to_string(roi)
                text = text.strip()
                text = ''.join(char for char in text if char.isalnum())
                i = []
                prev_entry=[]
                if text != "" and text != " ":
                    if text in prev_attendance:
                        x = prev_attendance.index(text)
                        time1 = datetime.datetime.now()
                        print(prev_attendance,x)
                        if time1 > prev_entry[x] + pd.DateOffset(minutes=2):
                            time1 = time1.strftime("%H:%M:%S")
                            i[x][-1] += time1

                    if text not in prev_attendance:
                        time11 = datetime.datetime.now()
                        time1 = time11.strftime("%H:%M:%S")
                        i = [text, time1, ' ']
                        entry_list.append(i)
                        prev_attendance.append(text)
                        prev_entry.append(time11)
                        print(i)
                return text

        cap = cv2.VideoCapture(1)
        while True:
            ret, frame = cap.read()

            if ret == False:
                print('unable to read video')
                break
            results = predicts(frame, mod)
            print("results", results)
            if results != ():
                cv2.namedWindow('YOLO', cv2.WINDOW_KEEPRATIO)
                cv2.imshow('YOLO', results)
            cv2.imshow("frame", frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
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

