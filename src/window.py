import tkinter as tk
from tkinter import ttk


class Window:
    def __init__(self):
        # Window
        self.__root = tk.Tk()
        self.__title = ttk.Label(text="Test Your Typing Speed")
        # Variables
        self._text = None
        self._user_input = None

    def configure_window(self):
        self.__root.geometry("1200x800")
        self.__root.title("Speed Typing Test")

    def place_widgets(self):
        self.__title.grid(row=0, column=1)

    def run_window(self):
        self.__root.mainloop()

    def set_text(self, text):
        pass
