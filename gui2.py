from PyQt5 import QtCore, QtWidgets, QtGui
#from PyQt5.Qt import *
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)  # 524, 600
################################################
        self.flags = [0, 0, 0, 0, 0]
        self.words = ['balse',
                      'abcde',
                      'flagh']
        self.game_word=self.random_word()
        self.flag_game=False
####################################################
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")

        self.word = QtWidgets.QLabel(self.centralwidget)
        self.word.setObjectName("word")

        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setObjectName("tableWidget")
        self.table.setColumnCount(5)
        self.table.setRowCount(6)
 ############################################################
        # настроить ячейки
        style='''QTableWidget::item{background-color: white;
        border-style: solid; border-width: 2px;
        border-radius: 9px; border-color:orange}
        QTableWidget::item:selected{background-color: bisque;
        color: black}'''
        self.table.setStyleSheet(style)

        #первоначально запрещаем редактировать все строки, кроме 1
        for i in range(1, self.table.rowCount()):
            for j in range(0, self.table.columnCount()):
                item=QtWidgets.QTableWidgetItem()
                item.setFlags(item.flags() & QtCore.Qt.ItemIsEditable)
                self.table.setItem(i,j,item)
############################################################################
        self.promt = QtWidgets.QLabel(self.centralwidget)
        self.promt.setObjectName("promt")

        self.b_inp = QtWidgets.QPushButton(self.centralwidget)
        self.b_inp.setObjectName("pushButton")
        self.b_inp.clicked.connect(self.b_click)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout.addWidget(self.word)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.table)
        self.verticalLayout_2.addWidget(self.promt)
        self.verticalLayout_2.addWidget(self.b_inp)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Игра 5БУКВ"))
        self.label.setText(_translate("MainWindow", "Загаданое слово:"))
        #self.word.setText(_translate("MainWindow", "5БУКВ"))
        self.word.setText(_translate("MainWindow", self.random_word()))
        self.promt.setText(_translate("MaimWindow", "подсказка:"))
        self.b_inp.setText(_translate("MainWindow", "Ввод"))
#######CLASS WIDGET#########################################
    def random_word(self): #####################
        return self.words[1]

    def b_click(self):
        r=self.get_tab()
        if r!=5:
            self.srav(r)
            self.chek_flag()
            self.style_row(r)
        else:
            b=0 ##############################
        tab.clear()

    def get_tab(self):  # получить таблицу и строку таблицы для работы
        r_tab = -1
        f_r = True
        for i in range(0, self.table.rowCount()):
            temp = []
            for j in range(0, self.table.columnCount()):
                try:
                    temp.append(self.table.item(i, j).text())
                except:
                    temp.append('')
                    f_r = False
            tab.append(temp)
        if f_r:
            r_tab = r_tab + 1
        #print(r_tab)
        return r_tab

    def srav(self, row_tab):
        flag_w=False
        my_word = ''.join(tab[row_tab])
        if my_word == self.game_word:
            flag_w = True
        #if flag_w:
        #print(my_word, flag_w)
        self.flag_game=flag_w

    def chek_flag(self):
        if self.flag_game:
            self.promt.setText("подсказка: Вы выйграли!")
        else:
            self.promt.setText("подсказка: Слово введено не верно.") ############
            #print("Не верно")

    def style_row(self, r):
        gw=list(self.game_word)
        for i in range(0, self.table.columnCount()):
            #print("i=",i)
            wid=QtWidgets.QWidget
            if tab[r][i]==gw[i]: # прав. место, прав. буква
                ##########################################################
                style = '''QTableWidget::item{background-color: white;
                        border-style: solid; border-width: 2px;
                        border-radius: 9px; border-color:orange}
                        QTableWidget::item:selected{background-color: bisque;
                        color: black}'''
                self.table.setStyleSheet(style)
                #wid.setStyleSheet('''''')
                #self.table.item(r,i).setBackground(QtGui.QColor('yellow'))
                print("я здесь1")
            else:
                f2=False
                for j in range(0,self.table.columnCount()):
                    if tab[r][i]==gw[j]:
                        f2=True
                if f2: # не прав. место, прав. буква
                    self.table.item(r, i).setBackground(QtGui.QColor('silver'))
                    print("я здесь2")
                else:# не правильная буква
                    self.table.item(r, i).setBackground(QtGui.QColor('blue'))
                    print("я здесь3")
class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self._widget=QtWidgets.QWidget()
        self._widget.setObjectName("_widget")
        self.setStyleSheet('''
        #_widjet {background-color: blue;}
        #_lable {color: k;}''')
        self._label=QtWidgets.QLabel(alignment=QtCore.Qt.AlignCenter)
        self._label.setObjectName("_lable")
        @property
        def label(self):
            return self._label

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):





QSS='''
QTableWidget {
    qproperty-showGrid: "false";
    padding-left: 50px;
    padding-right: 50px;
    border: 0px solid;        
    gridline-color: #000000;}
QTableWidget::item {
    border-style: solid; 
    border-width: 2px;
    border-radius: 9px; border-color:orange}
QTableWidget::item:selected {
    background: palette(highlight);}
QHeaderView::section:vertical { 
    border: 0px;
    border-top: 2px solid #9370DB}
QHeaderView::section:horizontal { 
    border: 0px;
    border-right: 2px solid #9370DB}'''

if __name__ == "__main__":
    tab = []
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(QSS)

    #Window1=MainWindow()
    #Window1.show

    mainwin = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainwin)
    mainwin.show()

    sys.exit(app.exec_())
