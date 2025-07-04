from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")

        # Title Label
        title_lbl = Label(self.root, text="Face Recognition", font=("times new roman", 35, "bold"), bg="black", fg="red")
        title_lbl.place(x=0, y=0, width=1366, height=50)

        back_btn=Button(title_lbl,text="Back Button",borderwidth=0,cursor="hand2",font=("times new roman",18,"bold"),bg="blue",fg="white")  # return_login
        back_btn.place(x=1200,y=8,width=145,height=30)

        # Background Image
        img_right = Image.open(r"C:college_images\fr2.png")
        img_right = img_right.resize((1366, 710))
        self.photoimage_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(self.root, image=self.photoimage_right)
        f_lbl.place(x=0, y=50, width=1366, height=710)

        # Face Recognition Button
        btn_lbl = Button(self.root, text="Face Recognition", cursor="hand2", font=("times of new roman", 15, "bold"), bg="red", fg="white", command=self.face_recog)
        btn_lbl.place(x=340, y=620, width=200, height=40)

    # **************** Attendance Store in CSV File Logic ******************
    def mark_attendance(self, id, phoneno, name, dept):
        # Create Attendance_Report directory if it doesn't exist
        if not os.path.exists("Attendance_Report"):
            os.makedirs("Attendance_Report")

        file_path = "Attendance_Report/sudha.csv"

        # Create CSV file with headers if it doesn't exist
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write("StudentID,Phone Number,Name,Department,Time,Date,Status\n")

        try:
            with open(file_path, "r+", newline="\n") as f:
                myDataList = f.readlines()
                today = datetime.now().strftime("%d/%m/%Y")
                existing_attendance = set()  # Use a set to track marked attendance

                # Collect already marked attendance
                for line in myDataList:
                    entry = line.strip().split(",")
                    if len(entry) >= 5 and entry[4] == today:  # Check if attendance is for today
                        existing_attendance.add(entry[0])  # Add StudentID to the set

                # Mark attendance if not already marked
                if str(id) not in existing_attendance:
                    now = datetime.now()
                    time = now.strftime("%H:%M:%S")
                    date = now.strftime("%d/%m/%Y")
                    f.write(f"{id},{phoneno},{name},{dept},{time},{date},Present\n")
                    print(f"Attendance marked for StudentID: {id}, Phone Number: {phoneno}, Name: {name}, Department: {dept}")
        except Exception as e:
            print(f"Error writing attendance: {e}")


    # ************************ Face Recognition Logic ************************
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="Shankar2sep@",
                        database="face_recognition",
                        auth_plugin="mysql_native_password"
                    )
                    my_cursor = conn.cursor(buffered=True)
                    my_cursor.execute("SELECT Name, `Phone Number`, Department FROM student WHERE StudentID = %s", (id,))
                    data = my_cursor.fetchone()
                    conn.close()

                    if data and confidence > 77:
                        name, phoneno, dept = data
                        cv2.putText(img, f"StudentID:{id}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Phone Number:{phoneno}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Name:{name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Department:{dept}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                        # Call attendance marking function
                        self.mark_attendance(id, phoneno, name, dept)
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                except Exception as e:
                    print(f"Error accessing database: {e}", parent=self.root)

        def recognize(img, clf, faceCascade):
            draw_boundary(img, faceCascade, 1.1, 10, (255, 0, 255), "Face", clf)
            return img

        # Load pre-trained face detection model
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        # Load pre-trained recognizer model
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"C:\\Users\\lenovo\\Desktop\\Face_Recognition_System\\classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(0) == 13:  # Press 'Enter' to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()
        

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
