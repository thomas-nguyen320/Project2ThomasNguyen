from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont
from Project2View import *


class Stopwatch(QMainWindow,Ui_MainWindow):
    def __init__(self, *args, **kwargs) -> None:
        '''
        Constructor to create initial state of a Stopwatch object.
        '''
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.stopwatch_hr = 0
        self.stopwatch_min = 0
        self.stopwatch_sec = 0
        self.stopwatch_tenthsec = 0

        self.lap_hr = 0
        self.lap_min = 0
        self.lap_sec = 0
        self.lap_tenthsec = 0
        self.stopwatch_started = False

        # The bottom two lines of codes will help me make a timer that updates the current time while letting us use the other functions.
        self.stopwatch_timer = QTimer()
        self.stopwatch_timer.timeout.connect(self.update_stopwatch)

    def start_or_stop_Watch(self) -> None:
        '''
        This method will start the stopwatch.
        '''
        self.stopwatch_started = not self.stopwatch_started
        if self.stopwatch_started:
            self.stopWatch_label.setText('00:00:00')
            self.stopWatch_label.setFont(QFont('Arial', 35))
            self.stopwatch_timer.start(10)
        else:
            self.stopwatch_timer.stop()

    def update_stopwatch(self) -> None:
        '''
        This method updates the current time and current lap of the stopwatch continously.
        '''
        self.stopwatch_tenthsec +=1
        self.lap_tenthsec += 1

        if self.stopwatch_tenthsec > 99:
            self.stopwatch_tenthsec = 0
            self.stopwatch_sec += 1
        if self.lap_tenthsec > 99:
            self.lap_tenthsec = 0
            self.lap_sec += 1

        if self.stopwatch_sec > 59:
            self.stopwatch_sec = 0
            self.stopwatch_min += 1
        if self.lap_sec > 59:
            self.lap_sec = 0
            self.lap_sec += 1

        if self.stopwatch_min > 59:
            self.stopwatch_min = 0
            self.stopwatch_hr += 1
        if self.lap_min > 59:
            self.lap_min = 0
            self.lap_min += 1

        self.stopWatch_label.setText(f'{self.stopwatch_hr:02}:{self.stopwatch_min:02}:{self.stopwatch_sec:02}.{self.stopwatch_tenthsec:02}')
        self.display_laptext.setText(f'Lap {self.laps}: {self.lap_hr:02}:{self.lap_min:02}:{self.lap_sec:02}.{self.lap_tenthsec:02}')

    def lap_stopwatch(self) -> None:
        '''
        This method will let the user be able to store their time they lapped into a text box if the stopwatch is started.
        '''
        try:
            if self.stopwatch_started:
                lap_time = f'{self.lap_hr:02}:{self.lap_min:02}:{self.lap_sec:02}.{self.lap_tenthsec:02}'
                self.lap_text.append(f'Lap {self.laps}: {lap_time}')
                self.lap_hr = 0
                self.lap_min = 0
                self.lap_sec = 0
                self.lap_tenthsec = 0
                self.laps += 1
            else:
                raise TypeError

        except TypeError:
            self.stopWatch_label.setFont(QFont('Arial',10))
            self.stopWatch_label.setText('Cannot lap, timer not started, reset or press start')

    def reset_stopwatch(self) -> None:
        '''
        This method will reset the stopwatch to its default values and stop the timer.
        '''
        self.stopwatch_hr = 0
        self.stopwatch_min = 0
        self.stopwatch_sec = 0
        self.stopwatch_tenthsec = 0
        self.lap_hr = 0
        self.lap_min = 0
        self.lap_sec = 0
        self.lap_tenthsec = 0
        self.laps = 1
        self.stopWatch_label.setFont(QFont('Arial', 35))
        self.stopWatch_label.setText('00:00:00')
        self.display_laptext.setText('')
        self.lap_text.clear()
        self.stopwatch_timer.stop()
        self.stopwatch_started = False


