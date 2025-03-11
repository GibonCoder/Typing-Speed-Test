import tkinter as tk
from tkinter import ttk


class Window:
    def __init__(self):
        self.__root = tk.Tk()
        self.__title = ttk.Label(text="Test Your Typing Speed")
        self.__text = tk.Text(state='disabled')
        self.__user_input = tk.Text()

    def __configure_window(self):
        self.__root.geometry("1200x800")
        self.__root.title("Speed Typing Test")

    def __place_widgets(self):
        pass


