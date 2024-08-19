#import item
import selection
from PyQt5 import QtCore, QtWidgets, QtGui
import sys


class MainWindow(object):
    def setupUi(self, mainwin):
        mainwin.setObjectName("MainWindow")
        mainwin.resize(700, 600)  # 524, 600

        #self.count_tab_baton_vvod = 0
        self.flags = [0, 0, 0, 0, 0]
        self.words = ['balse',
                      'abcde',
                      'flagh']
        self.game_word=self.random_word()
        self.flag_game=False

        self.centralwidget = QtWidgets.QWidget(mainwin)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")

        self.word = QtWidgets.QLabel(self.centralwidget)
        self.word.setObjectName("word")

        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setObjectName("tableWidget")
        self.table.setColumnCount(5)
        self.table.setRowCount(6)

        # self.table.setColumnWidth(0,15) # ширина 1 колонки
        # поместить в ячейки надпись и виджет
        # a=QtWidgets.QTableWidgetItem.ItemType
        #########################################
        #a=QtWidgets.QTableWidgetItem('a')
        #self.table.setItem(0,0,a)
        '''a=QtWidgets.QTableWidgetItem('a')
        b=QtWidgets.QPushButton()
        b.resize(20,20)
        b.setText('b')
        self.table.setItem(0,0,a)
        self.table.setCellWidget(0,1,b) '''

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


        self.promt = QtWidgets.QLabel(self.centralwidget)
        self.promt.setObjectName("promt")

        self.b_inp = QtWidgets.QPushButton(self.centralwidget)
        self.b_inp.setObjectName("pushButton")
        self.b_inp.clicked.connect(self.get_tab)
        # self.b_inp.clicked.connect(self.get_tab)

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

        mainwin.setCentralWidget(self.centralwidget)
        self.retranslateUi(mainwin)
        QtCore.QMetaObject.connectSlotsByName(mainwin)



    def retranslateUi(self, mainwin):
        _translate = QtCore.QCoreApplication.translate
        mainwin.setWindowTitle(_translate("MainWindow", "Игра 5БУКВ"))
        self.label.setText(_translate("MainWindow", "Загаданое слово:"))
        #self.word.setText(_translate("MainWindow", "5БУКВ"))
        self.word.setText(_translate("MainWindow", self.random_word()))
        self.promt.setText(_translate("MaimWindow", "подсказка:"))
        self.b_inp.setText(_translate("MainWindow", "Ввод"))

    def get_tab(self):  # получить таблицу
        r_tab=-1
        f_r=True
        for i in range(0, self.table.rowCount()):
            temp = []
            for j in range(0, self.table.columnCount()):
                try:
                    temp.append(self.table.item(i, j).text())
                except:
                    temp.append('')
                    f_r=False
            tab.append(temp)
        if f_r:
            r_tab=r_tab+1
        #print(tab)
        #print(r_tab)
        #if self.srav(r_tab):

        #else:

        #self.find_word()
        tab.clear()

    def random_word(self): #####################
        return self.words[1]

    def srav(self, row_tab):
        flag=False
        my_word=''.join(tab[row_tab])
        #if kol_sym_in_word==4 and my_word==game_word:
        if my_word == self.game_word:
            flag=True
        return flag

    def find_word(self):
        for i in range(0, len(self.flags)):
            my_word=''.join(tab[i])
            if self.flags[i]==0: # флаг слова =0
                # проверяем состоит ли оно из 5 букв
                if len(my_word)==5:
                    self.flags[i]=1
                    self.find_word()
                    #self.promt.setText("подсказка: ")
                else:
                    self.promt.setText("подсказка: "
                                       "Введите слово из 5 букв.")
                print(self.flags)
                break
            elif self.flags[i]==1: # флаг слова =1
                # проверяем есть ли слово из списка
                f=False
                for j in range(0, len(self.words)):
                    print("my_word: ", my_word)
                    print("words[", j, "]: ", self.words[j])
                    if my_word==self.words[j]:
                        f=True
                if f:
                    self.flags[i]=2
                    self.find_word()
                    #self.promt.setText("ggg")
                else:
                    self.promt.setText("подсказка: Введите "
                                       "существительное "
                                       "в единственом числе.")
                print(self.flags)
                break
            elif self.flags[i]==2: # флаг слова =1
                # проверяем совпадает ли слово
                #print("я тут")
                if my_word==self.game_word:
                    self.flags[i]=3
                    self.find_word()
                    #self.promt.setText("Вы выйграли!")
                else:
                    print("я тут")
                    self.promt.setText("подсказка: Слово"
                                       "не верное")
                print(self.flags)
                continue
            else: # флаг слова =3
                self.promt.setText("Вы выйграли!")
                self.flag_game=True
                print(self.flags)
                break # завершаем игру, т.к. слово верное
        #if self.flag_game:
        #    self.promt.setText("Вы выйграли!")
        #else:
        #    self.promt.setText("Вы проиграли.")


if __name__ == "__main__":
    tab = []
    app = QtWidgets.QApplication(sys.argv)
    mainwin = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi(mainwin)
    mainwin.show()
    sys.exit(app.exec_())
