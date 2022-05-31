import sys

from PyQt5 import QtWidgets as qtw

from controller.main_view_controller import MainViewController

def main():
    app = qtw.QApplication(sys.argv)
    main_controller = MainViewController()
    main_controller.show() 
    app.exec_()

if __name__ == "__main__":
    main()

