from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from Project2View import *
from datetime import datetime

class Timer(QMainWindow,Ui_MainWindow):
    def __init__(self, *args, **kwargs) -> None:
        '''
        Constructor to create initial state of a Timer object.
        '''
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.seconds_left = 0
        self.minutes_left = 0
        self.hours_left = 0
        self.time_in_sec = 0
        self.paused = False
        self.started = False
        self.time_of_day = 'A.M'

        #The bottom two lines of codes will help me make a timer that updates the current time while letting us use the other functions.
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

    def timeConversion(self, hour: int, min: int, sec: int) -> None:
        '''
        This method will help convert the time from military time to a standard 12-hour time clock.

        :param hour: This is the hour that will be used to convert to the future time.
        :param min: This is the minutes that will be used to convert to the future time.
        :param sec: This is the seconds that will be used to convert to the future time.
        '''
        self.now = datetime.now()
        self.current_hour = int(self.now.strftime("%H"))
        self.current_min = int(self.now.strftime("%M"))
        self.current_sec = int(self.now.strftime("%S"))
        future_hour = (hour + self.current_hour)
        future_min = (min + self.current_min)
        future_sec = (sec + self.current_sec)
        if future_min >= 60:
            future_min -= 60
            future_hour += 1
        if future_sec >= 60:
            future_sec -= 60
            future_min += 1
        if future_hour >= 24:
            future_hour %= 24

        if future_hour >= 13 and future_hour <= 23:
            self.time_of_day = 'P.M.'
            future_hour -= 12
        elif future_hour == 12:
            self.time_of_day = 'P.M.'
        elif future_hour >= 1 and future_hour <= 11:
            self.time_of_day = 'A.M.'
        elif future_hour == 0:
            self.time_of_day = 'A.M.'
            future_hour += 12

        self.done_label.setText(
            f'Timer done at:{future_hour:02}:{future_min:02}:{future_sec:02} {self.time_of_day}')

    def startTimer(self) -> None:
        '''
        This method will start the timer.
        '''
        self.started = True
        self.paused = False

        if self.paused == False:
            try:
                if int(self.hourInp_2.text()) == 0 and int(self.minInp_2.text()) == 0 and int(self.secInp_2.text()) == 0:
                    raise TypeError

                elif (int(self.hourInp_2.text()) >= 0 and int(self.hourInp_2.text()) <= 24) and (
                        int(self.minInp_2.text()) >= 0 and int(self.minInp_2.text()) <= 59) and (
                        int(self.secInp_2.text()) >= 0 and int(self.secInp_2.text()) <= 59):
                    self.error_label.setText('')
                    hour = int(self.hourInp_2.text())
                    min = int(self.minInp_2.text())
                    sec = int(self.secInp_2.text())
                    self.timeConversion(hour, min, sec)
                    self.time_in_sec = hour * 3600 + min * 60 + sec
                    self.timer.start(1000)
                else:
                    raise TypeError

            except TypeError:
                self.error_label.setText('Enter a value 1-24 for hour or 1-59 for minutes/seconds')
                self.timer_label.setText('')
                self.done_label.setText('')
                self.timer.stop()

            except ValueError:
                self.error_label.setText('Enter whole numbers only')
                self.timer_label.setText('')
                self.done_label.setText('')
                self.timer.stop()

    def pauseTimer(self) -> None:
        '''
        This method will pause the timer at its current time.
        '''
        if self.started:
            self.paused = not self.paused
            if self.paused:
                self.timer.stop()
            else:
                self.timeConversion(self.hours_left, self.minutes_left, self.seconds_left)
                self.timer.start(1000)

    def update_timer(self) -> None:
        '''
        This method will help update the timer continuously.

        '''
        if self.time_in_sec > -1:
            self.seconds_left = self.time_in_sec % 60
            self.minutes_left = (self.time_in_sec) // 60 % 60
            self.hours_left = self.time_in_sec // 3600
            self.time_in_sec -= 1
            self.timer_label.setText(f'{self.hours_left:02}:{self.minutes_left:02}:{self.seconds_left:02}')
        else:
            self.timer.stop()
            self.timer_label.setText('Time\'s up!')

    def resetTimer(self) -> None:
        '''
        This method will reset the timer to its default vaules.
        '''
        self.paused = False
        self.started = False
        self.timer_label.setText('')
        self.done_label.setText('')
        self.error_label.setText('')
        self.hourInp_2.setText('00')
        self.minInp_2.setText('00')
        self.secInp_2.setText('00')
        self.timer.stop()
        self.time_in_sec = 0
