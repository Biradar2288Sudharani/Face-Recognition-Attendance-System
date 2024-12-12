import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Back Button Example")
        self.geometry("300x200")

        # Create a container to hold frames
        self.container = ttk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Initialize frames
        self.frames = {}
        for F in (Main1, SecondPage):
            frame = F(parent=self.container, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the first page
        self.show_frame(Main1)

    def show_frame(self, frame_class):
        """Display the given frame."""
        frame = self.frames[frame_class]
        frame.tkraise()

class Main1(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ttk.Label(self, text="This is the First Page")
        label.pack(pady=10)

        next_button = ttk.Button(self, text="Next",command=lambda: controller.show_frame(SecondPage))
        next_button.pack()

class SecondPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ttk.Label(self, text="This is the Second Page")
        label.pack(pady=10)

        back_button = ttk.Button(self, text="Back",command=lambda: controller.show_frame(Main1))
        back_button.pack()

    

if __name__ == "__main__":
    app = App()
    app.mainloop()
