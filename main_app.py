import tkinter as tk
from tkinter import ttk
from upper_frame import UpperFrame

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x1000")
        self.title("Code Generator")
        self.create_widgets()
            
    def create_widgets(self):
        self.upper_frame = UpperFrame(self)
        self.upper_frame.pack(side="top", fill="both", expand=True)


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()