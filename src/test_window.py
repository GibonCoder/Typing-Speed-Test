import tkinter as tk
from text_generator import TextGenerator

tg = TextGenerator()


class TestWindow:
    def __init__(self):
        # Variables
        self._split_point = 0
        self._text = None
        self._user_input = None
        self._write_able = True
        self._passed_seconds = 0
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
        self.__root.geometry("700x700")
        self.__root.title("Speed Typing Test")

        self.__root.option_add("*Label.Font", "consolas 30")

        self.__root.bind('<Key>', self._key_pressed)

    def _configure_time(self):
        self.__root.after(30000, self._stop_test)
        self.__root.after(1000, self._add_second)

    def _place_widgets(self):
        self.__label_left.place(relx=0.5, rely=0.5, anchor=tk.E)
        self.__label_right.place(relx=0.5, rely=0.5, anchor=tk.W)
        self.__current_letter_label.place(relx=0.5, rely=0.6, anchor=tk.N)
        self.__time_left_label.place(relx=0.5, rely=0.4, anchor=tk.S)

    def run_window(self):
        self.__root.mainloop()

    def _set_text(self):
        text = tg.get_random_quote()
        self._text = text['quote'].lower()
        self.__label_left.configure(text=self._text[0:self._split_point])
        self.__label_right.configure(text=self._text[self._split_point:])
        self.__current_letter_label.configure(text=self._text[self._split_point])

    def start_test(self):
        self._configure_window()
        self._configure_time()
        self._set_text()
        self._place_widgets()

    def _stop_test(self):
        self._write_able = False

        amount_of_words = len(self.__label_left.cget('text').split(' '))

        self.__time_left_label.destroy()
        self.__current_letter_label.destroy()
        self.__label_right.destroy()
        self.__label_left.destroy()

        self.__result_label.configure(text=f'Words per Minute: {amount_of_words}')
        self.__result_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.__result_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    def restart(self):
        self.__result_label.destroy()
        self.__result_button.destroy()

        self._write_able = True
        self._passed_seconds = 0

        self.start_test()

    def _add_second(self):
        self._passed_seconds += 1
        self.__time_left_label.configure(text=f'{self._passed_seconds} Seconds')

        if self._write_able:
            self.__root.after(1000, self._add_second)

    def _key_pressed(self, event=None):
        try:
            if event.char.lower() == self.__label_right.cget('text')[0].lower():
                # Delete letter from the right side
                self.__label_right.configure(text=self.__label_right.cget('text')[1:])
                # Add letter to the left side
                self.__label_left.configure(text=self.__label_left.cget('text') + event.char.lower())
                # Set the next letter label
                self.__current_letter_label.configure(text=self.__label_right.cget('text')[0])
        except tk.TclError:
            pass
