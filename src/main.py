from test_window import TestWindow
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)


w = TestWindow()
w.start_test()
w.run_window()

