import tkinter as tk
from text_generator import TextGenerator
from speed_test import SpeedTest

tg = TextGenerator()


class TestWindow:
    def __init__(self):
        # Variables
        self._split_point = 0
        self._text = None
        self._user_input = None
        self.st = SpeedTest()
        # Window
        self.__root = tk.Tk()
        # Widgets
        self.__label_left = tk.Label(self.__root, fg='grey')
        self.__label_right = tk.Label(self.__root, fg='grey')
        self.__current_letter_label = tk.Label(self.__root, fg='black')
        self.__time_left_label = tk.Label(self.__root, fg='grey', text=f'0 Seconds')
        self.__result_label = tk.Label(self.__root, fg='black')
        self.__result_button = tk.Button(self.__root, text='Retry', command=self.restart)

    def _configure_window(self):
        self.__root.state('zoomed')
        self.__root.title("Speed Typing Test")

        self.__root.option_add("*Label.Font", "consolas 30")

        self.__root.bind('<Key>', self._key_pressed)

    def _place_widgets(self):
        self.__label_left.place(relx=0.5, rely=0.5, anchor=tk.E)
        self.__label_right.place(relx=0.5, rely=0.5, anchor=tk.W)
        self.__current_letter_label.place(relx=0.5, rely=0.6, anchor=tk.N)
        self.__time_left_label.place(relx=0.5, rely=0.4, anchor=tk.S)

    def run_window(self):
        self.__root.mainloop()

    def _set_text(self):
        text = tg.get_random_quote()
        self._text = text['body'].lower()
        self.__label_left.configure(text=self._text[0:self._split_point])
        self.__label_right.configure(text=self._text[self._split_point:])
        self.__current_letter_label.configure(text=self._text[self._split_point])

    # Adjust it
    def start_test(self):
        self._configure_window()
        self.st.config_time(self.__root, self.__time_left_label)
        self._set_text()
        self._place_widgets()

    def _stop_test(self):
        self._write_able = False

        wpm = self.st.stop_test(self.__label_left)

        self.__time_left_label.place_forget()
        self.__current_letter_label.place_forget()
        self.__label_right.place_forget()
        self.__label_left.place_forget()

        self.__result_label.configure(text=f'Words per Minute: {wpm}')
        self.__result_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.__result_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    def restart(self):
        self.__result_label.place_forget()
        self.__result_button.place_forget()

        self.st.restart_test()

        self.start_test()
