from Project2Controller import *

def main():
    '''
    This function will help set up the PyQt5 GUI.
    '''
    application = QApplication([])
    window = Controller()
    window.setFixedSize(391,591)
    window.setWindowTitle('Project 2')
    window.show()
    application.exec_()

if __name__ == '__main__':
    main()


#Original Idea: https://www.youtube.com/watch?v=CcnsV4qlBGQ
