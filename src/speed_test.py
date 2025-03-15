class SpeedTest:
    def __init__(self):
        self._split_point = 0
        self._write_able = True
        self._passed_seconds = 0

    def config_time(self, window):
        self._passed_seconds = 0
        window.after(60000, self._stop_test)
        window.after(1000, self._add_second)
