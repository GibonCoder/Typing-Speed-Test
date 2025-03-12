import tkinter as tk
from tkinter import ttk


class Window:
    def __init__(self):
        # Window
        self.__root = tk.Tk()
        # Widgets
        self.__title = ttk.Label(text="Test Your Typing Speed")
        __label_left = tk.Label(self.__root, fg='grey')
        __label_right = tk.Label(self.__root, fg='grey')
        # Variables
        self._split_point = 0
        self._text = None
        self._user_input = None

    def configure_window(self):
        self.__root.geometry("1200x800")
        self.__root.title("Speed Typing Test")

    def place_widgets(self):
        self.__title.grid(row=0, column=1)
        self.

    def run_window(self):
        self.__root.mainloop()

    def set_text(self, text):
        pass
