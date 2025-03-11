import tkinter as tk
from tkinter import ttk


class Window:
    def __init__(self):
        self.__root = tk.Tk()
        self.__title = ttk.Label(text="Test Your Typing Speed")
        self.__text = tk.Text(state='disabled', width=125, height=20)
        self.__user_input = tk.Text(width=125, height=20)

    def configure_window(self):
        self.__root.geometry("1200x800")
        self.__root.title("Speed Typing Test")

    def place_widgets(self):
        self.__title.grid(row=0, column=1)
        self.__text.grid(row=1, column=1)
        self.__user_input.grid(row=2, column=1)

    def run_window(self):
        self.__root.mainloop()