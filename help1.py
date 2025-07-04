from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser  # ✅ Importing webbrowser module to open links
import os

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")

        # Function to open URLs
        def open_url(url):
            webbrowser.open(url)

        # Title name
        title_lbl = Label(self.root, text="Help Desk", font=("times new roman", 35, "bold"), bg="black", fg="red")
        title_lbl.place(x=0, y=0, width=1366, height=55)

        back_btn = Button(title_lbl, text="Back Button", borderwidth=0, cursor="hand2", font=("times new roman", 18, "bold"), bg="blue", fg="white")  
        back_btn.place(x=1200, y=8, width=145, height=30)
        
        # Top Left Image (WhatsApp)
        top_left_img = Image.open(r"C:college_images\hd.png").resize((683, 325))
        self.photoimage_top_left = ImageTk.PhotoImage(top_left_img)
        Label(self.root, image=self.photoimage_top_left).place(x=0, y=55, width=683, height=325)

        # WhatsApp Call logo
        call_logo_img = Image.open(r"C:college_images\Wh.png").resize((40, 40))
        self.photoimage_call_logo = ImageTk.PhotoImage(call_logo_img)
        Label(self.root, image=self.photoimage_call_logo).place(x=180, y=195, width=40, height=40)

        # WhatsApp Number (Clickable with Underline)
        phone_num = Button(self.root, text="Mobile Number", font=("times new roman", 20, "bold", "underline"), bg="black", fg="pink", borderwidth=0, cursor="hand2", command=lambda: open_url("https://wa.me/7709298002"))
        phone_num.place(x=230, y=204, width=270, height=30)

        # Top Right Image (LinkedIn)
        top_right_img = Image.open(r"C:college_images\hd.png").resize((683, 325))
        self.photoimage_top_right = ImageTk.PhotoImage(top_right_img)
        Label(self.root, image=self.photoimage_top_right).place(x=683, y=55, width=683, height=325)

        # LinkedIn Logo
        linkdin_logo_img = Image.open(r"C:college_images\l.png").resize((40, 40))
        self.photoimage_linkdin_logo = ImageTk.PhotoImage(linkdin_logo_img)
        Label(self.root, image=self.photoimage_linkdin_logo).place(x=860, y=200, width=40, height=40)

        # LinkedIn Profile (Clickable with Underline)
        linkdin_id = Button(self.root, text="LinkedIn Profile", font=("times new roman", 20, "bold", "underline"), bg="black", fg="orange", borderwidth=0, cursor="hand2", command=lambda: open_url("https://www.linkedin.com/in/sudharani-biradar-40b280278"))
        linkdin_id.place(x=910, y=205, width=270, height=30)

        # Bottom Left Image (GitHub)
        bottom_left_img = Image.open(r"C:college_images\hd.png").resize((683, 325))
        self.photoimage_bottom_left = ImageTk.PhotoImage(bottom_left_img)
        Label(self.root, image=self.photoimage_bottom_left).place(x=0, y=380, width=683, height=325)

        # GitHub Logo
        github_logo_img = Image.open(r"C:college_images\g.png").resize((50, 50))
        self.photoimage_github_logo = ImageTk.PhotoImage(github_logo_img)
        Label(self.root, image=self.photoimage_github_logo).place(x=180, y=515, width=50, height=50)

        # GitHub Profile (Clickable with Underline)
        github_id = Button(self.root, text="GitHub Profile", font=("times new roman", 20, "bold", "underline"), bg="black", fg="blue", borderwidth=0, cursor="hand2", command=lambda: open_url("https://github.com/Biradar2288Sudharani"))
        github_id.place(x=240, y=530, width=270, height=30)

        # Bottom Right Image (Email)
        bottom_right_img = Image.open(r"C:college_images\hd.png").resize((683, 325))
        self.photoimage_bottom_right = ImageTk.PhotoImage(bottom_right_img)
        Label(self.root, image=self.photoimage_bottom_right).place(x=683, y=380, width=683, height=325)

        # Email Logo
        email_logo_img = Image.open(r"C:college_images\e2.png").resize((40, 40))
        self.photoimage_email_logo = ImageTk.PhotoImage(email_logo_img)
        Label(self.root, image=self.photoimage_email_logo).place(x=880, y=525, width=40, height=40)

        # Email (Clickable with Underline)
        email_id = Button(self.root, text="Email ID", font=("times new roman", 20, "bold", "underline"), bg="black", fg="purple", borderwidth=0, cursor="hand2", command=lambda: open_url("mailto:sudharanibiradar970@gmail.com"))
        email_id.place(x=930, y=530, width=270, height=30)

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
