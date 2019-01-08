from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QGridLayout, QWidget, QMessageBox
import sys

class Main(QWidget):
    def __init__(self):
        super().__init__()
        x, y, w, h = 400, 250, 400, 250
        self.setGeometry(500, 500, 500, 500)

        self.Grid()
        self.events()
        self.count1, self.count2, self.count3, self.count4, self.count5, self.count6, self.count7, self.count8, self.count9 = 0, 0, 0, 0, 0, 0, 0, 0, 0


    def Grid(self):

        grid = QGridLayout()
        self.setLayout(grid)

        self.btn1 = QPushButton()
        self.btn2 = QPushButton()
        self.btn3 = QPushButton()
        self.btn4 = QPushButton()
        self.btn5 = QPushButton()
        self.btn6 = QPushButton()
        self.btn7 = QPushButton()
        self.btn8 = QPushButton()
        self.btn9 = QPushButton()

        self.btnCheck = QPushButton('Проверить')
        self.btnReset= QPushButton('Сбросить')


        self.list = [self.btn1, self.btn2, self.btn3,
                self.btn4, self.btn5, self.btn6,
                self.btn7, self.btn8, self.btn9]

        self.RobotList = []

        pos = [(i, j) for i in range(3) for j in range(3)]

        count = -1

        for position in pos:

            count += 1
            print(count)


            grid.addWidget(self.list[count], *position)

        grid.addWidget(self.btnCheck, 4, 0)
        grid.addWidget(self.btnReset, 4, 1)



    def events(self):
        count = -1
        listevents = [self.change1, self.change2, self.change3,
                      self.change4, self.change5, self.change6,
                      self.change7, self.change8, self.change9]

        self.btnCheck.clicked.connect(self.check)
        self.btnReset.clicked.connect(self.reset)


        for i in self.list:
            count += 1
            i.clicked.connect(listevents[count])



    def change1(self):

        if self.count1 == 1:
            self.btn1.setText('x')
            self.count1 = 0
            return

        elif self.count1 == 0:
            self.btn1.setText('0')
            self.count1 += 1
            return




    def change2(self):
        if self.count2 == 1:
            self.btn2.setText('x')
            self.count2 = 0
            return

        elif self.count2 == 0:
            self.btn2.setText('0')
            self.count2 += 1
            return

    def change3(self):
        if self.count3 == 1:
            self.btn3.setText('x')
            self.count3 = 0
            return

        elif self.count3 == 0:
            self.btn3.setText('0')
            self.count3 += 1
            return

    def change4(self):
        if self.count4 == 1:
            self.btn4.setText('x')
            self.count4 = 0
            return

        elif self.count4 == 0:
            self.btn4.setText('0')
            self.count4 += 1
            return

    def change5(self):
        if self.count5 == 1:
            self.btn5.setText('x')
            self.count5 = 0
            return

        elif self.count5 == 0:
            self.btn5.setText('0')
            self.count5 += 1
            return

    def change6(self):
        if self.count6 == 1:
            self.btn6.setText('x')
            self.count6 = 0
            return

        elif self.count6 == 0:
            self.btn6.setText('0')
            self.count6 += 1
            return

    def change7(self):
        if self.count7 == 1:
            self.btn7.setText('x')
            self.count7 = 0
            return

        elif self.count7 == 0:
            self.btn7.setText('0')
            self.count7 += 1
            return

    def change8(self):
        if self.count8 == 1:
            self.btn8.setText('x')
            self.count8 = 0
            return

        elif self.count8 == 0:
            self.btn8.setText('0')
            self.count8 += 1
            return

    def change9(self):
        if self.count9 == 1:
            self.btn9.setText('x')
            self.count9 = 0
            return

        elif self.count9 == 0:
            self.btn9.setText('0')
            self.count9 += 1
            return

    def reset(self):
        count = 0
        for i in self.list:
            count += 1
            i.setText('')



    def check(self):

        scoar_x = 0
        scoar_y = 0
        if self.btn1.text() == 'x' and self.btn2.text() == 'x' and self.btn3.text() == 'x' :
            scoar_x = 1
        elif self.btn4.text() == 'x' and self.btn5.text() == 'x' and self.btn6.text() == 'x':
            scoar_x = 1
        elif self.btn7.text() == 'x' and self.btn8.text() == 'x' and self.btn9.text() == 'x' :


            scoar_x = 1
        elif self.btn1.text() == 'x' and self.btn4.text() == 'x' and self.btn4.text() == 'x':
            scoar_x = 1
        elif self.btn2.text() == 'x' and self.btn5.text() == 'x' and self.btn8.text() == 'x' :
            scoar_x = 1
        elif self.btn3.text() == 'x' and self.btn6.text() == 'x' and self.btn9.text() == 'x':


            scoar_x = 1
        elif self.btn1.text() == 'x' and self.btn5.text() == 'x' and self.btn9.text() == 'x' :
            scoar_x = 1
        elif self.btn7.text() == 'x' and self.btn5.text() == 'x' and self.btn3.text() == 'x' :
            scoar_x = 1




        if self.btn1.text() == '0' and self.btn2.text() == '0' and self.btn3.text() == '0' :
            scoar_y = 1
        elif self.btn4.text() == '0' and self.btn5.text() == '0' and self.btn6.text() == '0':
            scoar_y = 1
        elif self.btn7.text() == '0' and self.btn8.text() == '0' and self.btn9.text() == '0' :
            scoar_y = 1


        elif self.btn1.text() == '0' and self.btn4.text() == '0' and self.btn4.text() == '0':
            scoar_y = 1
        elif self.btn2.text() == '0' and self.btn5.text() == '0' and self.btn8.text() == '0' :
            scoar_y = 1
        elif self.btn3.text() == '0' and self.btn6.text() == '0' and self.btn9.text() == '0':


            scoar_y = 1
        elif self.btn1.text() == '0' and self.btn5.text() == '0' and self.btn9.text() == '0' :
            scoar_y = 1
        elif self.btn7.text() == '0' and self.btn5.text() == '0' and self.btn3.text() == '0' :
            scoar_y = 1

        if scoar_x == 1 and scoar_y == 1:
            finish = QMessageBox.question(self, 'tic tac toes', "Ничья. Продолжить?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if finish == QMessageBox.No:
                exit()

        elif scoar_x == 1:
            finish = QMessageBox.question(self, 'tic tac toes', "Выиграл x. Продолжить?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if finish == QMessageBox.No:
                exit()

        elif scoar_y == 1:
            finish = QMessageBox.question(self, 'tic tac toes', "Выиграл 0. Продолжить?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if finish == QMessageBox.No:
                exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen = Main()
    screen.show()
    app.exec()
