from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from Project2View import *
from datetime import datetime

class Alarm(QMainWindow,Ui_MainWindow):
    def __init__(self, *args, **kwargs) -> None:
        '''
        Constructor to create initial state of a Alarm object.
        '''
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        #The bottom two lines of codes will help me make a timer that updates the current time while letting us use the other functions.
        self.alarm_timer = QTimer()
        self.alarm_timer.timeout.connect(self.update_current_time)

    def set_alarm(self) -> None:
        '''
        This method will set up the alarm to the time the user inputs then start the alarm.
        '''
        try:
            self.userAlarmHour = int(self.alarmHourInp.text())
            self.userAlarmMin = int(self.alarmMinInp.text())
            self.alarmTimeOfDay = self.box_time_of_day.currentText()
            if (self.userAlarmHour > 0 and self.userAlarmHour <= 12) and (self.userAlarmMin >= 0 and self.userAlarmMin <= 59):
                self.alarmHourInp.setText('00')
                self.alarmMinInp.setText('00')
                if self.alarmTimeOfDay == 'AM':
                    self.alarmSet_label.setText(f'Alarm set for {self.userAlarmHour}:{self.userAlarmMin:02} A.M. ')
                elif self.alarmTimeOfDay == 'PM':
                    self.alarmSet_label.setText(f'Alarm set for {self.userAlarmHour}:{self.userAlarmMin:02} P.M. ')
                    self.userAlarmHour += 12
                self.alarm_timer.start(1000)
            else:
                raise TypeError
        except TypeError:
            self.alarmSet_label.setText('Enter a valid time in a 12-hour format')
        except ValueError:
            self.alarmSet_label.setText('Enter whole numbers only')

    def cancel_alarm(self) -> None:
        '''
        This method will cancel the alarm and make the alarm not go off.
        '''
        self.alarm_timer.stop()
        self.alarmSet_label.setText('Alarm not set')

    def update_current_time(self) -> None:
        '''
        This method will help update the current time continously and check if the user's input match the time.
        '''
        self.now = datetime.now()
        self.current_alarm_hour = int(self.now.strftime("%H"))
        self.current_alarm_min = int(self.now.strftime("%M"))
        if self.userAlarmHour == self.current_alarm_hour:
            if self.userAlarmMin == self.current_alarm_min:
                self.alarm_timer.stop()
                self.alarmSet_label.setText('Times Up!')
