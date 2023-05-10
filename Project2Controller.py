from timerProject2 import *
from alarmProject2 import *
from stopwatchProject2 import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(Timer,Alarm,Stopwatch):
    def __init__(self):
        '''
        Constructor to create initial state of a Controller object.
        Inherits the objects Timer, Alarm, and Stopwatch
        Contains the logic for buttons
        '''
        super().__init__()
        self.startBtn.clicked.connect(lambda: self.startTimer())
        self.pauseBtn.clicked.connect(lambda: self.pauseTimer())
        self.resetBtn.clicked.connect(lambda: self.resetTimer())

        self.stopwatchStartStopBtn.clicked.connect(lambda:self.start_or_stop_Watch())
        self.lapBtn.clicked.connect(lambda:self.lap_stopwatch())
        self.stopwatchReset_btn.clicked.connect(lambda:self.reset_stopwatch())

        self.alarmSetBtn.clicked.connect(lambda:self.set_alarm())
        self.cancelAlarmBtn.clicked.connect(lambda:self.cancel_alarm())

        self.tab_widget.currentChanged.connect(self.reset_tabs)

    def reset_tabs(self):
        '''
        This method will help reset the tabs everytime the user switches tabs.
        '''
        self.resetTimer()
        self.reset_stopwatch()
        self.cancel_alarm()