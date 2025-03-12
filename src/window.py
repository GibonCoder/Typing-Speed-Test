import tkinter as tk


class Window:
    def __init__(self):
        # Window
        self.__root = tk.Tk()
        # Widgets
        self.__title = tk.Label(text="Test Your Typing Speed")
        self.__label_left = tk.Label(self.__root, fg='grey')
        self.__label_right = tk.Label(self.__root, fg='grey')
        # Variables
        self._split_point = 0
        self._text = None
        self._user_input = None

    def configure_window(self):
        self.__root.geometry("1200x800")
        self.__root.title("Speed Typing Test")

    def place_widgets(self):
        self.__title.grid(row=0, column=1)
        self.__label_left.place(relx=0.5, rely=0.5, anchor=tk.E)
        self.__label_right.place(relx=0.5, rely=0.5, anchor=tk.W)

    def run_window(self):
        self.__root.mainloop()

    def set_text(self, text):
        self._text = text['quote']
        self.__label_left.configure(text=self._text[0:self._split_point])
        self.__label_right.configure(text=self._text[self._split_point:])
