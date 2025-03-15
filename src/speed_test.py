class SpeedTest:
    def __init__(self):
        self._split_point = 0
        self._write_able = True
        self._passed_seconds = 0

    def config_time(self, window, time_lbl):
        self._passed_seconds = 0
        window.after(60000, self.stop_test)
        window.after(1000, lambda: self._add_second(window, time_lbl))

    def _add_second(self, window, time_lbl):
        self._passed_seconds += 1
        time_lbl.configure(text=f'{self._passed_seconds}')

        if self._write_able:
            window.after(1000, lambda: self._add_second(window, time_lbl))

    def stop_test(self, user_lbl):
        self._write_able = False

        amount_of_words = len(user_lbl.cget('text'.split(' ')))

        return amount_of_words

    def restart_test(self):
        self._write_able = True
        self._passed_seconds = 0
