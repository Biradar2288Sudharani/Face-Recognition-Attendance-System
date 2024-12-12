from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        # Title label
        # Title name given
        title_lbl=Label(self.root,text="Face Recognition",font=("times new roman",35,"bold"),bg="black",fg="red")
        title_lbl.place(x=0,y=0,width=1366,height=50)
        #title_lbl = Label(self.root, text="Face Recognition", font=("times new roman", 35, "bold"), bg="white", fg="purple")
        #title_lbl.place(x=0, y=0, width=1366, height=40)

        # Right image
        img_right = Image.open(r"C:\Users\lenovo\Desktop\Face_Recognisation_System\Images\fr2.png")
        img_right = img_right.resize((1366, 710))
        self.photoimage_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(self.root, image=self.photoimage_right)
        f_lbl.place(x=0, y=50, width=1366, height=710)

        # Face Recognition Button
        btn_lbl = Button(self.root, text="Face Recognition", cursor="hand2", font=("times of new roman", 15, "bold"), bg="red", fg="white", command=self.face_recog)
        btn_lbl.place(x=340, y=620, width=200, height=40)

    # Face Recognition Logic
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", user="root", password="Shankar2sep@", database="face_recognition",auth_plugin="mysql_native_password")
                my_cursor = conn.cursor(buffered=True)
                
                my_cursor.execute("SELECT Name, `Roll No`, Department FROM student WHERE StudentID = %s", (id,))
                data = my_cursor.fetchone()
                
                if data and confidence > 77:
                    name, roll_no, dept = data
                    cv2.putText(img, f"Roll No:{roll_no}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{dept}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    #self.mark_attendance(id, roll_no, name, dept)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 0, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"C:\Users\lenovo\Desktop\Face_Recognisation_System\classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break
        
        video_cap.release()
        cv2.destroyAllWindows()

# Initialize and run the GUI
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
