import tkinter as tk
from tkinter import ttk


class Window:
    def __init__(self):
        self.__root = tk.Tk()

    def __configure_window(self):
        self.__root.geometry("1200x800")
        self.__root.title("Speed Typing Test")
