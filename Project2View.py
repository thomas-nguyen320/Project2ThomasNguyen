# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timerView.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(386, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_widget.setGeometry(QtCore.QRect(0, 0, 391, 591))
        self.tab_widget.setObjectName("tab_widget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.alarmFrame = QtWidgets.QFrame(self.tab_2)
        self.alarmFrame.setGeometry(QtCore.QRect(30, 80, 351, 71))
        self.alarmFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.alarmFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.alarmFrame.setObjectName("alarmFrame")
        self.alarmHourInp = QtWidgets.QLineEdit(self.alarmFrame)
        self.alarmHourInp.setGeometry(QtCore.QRect(70, 0, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.alarmHourInp.setFont(font)
        self.alarmHourInp.setAlignment(QtCore.Qt.AlignCenter)
        self.alarmHourInp.setObjectName("alarmHourInp")
        self.alarmMinInp = QtWidgets.QLineEdit(self.alarmFrame)
        self.alarmMinInp.setGeometry(QtCore.QRect(170, 0, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.alarmMinInp.setFont(font)
        self.alarmMinInp.setAlignment(QtCore.Qt.AlignCenter)
        self.alarmMinInp.setObjectName("alarmMinInp")
        self.colon_label = QtWidgets.QLabel(self.alarmFrame)
        self.colon_label.setGeometry(QtCore.QRect(150, 0, 16, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.colon_label.setFont(font)
        self.colon_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.colon_label.setObjectName("colon_label")
        self.box_time_of_day = QtWidgets.QComboBox(self.alarmFrame)
        self.box_time_of_day.setGeometry(QtCore.QRect(260, 30, 61, 41))
        self.box_time_of_day.setObjectName("box_time_of_day")
        self.box_time_of_day.addItem("")
        self.box_time_of_day.addItem("")
        self.alarmHourLabel = QtWidgets.QLabel(self.tab_2)
        self.alarmHourLabel.setGeometry(QtCore.QRect(120, 60, 47, 13))
        self.alarmHourLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.alarmHourLabel.setObjectName("alarmHourLabel")
        self.alarmMinLabel = QtWidgets.QLabel(self.tab_2)
        self.alarmMinLabel.setGeometry(QtCore.QRect(220, 60, 47, 13))
        self.alarmMinLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.alarmMinLabel.setObjectName("alarmMinLabel")
        self.alarmSet_frame = QtWidgets.QFrame(self.tab_2)
        self.alarmSet_frame.setGeometry(QtCore.QRect(40, 200, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.alarmSet_frame.setFont(font)
        self.alarmSet_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.alarmSet_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.alarmSet_frame.setObjectName("alarmSet_frame")
        self.alarmSet_label = QtWidgets.QLabel(self.alarmSet_frame)
        self.alarmSet_label.setGeometry(QtCore.QRect(0, 0, 301, 71))
        self.alarmSet_label.setAlignment(QtCore.Qt.AlignCenter)
        self.alarmSet_label.setWordWrap(True)
        self.alarmSet_label.setObjectName("alarmSet_label")
        self.alarmSetBtn = QtWidgets.QPushButton(self.tab_2)
        self.alarmSetBtn.setGeometry(QtCore.QRect(40, 310, 101, 91))
        self.alarmSetBtn.setObjectName("alarmSetBtn")
        self.cancelAlarmBtn = QtWidgets.QPushButton(self.tab_2)
        self.cancelAlarmBtn.setGeometry(QtCore.QRect(230, 310, 101, 91))
        self.cancelAlarmBtn.setObjectName("cancelAlarmBtn")
        self.tab_widget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.startBtn = QtWidgets.QPushButton(self.tab)
        self.startBtn.setGeometry(QtCore.QRect(20, 240, 151, 101))
        self.startBtn.setObjectName("startBtn")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(20, 60, 341, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.hourInp_2 = QtWidgets.QLineEdit(self.frame)
        self.hourInp_2.setGeometry(QtCore.QRect(30, 0, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.hourInp_2.setFont(font)
        self.hourInp_2.setAlignment(QtCore.Qt.AlignCenter)
        self.hourInp_2.setObjectName("hourInp_2")
        self.minInp_2 = QtWidgets.QLineEdit(self.frame)
        self.minInp_2.setGeometry(QtCore.QRect(130, 0, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.minInp_2.setFont(font)
        self.minInp_2.setAlignment(QtCore.Qt.AlignCenter)
        self.minInp_2.setObjectName("minInp_2")
        self.secInp_2 = QtWidgets.QLineEdit(self.frame)
        self.secInp_2.setGeometry(QtCore.QRect(230, 0, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.secInp_2.setFont(font)
        self.secInp_2.setAlignment(QtCore.Qt.AlignCenter)
        self.secInp_2.setObjectName("secInp_2")
        self.colon_label_3 = QtWidgets.QLabel(self.frame)
        self.colon_label_3.setGeometry(QtCore.QRect(100, 0, 20, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.colon_label_3.setFont(font)
        self.colon_label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.colon_label_3.setObjectName("colon_label_3")
        self.colon_label_4 = QtWidgets.QLabel(self.frame)
        self.colon_label_4.setGeometry(QtCore.QRect(200, 0, 20, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.colon_label_4.setFont(font)
        self.colon_label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.colon_label_4.setObjectName("colon_label_4")
        self.resetBtn = QtWidgets.QPushButton(self.tab)
        self.resetBtn.setGeometry(QtCore.QRect(110, 360, 151, 101))
        self.resetBtn.setObjectName("resetBtn")
        self.timer_label = QtWidgets.QLabel(self.tab)
        self.timer_label.setGeometry(QtCore.QRect(20, 110, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.timer_label.setFont(font)
        self.timer_label.setText("")
        self.timer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.timer_label.setObjectName("timer_label")
        self.done_label = QtWidgets.QLabel(self.tab)
        self.done_label.setGeometry(QtCore.QRect(20, 180, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.done_label.setFont(font)
        self.done_label.setText("")
        self.done_label.setAlignment(QtCore.Qt.AlignCenter)
        self.done_label.setObjectName("done_label")
        self.pauseBtn = QtWidgets.QPushButton(self.tab)
        self.pauseBtn.setGeometry(QtCore.QRect(210, 240, 151, 101))
        self.pauseBtn.setObjectName("pauseBtn")
        self.hour_label = QtWidgets.QLabel(self.tab)
        self.hour_label.setGeometry(QtCore.QRect(60, 40, 47, 13))
        self.hour_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hour_label.setObjectName("hour_label")
        self.minute_label = QtWidgets.QLabel(self.tab)
        self.minute_label.setGeometry(QtCore.QRect(160, 40, 47, 13))
        self.minute_label.setAlignment(QtCore.Qt.AlignCenter)
        self.minute_label.setObjectName("minute_label")
        self.second_label = QtWidgets.QLabel(self.tab)
        self.second_label.setGeometry(QtCore.QRect(250, 39, 61, 21))
        self.second_label.setAlignment(QtCore.Qt.AlignCenter)
        self.second_label.setObjectName("second_label")
        self.error_label = QtWidgets.QLabel(self.tab)
        self.error_label.setGeometry(QtCore.QRect(30, 110, 321, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.error_label.setFont(font)
        self.error_label.setText("")
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label.setWordWrap(True)
        self.error_label.setObjectName("error_label")
        self.tab_widget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.stopwatch_Frame = QtWidgets.QFrame(self.tab_3)
        self.stopwatch_Frame.setGeometry(QtCore.QRect(10, 110, 361, 80))
        self.stopwatch_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stopwatch_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stopwatch_Frame.setObjectName("stopwatch_Frame")
        self.stopWatch_label = QtWidgets.QLabel(self.stopwatch_Frame)
        self.stopWatch_label.setGeometry(QtCore.QRect(0, 0, 361, 81))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.stopWatch_label.setFont(font)
        self.stopWatch_label.setAlignment(QtCore.Qt.AlignCenter)
        self.stopWatch_label.setObjectName("stopWatch_label")
        self.lap_frame = QtWidgets.QFrame(self.tab_3)
        self.lap_frame.setGeometry(QtCore.QRect(10, 190, 361, 231))
        self.lap_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lap_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lap_frame.setObjectName("lap_frame")
        self.lap_text = QtWidgets.QTextBrowser(self.lap_frame)
        self.lap_text.setGeometry(QtCore.QRect(0, 40, 361, 191))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lap_text.setFont(font)
        self.lap_text.setObjectName("lap_text")
        self.display_laptext = QtWidgets.QLabel(self.lap_frame)
        self.display_laptext.setGeometry(QtCore.QRect(0, 0, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.display_laptext.setFont(font)
        self.display_laptext.setAutoFillBackground(False)
        self.display_laptext.setText("")
        self.display_laptext.setObjectName("display_laptext")
        self.lapBtn = QtWidgets.QPushButton(self.tab_3)
        self.lapBtn.setGeometry(QtCore.QRect(10, 430, 131, 41))
        self.lapBtn.setObjectName("lapBtn")
        self.stopwatchStartStopBtn = QtWidgets.QPushButton(self.tab_3)
        self.stopwatchStartStopBtn.setGeometry(QtCore.QRect(240, 430, 131, 41))
        self.stopwatchStartStopBtn.setObjectName("stopwatchStartStopBtn")
        self.stopwatchReset_btn = QtWidgets.QPushButton(self.tab_3)
        self.stopwatchReset_btn.setGeometry(QtCore.QRect(130, 480, 131, 41))
        self.stopwatchReset_btn.setObjectName("stopwatchReset_btn")
        self.tab_widget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.alarmHourInp.setText(_translate("MainWindow", "00"))
        self.alarmMinInp.setText(_translate("MainWindow", "00"))
        self.colon_label.setText(_translate("MainWindow", ":"))
        self.box_time_of_day.setItemText(0, _translate("MainWindow", "AM"))
        self.box_time_of_day.setItemText(1, _translate("MainWindow", "PM"))
        self.alarmHourLabel.setText(_translate("MainWindow", "Hour"))
        self.alarmMinLabel.setText(_translate("MainWindow", "Minute"))
        self.alarmSet_label.setText(_translate("MainWindow", "Alarm not set"))
        self.alarmSetBtn.setText(_translate("MainWindow", "Set Alarm"))
        self.cancelAlarmBtn.setText(_translate("MainWindow", "Cancel Alarm"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_2), _translate("MainWindow", "Alarm"))
        self.startBtn.setText(_translate("MainWindow", "Start"))
        self.hourInp_2.setText(_translate("MainWindow", "00"))
        self.minInp_2.setText(_translate("MainWindow", "00"))
        self.secInp_2.setText(_translate("MainWindow", "00"))
        self.colon_label_3.setText(_translate("MainWindow", ":"))
        self.colon_label_4.setText(_translate("MainWindow", ":"))
        self.resetBtn.setText(_translate("MainWindow", "Reset"))
        self.pauseBtn.setText(_translate("MainWindow", "Pause/Resume"))
        self.hour_label.setText(_translate("MainWindow", "Hour"))
        self.minute_label.setText(_translate("MainWindow", "Minute"))
        self.second_label.setText(_translate("MainWindow", "Second"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab), _translate("MainWindow", "Timer"))
        self.stopWatch_label.setText(_translate("MainWindow", "00:00:00.00"))
        self.lap_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.lapBtn.setText(_translate("MainWindow", "Lap"))
        self.stopwatchStartStopBtn.setText(_translate("MainWindow", "Start/Stop"))
        self.stopwatchReset_btn.setText(_translate("MainWindow", "Reset"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_3), _translate("MainWindow", "Stopwatch"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
