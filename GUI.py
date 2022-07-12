## -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QApplication, QDialog, QTabWidget
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon
import natural_nums
import integer_nums
import rational_nums
import polynomial

class Natural_nums(QWidget):
    def __init__(self):
        super().__init__()

        self.N = QLabel('Действия с натуральными числами')

        self.N1 = QLabel('Сравнение натуральных чисел: 2 - если первое больше второго, 0, если равно, 1 иначе.')
        self.N1.setWordWrap(True)

        self.N2 = QLabel('Проверка на ноль: если число не равно нулю, то «да» иначе «нет»')
        self.N2.setWordWrap(True)
        self.N2.hide()

        self.N3 = QLabel('Добавление 1 к натуральному числу')
        self.N3.setWordWrap(True)
        self.N2.hide()

        self.N4 = QLabel('Сложение натуральных чисел')
        self.N4.setWordWrap(True)
        self.N2.hide()

        self.N5 = QLabel('Вычитание из первого большего натурального числа второго меньшего или равного')
        self.N5.setWordWrap(True)
        self.N2.hide()

        self.N6 = QLabel('Умножение натурального числа на цифру')
        self.N6.setWordWrap(True)
        self.N2.hide()

        self.N7 = QLabel('Умножение натурального числа на 10^k')
        self.N7.setWordWrap(True)
        self.N2.hide()

        self.N8 = QLabel('Умножение натуральных чисел')
        self.N8.setWordWrap(True)
        self.N2.hide()

        self.N9 = QLabel('Вычитание из натурального другого натурального, умноженного на цифру для случая с неотрицательным результатом')
        self.N9.setWordWrap(True)
        self.N2.hide()

        self.N10 = QLabel('Вычисление первой цифры деления большего натурального на меньшее, домноженное на 10^k,где k - номер позиции этой цифры (номер считается с нуля)')
        self.N10.setWordWrap(True)
        self.N2.hide()

        self.N11 = QLabel('Частное от деления большего натурального числа на меньшее или равное натуральное с остатком(делитель отличен от нуля)')
        self.N11.setWordWrap(True)
        self.N2.hide()

        self.N12 = QLabel('Остаток от деления большего натурального числа на меньшее или равное натуральное с остатком(делитель отличен от нуля)')
        self.N12.setWordWrap(True)
        self.N2.hide()

        self.N13 = QLabel('НОД натуральных чисел')
        self.N13.setWordWrap(True)
        self.N2.hide()

        self.N14 = QLabel('НОК натуральных чисел')
        self.N14.setWordWrap(True)
        self.N2.hide()
        
        self.strInput1N1 = QLineEdit('', self)
        self.strInput1N1.setPlaceholderText('Введите первое число')
        self.strInput2N1 = QLineEdit('', self)
        self.strInput2N1.setPlaceholderText('Введите второе число')

        self.strInputN2 = QLineEdit('', self)
        self.strInputN2.setPlaceholderText('Введите число')
        self.strInputN2.hide()

        self.strInput2N6 = QLineEdit('', self)
        self.strInput2N6.setPlaceholderText('Введите цифру')
        self.strInput2N6.setMaxLength(1)
        self.strInput2N6.setFixedSize(115, 25)
        self.strInput2N6.hide()

        self.strInput2N7 = QLineEdit('', self)
        self.strInput2N7.setPlaceholderText('Введите степень 10')
        self.strInput2N7.hide()
        

        self.strOutput1 = QLineEdit('', self)
        self.strOutput1.setPlaceholderText('Результат')
        self.strOutput1.setReadOnly(True)

        self.strOutput2 = QLineEdit('', self)
        self.strOutput2.setPlaceholderText('Результат')
        self.strOutput2.setReadOnly(True)
        self.strOutput2.hide()

        self.strOutput3 = QLineEdit('', self)
        self.strOutput3.setPlaceholderText('Результат')
        self.strOutput3.setReadOnly(True)
        self.strOutput3.hide()

        self.strOutput4 = QLineEdit('', self)
        self.strOutput4.setPlaceholderText('Результат')
        self.strOutput4.setReadOnly(True)
        self.strOutput4.hide()

        self.strOutput5 = QLineEdit('', self)
        self.strOutput5.setPlaceholderText('Результат')
        self.strOutput5.setReadOnly(True)
        self.strOutput5.hide()

        self.strOutput6 = QLineEdit('', self)
        self.strOutput6.setPlaceholderText('Результат')
        self.strOutput6.setReadOnly(True)
        self.strOutput6.hide()

        self.strOutput7 = QLineEdit('', self)
        self.strOutput7.setPlaceholderText('Результат')
        self.strOutput7.setReadOnly(True)
        self.strOutput7.hide()

        self.strOutput8 = QLineEdit('', self)
        self.strOutput8.setPlaceholderText('Результат')
        self.strOutput8.setReadOnly(True)
        self.strOutput8.hide()

        self.strOutput9 = QLineEdit('', self)
        self.strOutput9.setPlaceholderText('Результат')
        self.strOutput9.setReadOnly(True)
        self.strOutput9.hide()

        self.strOutput10 = QLineEdit('', self)
        self.strOutput10.setPlaceholderText('Результат')
        self.strOutput10.setReadOnly(True)
        self.strOutput10.hide()

        self.strOutput11 = QLineEdit('', self)
        self.strOutput11.setPlaceholderText('Результат')
        self.strOutput11.setReadOnly(True)
        self.strOutput11.hide()

        self.strOutput12 = QLineEdit('', self)
        self.strOutput12.setPlaceholderText('Результат')
        self.strOutput12.setReadOnly(True)
        self.strOutput12.hide()

        self.strOutput13 = QLineEdit('', self)
        self.strOutput13.setPlaceholderText('Результат')
        self.strOutput13.setReadOnly(True)
        self.strOutput13.hide()

        self.strOutput14 = QLineEdit('', self)
        self.strOutput14.setPlaceholderText('Результат')
        self.strOutput14.setReadOnly(True)
        self.strOutput14.hide()

        self.but1 = QPushButton('Посчитать', self)
        self.but1.clicked.connect(self.butt1)

        self.but2 = QPushButton('Посчитать', self)
        self.but2.clicked.connect(self.butt2)
        self.but2.hide()

        self.but3 = QPushButton('Посчитать', self)
        self.but3.clicked.connect(self.butt3)
        self.but3.hide()

        self.but4 = QPushButton('Посчитать', self)
        self.but4.clicked.connect(self.butt4)
        self.but4.hide()

        self.but5 = QPushButton('Посчитать', self)
        self.but5.clicked.connect(self.butt5)
        self.but5.hide()

        self.but6 = QPushButton('Посчитать', self)
        self.but6.clicked.connect(self.butt6)
        self.but6.hide()

        self.but7 = QPushButton('Посчитать', self)
        self.but7.clicked.connect(self.butt7)
        self.but7.hide()

        self.but8 = QPushButton('Посчитать', self)
        self.but8.clicked.connect(self.butt8)
        self.but8.hide()

        self.but9 = QPushButton('Посчитать', self)
        self.but9.clicked.connect(self.butt9)
        self.but9.hide()

        self.but10 = QPushButton('Посчитать', self)
        self.but10.clicked.connect(self.butt10)
        self.but10.hide()

        self.but11 = QPushButton('Посчитать', self)
        self.but11.clicked.connect(self.butt11)
        self.but11.hide()

        self.but12 = QPushButton('Посчитать', self)
        self.but12.clicked.connect(self.butt12)
        self.but12.hide()

        self.but13 = QPushButton('Посчитать', self)
        self.but13.clicked.connect(self.butt13)
        self.but13.hide()

        self.but14 = QPushButton('Посчитать', self)
        self.but14.clicked.connect(self.butt14)
        self.but14.hide()

        self.selectN = QComboBox(self)
        self.selectN.setFixedSize(200, 25)
        
        self.selectN.addItem('Сравнение нат. чисел')
        self.selectN.addItem('Проверка на ноль')
        self.selectN.addItem('Добавление 1 к нат. числу')
        self.selectN.addItem('Сложение нат. чисел')
        self.selectN.addItem('Вычитание из 1-ого бол. мен. нат.')
        self.selectN.addItem('Умножение нат. числа на цифру')
        self.selectN.addItem('Умножение нат. числа на 10^k')
        self.selectN.addItem('Умножение нат. чисел')
        self.selectN.addItem('Вычитание из нат. др. нат., домн. на цифру')
        self.selectN.addItem('Первая цифра от дел. бол. на мен.')
        self.selectN.addItem('Частное от дел. бол. на мен.')
        self.selectN.addItem('Остаток от дел. бол. на мен.')
        self.selectN.addItem('НОД нат. чисел')
        self.selectN.addItem('НОК нат. чисел')

        self.selectN.currentTextChanged.connect(self.changedN)

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.N)
        self.hbox.addWidget(self.selectN)

        self.hbox1 = QHBoxLayout()
        self.hbox1.addWidget(self.N1)

        self.hbox2 = QHBoxLayout()
        self.hbox2.addWidget(self.strInput1N1)
        self.hbox2.addWidget(self.strInput2N1)

        self.hbox3 = QHBoxLayout()
        self.hbox3.addWidget(self.strOutput1)
        self.hbox3.addWidget(self.but1)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)

        self.setLayout(self.vbox)

    def butt1(self):
        try:
            num1 = natural_nums.STR_TO_NAT(self.strInput1N1.text())
            num2 = natural_nums.STR_TO_NAT(self.strInput2N1.text())
            self.strOutput1.setText(str(natural_nums.COM_NN_D(num1, num2)))
        except:
            self.strOutput1.setText('Введены недопустимые значения')

    def butt2(self):
        try:
            num = natural_nums.STR_TO_NAT(self.strInputN2.text())
            self.strOutput2.setText(str(natural_nums.NZER_N_B(num)))
        except:
            self.strOutput2.setText('Введены недопустимые значения')

    def butt3(self):
        try:
            num = natural_nums.STR_TO_NAT(self.strInputN2.text())
            self.strOutput3.setText(natural_nums.NAT_TO_NORMAL(natural_nums.ADD_1N_N(num)))
        except:
            self.strOutput3.setText('Введены недопустимые значения')

    def butt4(self):
        try:
            num1 = natural_nums.STR_TO_NAT(self.strInput1N1.text())
            num2 = natural_nums.STR_TO_NAT(self.strInput2N1.text())
            self.strOutput4.setText(natural_nums.NAT_TO_NORMAL(natural_nums.ADD_NN_N(num1, num2)))
        except:
            self.strOutput4.setText('Введены недопустимые значения')

    def butt5(self):
        try:
            num1 = natural_nums.STR_TO_NAT(self.strInput1N1.text())
            num2 = natural_nums.STR_TO_NAT(self.strInput2N1.text())
            self.strOutput5.setText(natural_nums.NAT_TO_NORMAL(natural_nums.SUB_NN_N(num1, num2)))
        except:
            self.strOutput5.setText('Введены недопустимые значения')

    def butt6(self):
        try:
            num = natural_nums.STR_TO_NAT(self.strInputN2.text())
            c = int(self.strInput2N6.text())
            self.strOutput6.setText(natural_nums.NAT_TO_NORMAL(natural_nums.MUL_ND_N(c, num)))
        except:
            self.strOutput6.setText('Введены недопустимые значения')

    def butt7(self):
        try:
            num = natural_nums.STR_TO_NAT(self.strInputN2.text())
            c = int(self.strInput2N7.text())
            self.strOutput7.setText(natural_nums.NAT_TO_NORMAL(natural_nums.MUL_Nk_N(num, c)))
        except:
            self.strOutput7.setText('Введены недопустимые значения')

    def butt8(self):
        try:
            num1 = natural_nums.STR_TO_NAT(self.strInput1N1.text())
            num2 = natural_nums.STR_TO_NAT(self.strInput2N1.text())
            self.strOutput8.setText(natural_nums.NAT_TO_NORMAL(natural_nums.MUL_NN_N(num1, num2)))
        except:
            self.strOutput8.setText('Введены недопустимые значения')

    def butt9(self):
        try:
            num1 = natural_nums.STR_TO_NAT(self.strInput1N1.text())
            num2 = natural_nums.STR_TO_NAT(self.strInput2N1.text())
            c = int(self.strInput2N6.text())
            self.strOutput9.setText(natural_nums.NAT_TO_NORMAL(natural_nums.SUB_NDN_N(num1, num2, c)))
        except:
            self.strOutput9.setText('Введены недопустимые значения')

    def butt10(self):
        try:
            num1 = natural_nums.STR_TO_NAT(self.strInput1N1.text())
            num2 = natural_nums.STR_TO_NAT(self.strInput2N1.text())
            self.strOutput10.setText(natural_nums.NAT_TO_NORMAL(natural_nums.DIV_NN_Dk(num1, num2)))
        except:
            self.strOutput10.setText('Введены недопустимые значения')

    def butt11(self):
        try:
            num1 = natural_nums.STR_TO_NAT(self.strInput1N1.text())
            num2 = natural_nums.STR_TO_NAT(self.strInput2N1.text())
            self.strOutput11.setText(natural_nums.NAT_TO_NORMAL(natural_nums.DIV_NN_N(num1, num2)))
        except:
            self.strOutput11.setText('Введены недопустимые значения')

    def butt12(self):
        try:
            num1 = natural_nums.STR_TO_NAT(self.strInput1N1.text())
            num2 = natural_nums.STR_TO_NAT(self.strInput2N1.text())
            self.strOutput12.setText(natural_nums.NAT_TO_NORMAL(natural_nums.MOD_NN_N(num1, num2)))
        except:
            self.strOutput12.setText('Введены недопустимые значения')

    def butt13(self):
        try:
            num1 = natural_nums.STR_TO_NAT(self.strInput1N1.text())
            num2 = natural_nums.STR_TO_NAT(self.strInput2N1.text())
            self.strOutput13.setText(natural_nums.NAT_TO_NORMAL(natural_nums.GCF_NN_N(num1, num2)))
        except:
            self.strOutput13.setText('Введены недопустимые значения')

    def butt14(self):
        try:
            num1 = natural_nums.STR_TO_NAT(self.strInput1N1.text())
            num2 = natural_nums.STR_TO_NAT(self.strInput2N1.text())
            self.strOutput14.setText(natural_nums.NAT_TO_NORMAL(natural_nums.LCM_NN_N(num1, num2)))
        except:
            self.strOutput14.setText('Введены недопустимые значения')

    def changedN(self):
        n = self.selectN.currentText()
        self.N1.hide()
        self.N2.hide()
        self.N3.hide()
        self.N4.hide()
        self.N5.hide()
        self.N6.hide()
        self.N7.hide()
        self.N8.hide()
        self.N9.hide()
        self.N10.hide()
        self.N11.hide()
        self.N12.hide()
        self.N13.hide()
        self.N14.hide()
        self.strInput1N1.hide()
        self.strInput2N1.hide()
        self.strInputN2.hide()
        self.strInput2N6.hide()
        self.strInput2N7.hide()
        self.strOutput1.hide()
        self.strOutput2.hide()
        self.strOutput3.hide()
        self.strOutput4.hide()
        self.strOutput5.hide()
        self.strOutput6.hide()
        self.strOutput7.hide()
        self.strOutput8.hide()
        self.strOutput9.hide()
        self.strOutput10.hide()
        self.strOutput11.hide()
        self.strOutput12.hide()
        self.strOutput13.hide()
        self.strOutput14.hide()
        self.but1.hide()
        self.but2.hide()
        self.but3.hide()
        self.but4.hide()
        self.but5.hide()
        self.but6.hide()
        self.but7.hide()
        self.but8.hide()
        self.but9.hide()
        self.but10.hide()
        self.but11.hide()
        self.but12.hide()
        self.but13.hide()
        self.but14.hide()
        if n == 'Сравнение нат. чисел':
            self.hbox1.addWidget(self.N1)
            self.N1.show()
            self.hbox2.addWidget(self.strInput1N1)
            self.strInput1N1.show()
            self.hbox2.addWidget(self.strInput2N1)
            self.strInput2N1.show()
            self.hbox3.addWidget(self.strOutput1)
            self.strOutput1.show()
            self.hbox3.addWidget(self.but1)
            self.but1.show()
        elif n == 'Проверка на ноль':
            self.hbox1.addWidget(self.N2)
            self.N2.show()
            self.hbox2.addWidget(self.strInputN2)
            self.strInputN2.show()
            self.hbox3.addWidget(self.strOutput2)
            self.strOutput2.show()
            self.hbox3.addWidget(self.but2)
            self.but2.show()
        elif n == 'Добавление 1 к нат. числу':
            self.hbox1.addWidget(self.N3)
            self.N3.show()
            self.hbox2.addWidget(self.strInputN2)
            self.strInputN2.show()
            self.hbox3.addWidget(self.strOutput3)
            self.strOutput3.show()
            self.hbox3.addWidget(self.but3)
            self.but3.show()
        elif n == 'Сложение нат. чисел':
            self.hbox1.addWidget(self.N4)
            self.N4.show()
            self.hbox2.addWidget(self.strInput1N1)
            self.strInput1N1.show()
            self.hbox2.addWidget(self.strInput2N1)
            self.strInput2N1.show()
            self.hbox3.addWidget(self.strOutput4)
            self.strOutput4.show()
            self.hbox3.addWidget(self.but4)
            self.but4.show()
        elif n == 'Вычитание из 1-ого бол. мен. нат.':
            self.hbox1.addWidget(self.N5)
            self.N5.show()
            self.hbox2.addWidget(self.strInput1N1)
            self.strInput1N1.show()
            self.hbox2.addWidget(self.strInput2N1)
            self.strInput2N1.show()
            self.hbox3.addWidget(self.strOutput5)
            self.strOutput5.show()
            self.hbox3.addWidget(self.but5)
            self.but5.show()
        elif n == 'Умножение нат. числа на цифру':
            self.hbox1.addWidget(self.N6)
            self.N6.show()
            self.hbox2.addWidget(self.strInputN2)
            self.strInputN2.show()
            self.hbox2.addWidget(self.strInput2N6)
            self.strInput2N6.show()
            self.hbox3.addWidget(self.strOutput6)
            self.strOutput6.show()
            self.hbox3.addWidget(self.but6)
            self.but6.show()
        elif n == 'Умножение нат. числа на 10^k':
            self.hbox1.addWidget(self.N7)
            self.N7.show()
            self.hbox2.addWidget(self.strInputN2)
            self.strInputN2.show()
            self.hbox2.addWidget(self.strInput2N7)
            self.strInput2N7.show()
            self.hbox3.addWidget(self.strOutput7)
            self.strOutput7.show()
            self.hbox3.addWidget(self.but7)
            self.but7.show()
        elif n == 'Умножение нат. чисел':
            self.hbox1.addWidget(self.N8)
            self.N8.show()
            self.hbox2.addWidget(self.strInput1N1)
            self.strInput1N1.show()
            self.hbox2.addWidget(self.strInput2N1)
            self.strInput2N1.show()
            self.hbox3.addWidget(self.strOutput8)
            self.strOutput8.show()
            self.hbox3.addWidget(self.but8)
            self.but8.show()
        elif n == 'Вычитание из нат. др. нат., домн. на цифру':
            self.hbox1.addWidget(self.N9)
            self.N9.show()
            self.hbox2.addWidget(self.strInput1N1)
            self.strInput1N1.show()
            self.hbox2.addWidget(self.strInput2N1)
            self.strInput2N1.show()
            self.hbox2.addWidget(self.strInput2N6)
            self.strInput2N6.show()
            self.hbox3.addWidget(self.strOutput9)
            self.strOutput9.show()
            self.hbox3.addWidget(self.but9)
            self.but9.show()
        elif n == 'Первая цифра от дел. бол. на мен.':
            self.hbox1.addWidget(self.N10)
            self.N10.show()
            self.hbox2.addWidget(self.strInput1N1)
            self.strInput1N1.show()
            self.hbox2.addWidget(self.strInput2N1)
            self.strInput2N1.show()
            self.hbox3.addWidget(self.strOutput10)
            self.strOutput10.show()
            self.hbox3.addWidget(self.but10)
            self.but10.show()
        elif n == 'Частное от дел. бол. на мен.':
            self.hbox1.addWidget(self.N11)
            self.N11.show()
            self.hbox2.addWidget(self.strInput1N1)
            self.strInput1N1.show()
            self.hbox2.addWidget(self.strInput2N1)
            self.strInput2N1.show()
            self.hbox3.addWidget(self.strOutput11)
            self.strOutput11.show()
            self.hbox3.addWidget(self.but11)
            self.but11.show()
        elif n == 'Остаток от дел. бол. на мен.':
            self.hbox1.addWidget(self.N12)
            self.N12.show()
            self.hbox2.addWidget(self.strInput1N1)
            self.strInput1N1.show()
            self.hbox2.addWidget(self.strInput2N1)
            self.strInput2N1.show()
            self.hbox3.addWidget(self.strOutput12)
            self.strOutput12.show()
            self.hbox3.addWidget(self.but12)
            self.but12.show()
        elif n == 'НОД нат. чисел':
            self.hbox1.addWidget(self.N13)
            self.N13.show()
            self.hbox2.addWidget(self.strInput1N1)
            self.strInput1N1.show()
            self.hbox2.addWidget(self.strInput2N1)
            self.strInput2N1.show()
            self.hbox3.addWidget(self.strOutput13)
            self.strOutput13.show()
            self.hbox3.addWidget(self.but13)
            self.but13.show()
        else:
            self.hbox1.addWidget(self.N14)
            self.N14.show()
            self.hbox2.addWidget(self.strInput1N1)
            self.strInput1N1.show()
            self.hbox2.addWidget(self.strInput2N1)
            self.strInput2N1.show()
            self.hbox3.addWidget(self.strOutput14)
            self.strOutput14.show()
            self.hbox3.addWidget(self.but14)
            self.but14.show()
            

class Integer_nums(QWidget):
    def __init__(self,):
        super().__init__()

        self.Z = QLabel('Действия с целыми числами')

        self.Z1 = QLabel('Абсолютная величина числа, результат - натуральное')
        self.Z1.setWordWrap(True)

        self.Z2 = QLabel('Определение положительности числа (2 - положительное, 0 — равное нулю, 1 - отрицательное)')
        self.Z2.setWordWrap(True)
        self.Z2.hide()

        self.Z3 = QLabel('Умножение целого на (-1)')
        self.Z3.setWordWrap(True)
        self.Z3.hide()

        self.Z4 = QLabel('Преобразование натурального в целое')
        self.Z4.setWordWrap(True)
        self.Z4.hide()

        self.Z5 = QLabel('Преобразование целого неотрицательного в натуральное')
        self.Z5.setWordWrap(True)
        self.Z5.hide()

        self.Z6 = QLabel('Сложение целых чисел')
        self.Z6.setWordWrap(True)
        self.Z6.hide()

        self.Z7 = QLabel('Вычитание целых чисел')
        self.Z7.setWordWrap(True)
        self.Z7.hide()

        self.Z8 = QLabel('Умножение целых чисел')
        self.Z8.setWordWrap(True)
        self.Z8.hide()

        self.Z9 = QLabel('Частное от деления целого на целое (делитель отличен от нуля)')
        self.Z9.setWordWrap(True)
        self.Z9.hide()

        self.Z10 = QLabel('Остаток от деления целого на целое(делитель отличен от нуля)')
        self.Z10.setWordWrap(True)
        self.Z10.hide()
        
        self.strInputZ1 = QLineEdit('', self)
        self.strInputZ1.setPlaceholderText('Введите число')

        self.strInput1Z6 = QLineEdit('', self)
        self.strInput1Z6.setPlaceholderText('Введите первое число')
        self.strInput1Z6.hide()
        self.strInput2Z6 = QLineEdit('', self)
        self.strInput2Z6.setPlaceholderText('Введите второе число')
        self.strInput2Z6.hide()

        self.strOutput1 = QLineEdit('', self)
        self.strOutput1.setPlaceholderText('Результат')
        self.strOutput1.setReadOnly(True)

        self.strOutput2 = QLineEdit('', self)
        self.strOutput2.setPlaceholderText('Результат')
        self.strOutput2.setReadOnly(True)
        self.strOutput2.hide()

        self.strOutput3 = QLineEdit('', self)
        self.strOutput3.setPlaceholderText('Результат')
        self.strOutput3.setReadOnly(True)
        self.strOutput3.hide()

        self.strOutput4 = QLineEdit('', self)
        self.strOutput4.setPlaceholderText('Результат')
        self.strOutput4.setReadOnly(True)
        self.strOutput4.hide()

        self.strOutput5 = QLineEdit('', self)
        self.strOutput5.setPlaceholderText('Результат')
        self.strOutput5.setReadOnly(True)
        self.strOutput5.hide()

        self.strOutput6 = QLineEdit('', self)
        self.strOutput6.setPlaceholderText('Результат')
        self.strOutput6.setReadOnly(True)
        self.strOutput6.hide()

        self.strOutput7 = QLineEdit('', self)
        self.strOutput7.setPlaceholderText('Результат')
        self.strOutput7.setReadOnly(True)
        self.strOutput7.hide()

        self.strOutput8 = QLineEdit('', self)
        self.strOutput8.setPlaceholderText('Результат')
        self.strOutput8.setReadOnly(True)
        self.strOutput8.hide()

        self.strOutput9 = QLineEdit('', self)
        self.strOutput9.setPlaceholderText('Результат')
        self.strOutput9.setReadOnly(True)
        self.strOutput9.hide()

        self.strOutput10 = QLineEdit('', self)
        self.strOutput10.setPlaceholderText('Результат')
        self.strOutput10.setReadOnly(True)
        self.strOutput10.hide()

        self.but1 = QPushButton('Посчитать', self)
        self.but1.clicked.connect(self.butt1)

        self.but2 = QPushButton('Посчитать', self)
        self.but2.clicked.connect(self.butt2)
        self.but2.hide()

        self.but3 = QPushButton('Посчитать', self)
        self.but3.clicked.connect(self.butt3)
        self.but3.hide()

        self.but4 = QPushButton('Посчитать', self)
        self.but4.clicked.connect(self.butt4)
        self.but4.hide()

        self.but5 = QPushButton('Посчитать', self)
        self.but5.clicked.connect(self.butt5)
        self.but5.hide()

        self.but6 = QPushButton('Посчитать', self)
        self.but6.clicked.connect(self.butt6)
        self.but6.hide()

        self.but7 = QPushButton('Посчитать', self)
        self.but7.clicked.connect(self.butt7)
        self.but7.hide()

        self.but8 = QPushButton('Посчитать', self)
        self.but8.clicked.connect(self.butt8)
        self.but8.hide()

        self.but9 = QPushButton('Посчитать', self)
        self.but9.clicked.connect(self.butt9)
        self.but9.hide()

        self.but10 = QPushButton('Посчитать', self)
        self.but10.clicked.connect(self.butt10)
        self.but10.hide()

        self.selectZ = QComboBox(self)
        self.selectZ.setFixedSize(200, 25)

        self.selectZ.addItem('Модуль числа')
        self.selectZ.addItem('Положительность числа')
        self.selectZ.addItem('Умножение на (-1)')
        self.selectZ.addItem('Преобразование нат. в цел.')
        self.selectZ.addItem('Преобразование цел. в нат.')
        self.selectZ.addItem('Сложение цел. чисел')
        self.selectZ.addItem('Вычитание цел. чисел')
        self.selectZ.addItem('Умножение цел. чисел')
        self.selectZ.addItem('Частное от деления')
        self.selectZ.addItem('Остаток от деления')

        self.selectZ.currentTextChanged.connect(self.changedZ)

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.Z)
        self.hbox.addWidget(self.selectZ)

        self.hbox1 = QHBoxLayout()
        self.hbox1.addWidget(self.Z1)
        self.hbox1.addWidget(self.Z2)
        self.hbox1.addWidget(self.Z3)
        self.hbox1.addWidget(self.Z4)
        self.hbox1.addWidget(self.Z5)
        self.hbox1.addWidget(self.Z6)
        self.hbox1.addWidget(self.Z7)
        self.hbox1.addWidget(self.Z8)
        self.hbox1.addWidget(self.Z9)
        self.hbox1.addWidget(self.Z10)

        self.hbox2 = QHBoxLayout()
        self.hbox2.addWidget(self.strInputZ1)
        self.hbox2.addWidget(self.strInput1Z6)
        self.hbox2.addWidget(self.strInput2Z6)

        self.hbox3 = QHBoxLayout()
        self.hbox3.addWidget(self.strOutput1)
        self.hbox3.addWidget(self.but1)
        self.hbox3.addWidget(self.strOutput2)
        self.hbox3.addWidget(self.but2)
        self.hbox3.addWidget(self.strOutput3)
        self.hbox3.addWidget(self.but3)
        self.hbox3.addWidget(self.strOutput4)
        self.hbox3.addWidget(self.but4)
        self.hbox3.addWidget(self.strOutput5)
        self.hbox3.addWidget(self.but5)
        self.hbox3.addWidget(self.strOutput6)
        self.hbox3.addWidget(self.but6)
        self.hbox3.addWidget(self.strOutput7)
        self.hbox3.addWidget(self.but7)
        self.hbox3.addWidget(self.strOutput8)
        self.hbox3.addWidget(self.but8)
        self.hbox3.addWidget(self.strOutput9)
        self.hbox3.addWidget(self.but9)
        self.hbox3.addWidget(self.strOutput10)
        self.hbox3.addWidget(self.but10)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)

        self.setLayout(self.vbox)

    def butt1(self):
        try:
            num = integer_nums.ABS_Z_N(integer_nums.STR_TO_INT(self.strInputZ1.text()))
            self.strOutput1.setText(natural_nums.NAT_TO_NORMAL(num))
        except:
            self.strOutput1.setText('Введены недопустимые значения')

    def butt2(self):
        try:
            num = integer_nums.POZ_Z_D(integer_nums.STR_TO_INT(self.strInputZ1.text()))
            self.strOutput2.setText(str(num))
        except:
            self.strOutput2.setText('Введены недопустимые значения')

    def butt3(self):
        try:
            num = integer_nums.MUL_ZM_Z(integer_nums.STR_TO_INT(self.strInputZ1.text()))
            self.strOutput3.setText(integer_nums.INT_TO_NORMAL(num))
        except:
            self.strOutput3.setText('Введены недопустимые значения')

    def butt4(self):
        try:
            num = integer_nums.TRANS_N_Z(natural_nums.STR_TO_NAT(self.strInputZ1.text()))
            self.strOutput4.setText(integer_nums.INT_TO_NORMAL(num))
        except:
            self.strOutput4.setText('Введены недопустимые значения')

    def butt5(self):
        try:
            num = integer_nums.TRANS_Z_N(integer_nums.STR_TO_INT(self.strInputZ1.text()))
            self.strOutput5.setText(natural_nums.NAT_TO_NORMAL(num))
        except:
            self.strOutput5.setText('Введены недопустимые значения')

    def butt6(self):
        try:
            num1 = integer_nums.STR_TO_INT(self.strInput1Z6.text())
            num2 = integer_nums.STR_TO_INT(self.strInput2Z6.text())
            num = integer_nums.ADD_ZZ_Z(num1, num2)
            self.strOutput6.setText(integer_nums.INT_TO_NORMAL(num))
        except:
            self.strOutput6.setText('Введены недопустимые значения')

    def butt7(self):
        try:
            num1 = integer_nums.STR_TO_INT(self.strInput1Z6.text())
            num2 = integer_nums.STR_TO_INT(self.strInput2Z6.text())
            num = integer_nums.SUB_ZZ_Z(num1, num2)
            self.strOutput7.setText(integer_nums.INT_TO_NORMAL(num))
        except:
            self.strOutput7.setText('Введены недопустимые значения')

    def butt8(self):
        try:
            num1 = integer_nums.STR_TO_INT(self.strInput1Z6.text())
            num2 = integer_nums.STR_TO_INT(self.strInput2Z6.text())
            num = integer_nums.MUL_ZZ_Z(num1, num2)
            self.strOutput8.setText(integer_nums.INT_TO_NORMAL(num))
        except:
            self.strOutput8.setText('Введены недопустимые значения')

    def butt9(self):
        try:
            num1 = integer_nums.STR_TO_INT(self.strInput1Z6.text())
            num2 = integer_nums.STR_TO_INT(self.strInput2Z6.text())
            num = integer_nums.DIV_ZZ_Z(num1, num2)
            self.strOutput9.setText(integer_nums.INT_TO_NORMAL(num))
        except:
            self.strOutput9.setText('Введены недопустимые значения')

    def butt10(self):
        try:
            num1 = integer_nums.STR_TO_INT(self.strInput1Z6.text())
            num2 = integer_nums.STR_TO_INT(self.strInput2Z6.text())
            num = integer_nums.MOD_ZZ_Z(num1, num2)
            self.strOutput10.setText(integer_nums.INT_TO_NORMAL(num))
        except:
            self.strOutput10.setText('Введены недопустимые значения')

    def changedZ(self):
        z = self.selectZ.currentText()
        self.Z1.hide()
        self.Z2.hide()
        self.Z3.hide()
        self.Z4.hide()
        self.Z5.hide()
        self.Z6.hide()
        self.Z7.hide()
        self.Z8.hide()
        self.Z9.hide()
        self.Z10.hide()
        self.strInputZ1.hide()
        self.strInput1Z6.hide()
        self.strInput2Z6.hide()
        self.strOutput1.hide()
        self.strOutput2.hide()
        self.strOutput3.hide()
        self.strOutput4.hide()
        self.strOutput5.hide()
        self.strOutput6.hide()
        self.strOutput7.hide()
        self.strOutput8.hide()
        self.strOutput9.hide()
        self.strOutput10.hide()
        self.but1.hide()
        self.but2.hide()
        self.but3.hide()
        self.but4.hide()
        self.but5.hide()
        self.but6.hide()
        self.but7.hide()
        self.but8.hide()
        self.but9.hide()
        self.but10.hide()
        if z == 'Модуль числа':
            self.Z1.show()
            self.strInputZ1.show()
            self.strOutput1.show()
            self.but1.show()
        elif z == 'Положительность числа':
            self.Z2.show()
            self.strInputZ1.show()
            self.strOutput2.show()
            self.but2.show()
        elif z == 'Умножение на (-1)':
            self.Z3.show()
            self.strInputZ1.show()
            self.strOutput3.show()
            self.but3.show()
        elif z == 'Преобразование нат. в цел.':
            self.Z4.show()
            self.strInputZ1.show()
            self.strOutput4.show()
            self.but4.show()
        elif z == 'Преобразование цел. в нат.':
            self.Z5.show()
            self.strInputZ1.show()
            self.strOutput5.show()
            self.but5.show()
        elif z == 'Сложение цел. чисел':
            self.Z6.show()
            self.strInput1Z6.show()
            self.strInput2Z6.show()
            self.strOutput6.show()
            self.but6.show()
        elif z == 'Вычитание цел. чисел':
            self.Z7.show()
            self.strInput1Z6.show()
            self.strInput2Z6.show()
            self.strOutput7.show()
            self.but7.show()
        elif z == 'Умножение цел. чисел':
            self.Z8.show()
            self.strInput1Z6.show()
            self.strInput2Z6.show()
            self.strOutput8.show()
            self.but8.show()
        elif z == 'Частное от деления':
            self.Z9.show()
            self.strInput1Z6.show()
            self.strInput2Z6.show()
            self.strOutput9.show()
            self.but9.show()
        else:
            self.Z10.show()
            self.strInput1Z6.show()
            self.strInput2Z6.show()
            self.strOutput10.show()
            self.but10.show()

class Rational_nums(QWidget):
    def __init__(self):
        super().__init__()

        self.Q = QLabel('Действия с рациональными числами')

        self.Q1 = QLabel('Сокращение дроби')
        self.Q1.setWordWrap(True)

        self.Q2 = QLabel('Проверка на целое, если рациональное число является целым, то «да», иначе «нет»')
        self.Q2.setWordWrap(True)
        self.Q2.hide()

        self.Q3 = QLabel('Преобразование целого в дробное')
        self.Q3.setWordWrap(True)
        self.Q3.hide()

        self.Q4 = QLabel('Преобразование дробного в целое (если знаменатель равен 1)')
        self.Q4.setWordWrap(True)
        self.Q4.hide()

        self.Q5 = QLabel('Сложение дробей')
        self.Q5.setWordWrap(True)
        self.Q5.hide()

        self.Q6 = QLabel('Вычитание дробей')
        self.Q6.setWordWrap(True)
        self.Q6.hide()

        self.Q7 = QLabel('Умножение дробей')
        self.Q7.setWordWrap(True)
        self.Q7.hide()

        self.Q8 = QLabel('Деление дробей (делитель отличен от нуля)')
        self.Q8.setWordWrap(True)
        self.Q8.hide()
        
        self.strInput1Q1 = QLineEdit('', self)
        self.strInput1Q1.setPlaceholderText('Введите числитель')
        self.strInput2Q1 = QLineEdit('', self)
        self.strInput2Q1.setPlaceholderText('Введите знаменатель')

        self.strInputQ3 = QLineEdit('', self)
        self.strInputQ3.setPlaceholderText('Введите число')
        self.strInputQ3.hide()

        self.strInput1Q5 = QLineEdit('', self)
        self.strInput1Q5.setPlaceholderText('Введите числитель первого числа')
        self.strInput1Q5.hide()
        self.strInput2Q5 = QLineEdit('', self)
        self.strInput2Q5.setPlaceholderText('Введите знаменатель первого числа')
        self.strInput2Q5.hide()
        self.strInput3Q5 = QLineEdit('', self)
        self.strInput3Q5.setPlaceholderText('Введите числитель второго числа')
        self.strInput3Q5.hide()
        self.strInput4Q5 = QLineEdit('', self)
        self.strInput4Q5.setPlaceholderText('Введите знаменатель второго числа')
        self.strInput4Q5.hide()

        self.strOutput1 = QLineEdit('', self)
        self.strOutput1.setPlaceholderText('Результат')
        self.strOutput1.setReadOnly(True)

        self.strOutput2 = QLineEdit('', self)
        self.strOutput2.setPlaceholderText('Результат')
        self.strOutput2.setReadOnly(True)
        self.strOutput2.hide()

        self.strOutput3 = QLineEdit('', self)
        self.strOutput3.setPlaceholderText('Результат')
        self.strOutput3.setReadOnly(True)
        self.strOutput3.hide()

        self.strOutput4 = QLineEdit('', self)
        self.strOutput4.setPlaceholderText('Результат')
        self.strOutput4.setReadOnly(True)
        self.strOutput4.hide()

        self.strOutput5 = QLineEdit('', self)
        self.strOutput5.setPlaceholderText('Результат')
        self.strOutput5.setReadOnly(True)
        self.strOutput5.hide()

        self.strOutput6 = QLineEdit('', self)
        self.strOutput6.setPlaceholderText('Результат')
        self.strOutput6.setReadOnly(True)
        self.strOutput6.hide()

        self.strOutput7 = QLineEdit('', self)
        self.strOutput7.setPlaceholderText('Результат')
        self.strOutput7.setReadOnly(True)
        self.strOutput7.hide()

        self.strOutput8 = QLineEdit('', self)
        self.strOutput8.setPlaceholderText('Результат')
        self.strOutput8.setReadOnly(True)
        self.strOutput8.hide()

        self.but1 = QPushButton('Посчитать', self)
        self.but1.clicked.connect(self.butt1)

        self.but2 = QPushButton('Посчитать', self)
        self.but2.clicked.connect(self.butt2)
        self.but2.hide()

        self.but3 = QPushButton('Посчитать', self)
        self.but3.clicked.connect(self.butt3)
        self.but3.hide()

        self.but4 = QPushButton('Посчитать', self)
        self.but4.clicked.connect(self.butt4)
        self.but4.hide()

        self.but5 = QPushButton('Посчитать', self)
        self.but5.clicked.connect(self.butt5)
        self.but5.hide()

        self.but6 = QPushButton('Посчитать', self)
        self.but6.clicked.connect(self.butt6)
        self.but6.hide()

        self.but7 = QPushButton('Посчитать', self)
        self.but7.clicked.connect(self.butt7)
        self.but7.hide()

        self.but8 = QPushButton('Посчитать', self)
        self.but8.clicked.connect(self.butt8)
        self.but8.hide()

        self.selectQ = QComboBox(self)
        self.selectQ.setFixedSize(200, 25)

        self.selectQ.addItem('Сокращение дроби')
        self.selectQ.addItem('Проверка на целое')
        self.selectQ.addItem('Преобразование цел. в дроб.')
        self.selectQ.addItem('Преобразование дроб. в цел.')
        self.selectQ.addItem('Сложение дробей')
        self.selectQ.addItem('Вычитание дробей')
        self.selectQ.addItem('Умножение дробей')
        self.selectQ.addItem('Деление дробей')

        self.selectQ.currentTextChanged.connect(self.changedQ)

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.Q)
        self.hbox.addWidget(self.selectQ)

        self.hbox1 = QHBoxLayout()
        self.hbox1.addWidget(self.Q1)

        self.hbox2 = QHBoxLayout()
        self.hbox2.addWidget(self.strInput1Q1)

        self.hbox3 = QHBoxLayout()
        self.hbox3.addWidget(self.strInput2Q1)

        self.hbox4 = QHBoxLayout()
        self.hbox4.addWidget(self.strOutput1)
        self.hbox4.addWidget(self.but1)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)

        self.setLayout(self.vbox)

    def butt1(self):
        try:
            n = self.strInput1Q1.text()
            d = self.strInput2Q1.text()
            num = rational_nums.STR_TO_RAT(n, d)
            num = rational_nums.RED_Q_Q(num)
            self.strOutput1.setText(rational_nums.RAT_TO_NORMAL(num))
        except:
            self.strOutput1.setText('Введены недопустимые значения')

    def butt2(self):
        try:
            n = self.strInput1Q1.text()
            d = self.strInput2Q1.text()
            num = rational_nums.STR_TO_RAT(n, d)
            num = rational_nums.INT_Q_B(num)
            self.strOutput2.setText(num)
        except:
            self.strOutput2.setText('Введены недопустимые значения')

    def butt3(self):
        try:
            n = self.strInputQ3.text()
            num = integer_nums.STR_TO_INT(n)
            num = rational_nums.TRANS_Z_Q(num)
            self.strOutput3.setText(rational_nums.RAT_TO_NORMAL(num))
        except:
            self.strOutput3.setText('Введены недопустимые значения')

    def butt4(self):
        try:
            n = self.strInput1Q1.text()
            d = self.strInput2Q1.text()
            num = rational_nums.STR_TO_RAT(n, d)
            num = rational_nums.TRANS_Q_Z(num)
            self.strOutput4.setText(integer_nums.INT_TO_NORMAL(num))
        except:
            self.strOutput4.setText('Введены недопустимые значения')

    def butt5(self):
        try:
            num1 = rational_nums.STR_TO_RAT(self.strInput1Q5.text(), self.strInput2Q5.text())
            num2 = rational_nums.STR_TO_RAT(self.strInput3Q5.text(), self.strInput4Q5.text())
            num = rational_nums.ADD_QQ_Q(num1, num2)
            self.strOutput5.setText(rational_nums.RAT_TO_NORMAL(num))
        except:
            self.strOutput5.setText('Введены недопустимые значения')

    def butt6(self):
        try:
            num1 = rational_nums.STR_TO_RAT(self.strInput1Q5.text(), self.strInput2Q5.text())
            num2 = rational_nums.STR_TO_RAT(self.strInput3Q5.text(), self.strInput4Q5.text())
            num = rational_nums.SUB_QQ_Q(num1, num2)
            self.strOutput6.setText(rational_nums.RAT_TO_NORMAL(num))
        except:
            self.strOutput6.setText('Введены недопустимые значения')

    def butt7(self):
        try:
            num1 = rational_nums.STR_TO_RAT(self.strInput1Q5.text(), self.strInput2Q5.text())
            num2 = rational_nums.STR_TO_RAT(self.strInput3Q5.text(), self.strInput4Q5.text())
            num = rational_nums.MUL_QQ_Q(num1, num2)
            self.strOutput7.setText(rational_nums.RAT_TO_NORMAL(num))
        except:
            self.strOutput7.setText('Введены недопустимые значения')

    def butt8(self):
        try:
            num1 = rational_nums.STR_TO_RAT(self.strInput1Q5.text(), self.strInput2Q5.text())
            num2 = rational_nums.STR_TO_RAT(self.strInput3Q5.text(), self.strInput4Q5.text())
            num = rational_nums.DIV_QQ_Q(num1, num2)
            print(num1, num2)
            self.strOutput8.setText(rational_nums.RAT_TO_NORMAL(num))
        except:
            self.strOutput8.setText('Введены недопустимые значения')

    def changedQ(self):
        q = self.selectQ.currentText()
        self.hbox1.itemAt(0).widget().setParent(None)
        for i in reversed(range(self.hbox2.count())):
            self.hbox2.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.hbox3.count())):
            self.hbox3.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.hbox4.count())):
            self.hbox4.itemAt(i).widget().setParent(None)
        if q == 'Сокращение дроби':
            self.hbox1.addWidget(self.Q1)
            self.Q1.show()
            self.hbox2.addWidget(self.strInput1Q1)
            self.strInput1Q1.show()
            self.hbox3.addWidget(self.strInput2Q1)
            self.strInput2Q1.show()
            self.hbox4.addWidget(self.strOutput1)
            self.strOutput1.show()
            self.hbox4.addWidget(self.but1)
            self.but1.show()
        elif q == 'Проверка на целое':
            self.hbox1.addWidget(self.Q2)
            self.Q2.show()
            self.hbox2.addWidget(self.strInput1Q1)
            self.strInput1Q1.show()
            self.hbox3.addWidget(self.strInput2Q1)
            self.strInput2Q1.show()
            self.hbox4.addWidget(self.strOutput2)
            self.strOutput2.show()
            self.hbox4.addWidget(self.but2)
            self.but2.show()
        elif q == 'Преобразование цел. в дроб.':
            self.hbox1.addWidget(self.Q3)
            self.Q3.show()
            self.hbox2.addWidget(self.strInputQ3)
            self.strInputQ3.show()
            self.hbox4.addWidget(self.strOutput3)
            self.strOutput3.show()
            self.hbox4.addWidget(self.but3)
            self.but3.show()
        elif q == 'Преобразование дроб. в цел.':
            self.hbox1.addWidget(self.Q4)
            self.Q4.show()
            self.hbox2.addWidget(self.strInput1Q1)
            self.strInput1Q1.show()
            self.hbox3.addWidget(self.strInput2Q1)
            self.strInput2Q1.show()
            self.hbox4.addWidget(self.strOutput4)
            self.strOutput4.show()
            self.hbox4.addWidget(self.but4)
            self.but4.show()
        elif q == 'Сложение дробей':
            self.hbox1.addWidget(self.Q5)
            self.Q5.show()
            self.hbox2.addWidget(self.strInput1Q5)
            self.strInput1Q5.show()
            self.hbox2.addWidget(self.strInput3Q5)
            self.strInput3Q5.show()
            self.hbox3.addWidget(self.strInput2Q5)
            self.strInput2Q5.show()
            self.hbox3.addWidget(self.strInput4Q5)
            self.strInput4Q5.show()
            self.hbox4.addWidget(self.strOutput5)
            self.strOutput5.show()
            self.hbox4.addWidget(self.but5)
            self.but5.show()
        elif q == 'Вычитание дробей':
            self.hbox1.addWidget(self.Q6)
            self.Q6.show()
            self.hbox2.addWidget(self.strInput1Q5)
            self.strInput1Q5.show()
            self.hbox2.addWidget(self.strInput3Q5)
            self.strInput3Q5.show()
            self.hbox3.addWidget(self.strInput2Q5)
            self.strInput2Q5.show()
            self.hbox3.addWidget(self.strInput4Q5)
            self.strInput4Q5.show()
            self.hbox4.addWidget(self.strOutput6)
            self.strOutput6.show()
            self.hbox4.addWidget(self.but6)
            self.but6.show()
        elif q == 'Умножение дробей':
            self.hbox1.addWidget(self.Q7)
            self.Q7.show()
            self.hbox2.addWidget(self.strInput1Q5)
            self.strInput1Q5.show()
            self.hbox2.addWidget(self.strInput3Q5)
            self.strInput3Q5.show()
            self.hbox3.addWidget(self.strInput2Q5)
            self.strInput2Q5.show()
            self.hbox3.addWidget(self.strInput4Q5)
            self.strInput4Q5.show()
            self.hbox4.addWidget(self.strOutput7)
            self.strOutput7.show()
            self.hbox4.addWidget(self.but7)
            self.but7.show()
        else:
            self.hbox1.addWidget(self.Q8)
            self.Q8.show()
            self.hbox2.addWidget(self.strInput1Q5)
            self.strInput1Q5.show()
            self.hbox2.addWidget(self.strInput3Q5)
            self.strInput3Q5.show()
            self.hbox3.addWidget(self.strInput2Q5)
            self.strInput2Q5.show()
            self.hbox3.addWidget(self.strInput4Q5)
            self.strInput4Q5.show()
            self.hbox4.addWidget(self.strOutput8)
            self.strOutput8.show()
            self.hbox4.addWidget(self.but8)
            self.but8.show()

class Polynomial(QWidget):
    def __init__(self):
        super().__init__()

        self.P = QLabel('Действия с многочленами')

        self.P1 = QLabel('Сложение многочленов')
        self.P1.setWordWrap(True)

        self.P2 = QLabel('Вычитание многочленов')
        self.P2.setWordWrap(True)
        self.P2.hide()

        self.P3 = QLabel('Умножение многочлена на рациональное число')
        self.P3.setWordWrap(True)
        self.P3.hide()

        self.P4 = QLabel('Умножение многочлена на x^k')
        self.P4.setWordWrap(True)
        self.P4.hide()

        self.P5 = QLabel('Старший коэффициент многочлена')
        self.P5.setWordWrap(True)
        self.P5.hide()

        self.P6 = QLabel('Степень многочлена')
        self.P6.setWordWrap(True)
        self.P6.hide()

        self.P7 = QLabel('Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей')
        self.P7.setWordWrap(True)
        self.P7.hide()

        self.P8 = QLabel('Умножение многочленов')
        self.P8.setWordWrap(True)
        self.P8.hide()

        self.P9 = QLabel('Частное от деления многочлена на многочлен при делении с остатком')
        self.P9.setWordWrap(True)
        self.P9.hide()

        self.P10 = QLabel('Остаток от деления многочлена на многочлен при делении с остатком')
        self.P10.setWordWrap(True)
        self.P10.hide()

        self.P11 = QLabel('НОД многочленов')
        self.P11.setWordWrap(True)
        self.P11.hide()

        self.P12 = QLabel('Производная многочлена')
        self.P12.setWordWrap(True)
        self.P12.hide()

        self.P13 = QLabel('Преобразование многочлена — кратные корни в простые')
        self.P13.setWordWrap(True)
        self.P13.hide()
        
        self.strInput1P1 = QLineEdit('', self)
        self.strInput1P1.setPlaceholderText('Введите степень первого многочлена')
        self.strInput2P1 = QLineEdit('', self)
        self.strInput2P1.setPlaceholderText('Введите коэффициенты первого многочлена')
        self.strInput3P1 = QLineEdit('', self)
        self.strInput3P1.setPlaceholderText('Введите степень второго многочлена')
        self.strInput4P1 = QLineEdit('', self)
        self.strInput4P1.setPlaceholderText('Введите коэффициенты второго многочлена')

        self.strInput1P3 = QLineEdit('', self)
        self.strInput1P3.setPlaceholderText('Введите степень многочлена')
        self.strInput1P3.hide()
        self.strInput2P3 = QLineEdit('', self)
        self.strInput2P3.setPlaceholderText('Введите коэффициенты многочлена')
        self.strInput2P3.hide()
        self.strInput3P3 = QLineEdit('', self)
        self.strInput3P3.setPlaceholderText('Введите числитель')
        self.strInput3P3.hide()
        self.strInput4P3 = QLineEdit('', self)
        self.strInput4P3.setPlaceholderText('Введите знаменатель')
        self.strInput4P3.hide()

        self.strInput3P4 = QLineEdit('', self)
        self.strInput3P4.setPlaceholderText('Введите степень x^k')
        self.strInput3P4.hide()

        self.strOutput1 = QLineEdit('', self)
        self.strOutput1.setPlaceholderText('Результат')
        self.strOutput1.setReadOnly(True)

        self.strOutput2 = QLineEdit('', self)
        self.strOutput2.setPlaceholderText('Результат')
        self.strOutput2.setReadOnly(True)
        self.strOutput2.hide()

        self.strOutput3 = QLineEdit('', self)
        self.strOutput3.setPlaceholderText('Результат')
        self.strOutput3.setReadOnly(True)
        self.strOutput3.hide()

        self.strOutput4 = QLineEdit('', self)
        self.strOutput4.setPlaceholderText('Результат')
        self.strOutput4.setReadOnly(True)
        self.strOutput4.hide()

        self.strOutput5 = QLineEdit('', self)
        self.strOutput5.setPlaceholderText('Результат')
        self.strOutput5.setReadOnly(True)
        self.strOutput5.hide()

        self.strOutput6 = QLineEdit('', self)
        self.strOutput6.setPlaceholderText('Результат')
        self.strOutput6.setReadOnly(True)
        self.strOutput6.hide()

        self.strOutput7 = QLineEdit('', self)
        self.strOutput7.setPlaceholderText('Результат')
        self.strOutput7.setReadOnly(True)
        self.strOutput7.hide()

        self.strOutput8 = QLineEdit('', self)
        self.strOutput8.setPlaceholderText('Результат')
        self.strOutput8.setReadOnly(True)
        self.strOutput8.hide()

        self.strOutput9 = QLineEdit('', self)
        self.strOutput9.setPlaceholderText('Результат')
        self.strOutput9.setReadOnly(True)
        self.strOutput9.hide()

        self.strOutput10 = QLineEdit('', self)
        self.strOutput10.setPlaceholderText('Результат')
        self.strOutput10.setReadOnly(True)
        self.strOutput10.hide()

        self.strOutput11 = QLineEdit('', self)
        self.strOutput11.setPlaceholderText('Результат')
        self.strOutput11.setReadOnly(True)
        self.strOutput11.hide()

        self.strOutput12 = QLineEdit('', self)
        self.strOutput12.setPlaceholderText('Результат')
        self.strOutput12.setReadOnly(True)
        self.strOutput12.hide()

        self.strOutput13 = QLineEdit('', self)
        self.strOutput13.setPlaceholderText('Результат')
        self.strOutput13.setReadOnly(True)
        self.strOutput13.hide()


        self.but1 = QPushButton('Посчитать', self)
        self.but1.clicked.connect(self.butt1)

        self.but2 = QPushButton('Посчитать', self)
        self.but2.clicked.connect(self.butt2)
        self.but2.hide()

        self.but3 = QPushButton('Посчитать', self)
        self.but3.clicked.connect(self.butt3)
        self.but3.hide()

        self.but4 = QPushButton('Посчитать', self)
        self.but4.clicked.connect(self.butt4)
        self.but4.hide()

        self.but5 = QPushButton('Посчитать', self)
        self.but5.clicked.connect(self.butt5)
        self.but5.hide()

        self.but6 = QPushButton('Посчитать', self)
        self.but6.clicked.connect(self.butt6)
        self.but6.hide()

        self.but7 = QPushButton('Посчитать', self)
        self.but7.clicked.connect(self.butt7)
        self.but7.hide()

        self.but8 = QPushButton('Посчитать', self)
        self.but8.clicked.connect(self.butt8)
        self.but8.hide()

        self.but9 = QPushButton('Посчитать', self)
        self.but9.clicked.connect(self.butt9)
        self.but9.hide()

        self.but10 = QPushButton('Посчитать', self)
        self.but10.clicked.connect(self.butt10)
        self.but10.hide()

        self.but11 = QPushButton('Посчитать', self)
        self.but11.clicked.connect(self.butt11)
        self.but11.hide()

        self.but12 = QPushButton('Посчитать', self)
        self.but12.clicked.connect(self.butt12)
        self.but12.hide()

        self.but13 = QPushButton('Посчитать', self)
        self.but13.clicked.connect(self.butt13)
        self.but13.hide()

        self.selectP = QComboBox(self)
        self.selectP.setFixedSize(200, 25)

        self.selectP.addItem('Сложение многочленов')
        self.selectP.addItem('Вычитание многочленов')
        self.selectP.addItem('Умножение на число')
        self.selectP.addItem('Умножение на x^k')
        self.selectP.addItem('Старший коэфф.')
        self.selectP.addItem('Степень многочлена')
        self.selectP.addItem('НОД/НОК')
        self.selectP.addItem('Умножение многочленов')
        self.selectP.addItem('Частное от деления')
        self.selectP.addItem('Остаток от деления')
        self.selectP.addItem('НОД многочленов')
        self.selectP.addItem('Производная')
        self.selectP.addItem('Простые корни')

        self.selectP.currentTextChanged.connect(self.changedP)

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.P)
        self.hbox.addWidget(self.selectP)

        self.hbox1 = QHBoxLayout()
        self.hbox1.addWidget(self.P1)

        self.hbox2 = QHBoxLayout()
        self.hbox2.addWidget(self.strInput1P1)
        self.hbox2.addWidget(self.strInput3P1)

        self.hbox3 = QHBoxLayout()
        self.hbox3.addWidget(self.strInput2P1)
        self.hbox3.addWidget(self.strInput4P1)

        self.hbox4 = QHBoxLayout()
        self.hbox4.addWidget(self.strOutput1)
        self.hbox4.addWidget(self.but1)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)

        self.setLayout(self.vbox)

    def butt1(self):
        try:
            k1 = int(self.strInput1P1.text())
            c1 = self.strInput2P1.text()
            k2 = int(self.strInput3P1.text())
            c2 = self.strInput4P1.text()
            pol1 = polynomial.STR_TO_POL(k1, c1)
            pol2 = polynomial.STR_TO_POL(k2, c2)
            pol = polynomial.ADD_PP_P(pol1, pol2)
            self.strOutput1.setText(polynomial.POL_TO_NORMAL(pol))
        except:
            self.strOutput1.setText('Ошибка в водимых данных')

    def butt2(self):
        try:
            k1 = int(self.strInput1P1.text())
            c1 = self.strInput2P1.text()
            k2 = int(self.strInput3P1.text())
            c2 = self.strInput4P1.text()
            pol1 = polynomial.STR_TO_POL(k1, c1)
            pol2 = polynomial.STR_TO_POL(k2, c2)
            pol = polynomial.SUB_PP_P(pol1, pol2)
            self.strOutput2.setText(polynomial.POL_TO_NORMAL(pol))
        except:
            self.strOutput2.setText('Ошибка в водимых данных')

    def butt3(self):
        try:
            k1 = int(self.strInput1P3.text())
            c1 = self.strInput2P3.text()
            k2 = int(self.strInput3P3.text())
            c2 = self.strInput4P3.text()
            pol1 = polynomial.STR_TO_POL(k1, c1)
            rat = rational.STR_TO_RAT(k2, c2)
            pol = polynomial.MUL_PQ_P(rat, pol1)
            self.strOutput3.setText(polynomial.POL_TO_NORMAL(pol))
        except:
            self.strOutput3.setText('Ошибка в водимых данных')

    def butt4(self):
        try:
            k1 = int(self.strInput1P3.text())
            c1 = self.strInput2P3.text()
            k2 = int(self.strInput3P4.text())
            pol1 = polynomial.STR_TO_POL(k1, c1)
            pol = polynomial.MUL_Pxk_P(pol1, k2)
            self.strOutput4.setText(polynomial.POL_TO_NORMAL(pol))
        except:
            self.strOutput4.setText('Ошибка в водимых данных')

    def butt5(self):
        try:
            k1 = int(self.strInput1P3.text())
            c1 = self.strInput2P3.text()
            pol1 = polynomial.STR_TO_POL(k1, c1)
            rat = polynomial.LED_P_Q(pol1)
            self.strOutput5.setText(rational_nums.RAT_TO_NORMAL(rat))
        except:
            self.strOutput5.setText('Ошибка в водимых данных')

    def butt6(self):
        try:
            k1 = int(self.strInput1P3.text())
            c1 = self.strInput2P3.text()
            pol1 = polynomial.STR_TO_POL(k1, c1)
            k = polynomial.DEG_P_N(pol1)
            self.strOutput6.setText(str(k))
        except:
            self.strOutput6.setText('Ошибка в водимых данных')

    def butt7(self):
        try:
            k1 = int(self.strInput1P3.text())
            c1 = self.strInput2P3.text()
            pol1 = polynomial.STR_TO_POL(k1, c1)
            mas = polynomial.FAC_P_Q(pol1)
            self.strOutput7.setText(mas)
        except:
            self.strOutput7.setText('Ошибка в водимых данных')

    def butt8(self):
        try:
            kk1 = int(self.strInput1P1.text())
            c1 = self.strInput2P1.text()
            k2 = int(self.strInput3P1.text())
            c2 = self.strInput4P1.text()
            pol1 = polynomial.STR_TO_POL(k1, c1)
            pol2 = polynomial.STR_TO_POL(k2, c2)
            pol = polynomial.MUL_PP_P(pol1, pol2)
            self.strOutput8.setText(polynomial.POL_TO_NORMAL(pol))
        except:
            self.strOutput8.setText('Ошибка в водимых данных')

    def butt9(self):
        try:
            kk1 = int(self.strInput1P1.text())
            c1 = self.strInput2P1.text()
            k2 = int(self.strInput3P1.text())
            c2 = self.strInput4P1.text()
            pol1 = polynomial.STR_TO_POL(k1, c1)
            pol2 = polynomial.STR_TO_POL(k2, c2)
            pol = polynomial.DIV_PP_P(pol1, pol2)
            self.strOutput9.setText(polynomial.POL_TO_NORMAL(pol))
        except:
            self.strOutput9.setText('Ошибка в водимых данных')

    def butt10(self):
        try:
            kk1 = int(self.strInput1P1.text())
            c1 = self.strInput2P1.text()
            k2 = int(self.strInput3P1.text())
            c2 = self.strInput4P1.text()
            pol1 = polynomial.STR_TO_POL(k1, c1)
            pol2 = polynomial.STR_TO_POL(k2, c2)
            pol = polynomial.MOD_PP_P(pol1, pol2)
            self.strOutput10.setText(polynomial.POL_TO_NORMAL(pol))
        except:
            self.strOutput10.setText('Ошибка в водимых данных')

    def butt11(self):
        try:
            kk1 = int(self.strInput1P1.text())
            c1 = self.strInput2P1.text()
            k2 = int(self.strInput3P1.text())
            c2 = self.strInput4P1.text()
            pol1 = polynomial.STR_TO_POL(k1, c1)
            pol2 = polynomial.STR_TO_POL(k2, c2)
            pol = polynomial.GCF_PP_P(pol1, pol2)
            self.strOutput11.setText(polynomial.POL_TO_NORMAL(pol))
        except:
            self.strOutput11.setText('Ошибка в водимых данных')

    def butt12(self):
        try:
            k1 = int(self.strInput1P3.text())
            c1 = self.strInput2P3.text()
            pol1 = polynomial.STR_TO_POL(k1, c1)
            pol = polynomial.DER_P_P(pol1)
            self.strOutput12.setText(polynomial.POL_TO_NORMAL(pol))
        except:
            self.strOutput12.setText('Ошибка в водимых данных')

    def butt13(self):
        try:
            self.strOutput13.setText(polynomial.POL_TO_NORMAL(pol))
        except:
            self.strOutput13.setText('Ошибка в водимых данных')

    def changedP(self):
        p = self.selectP.currentText()
        self.hbox1.itemAt(0).widget().setParent(None)
        for i in reversed(range(self.hbox2.count())):
            self.hbox2.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.hbox3.count())):
            self.hbox3.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.hbox4.count())):
            self.hbox4.itemAt(i).widget().setParent(None)
        if p == 'Сложение многочленов':
            self.hbox1.addWidget(self.P1)
            self.P1.show()
            self.hbox2.addWidget(self.strInput1P1)
            self.strInput1P1.show()
            self.hbox2.addWidget(self.strInput3P1)
            self.strInput3P1.show()
            self.hbox3.addWidget(self.strInput2P1)
            self.strInput2P1.show()
            self.hbox3.addWidget(self.strInput4P1)
            self.strInput4P1.show()
            self.hbox4.addWidget(self.strOutput1)
            self.strOutput1.show()
            self.hbox4.addWidget(self.but1)
            self.but1.show()
        elif p == 'Вычитание многочленов':
            self.hbox1.addWidget(self.P2)
            self.P2.show()
            self.hbox2.addWidget(self.strInput1P1)
            self.strInput1P1.show()
            self.hbox2.addWidget(self.strInput3P1)
            self.strInput3P1.show()
            self.hbox3.addWidget(self.strInput2P1)
            self.strInput2P1.show()
            self.hbox3.addWidget(self.strInput4P1)
            self.strInput4P1.show()
            self.hbox4.addWidget(self.strOutput2)
            self.strOutput2.show()
            self.hbox4.addWidget(self.but2)
            self.but2.show()
        elif p == 'Умножение на число':
            self.hbox1.addWidget(self.P3)
            self.P3.show()
            self.hbox2.addWidget(self.strInput1P3)
            self.strInput1P3.show()
            self.hbox2.addWidget(self.strInput3P3)
            self.strInput3P3.show()
            self.hbox3.addWidget(self.strInput2P3)
            self.strInput2P3.show()
            self.hbox3.addWidget(self.strInput4P3)
            self.strInput4P3.show()
            self.hbox4.addWidget(self.strOutput3)
            self.strOutput3.show()
            self.hbox4.addWidget(self.but3)
            self.but3.show()
        elif p == 'Умножение на x^k':
            self.hbox1.addWidget(self.P4)
            self.P4.show()
            self.hbox2.addWidget(self.strInput1P3)
            self.strInput1P3.show()
            self.hbox3.addWidget(self.strInput2P3)
            self.strInput2P3.show()
            self.hbox3.addWidget(self.strInput3P4)
            self.strInput3P4.show()
            self.hbox4.addWidget(self.strOutput4)
            self.strOutput4.show()
            self.hbox4.addWidget(self.but4)
            self.but4.show()
        elif p == 'Старший коэфф.':
            self.hbox1.addWidget(self.P5)
            self.P5.show()
            self.hbox2.addWidget(self.strInput1P3)
            self.strInput1P3.show()
            self.hbox3.addWidget(self.strInput2P3)
            self.strInput2P3.show()
            self.hbox4.addWidget(self.strOutput5)
            self.strOutput5.show()
            self.hbox4.addWidget(self.but5)
            self.but5.show()
        elif p == 'Степень многочлена':
            self.hbox1.addWidget(self.P6)
            self.P6.show()
            self.hbox2.addWidget(self.strInput1P3)
            self.strInput1P3.show()
            self.hbox3.addWidget(self.strInput2P3)
            self.strInput2P3.show()
            self.hbox4.addWidget(self.strOutput6)
            self.strOutput6.show()
            self.hbox4.addWidget(self.but6)
            self.but6.show()
        elif p == 'НОД/НОК':
            self.hbox1.addWidget(self.P7)
            self.P7.show()
            self.hbox2.addWidget(self.strInput1P3)
            self.strInput1P3.show()
            self.hbox3.addWidget(self.strInput2P3)
            self.strInput2P3.show()
            self.hbox4.addWidget(self.strOutput7)
            self.strOutput7.show()
            self.hbox4.addWidget(self.but7)
            self.but7.show()
        elif p == 'Умножение многочленов':
            self.hbox1.addWidget(self.P8)
            self.P8.show()
            self.hbox2.addWidget(self.strInput1P1)
            self.strInput1P1.show()
            self.hbox2.addWidget(self.strInput3P1)
            self.strInput3P1.show()
            self.hbox3.addWidget(self.strInput2P1)
            self.strInput2P1.show()
            self.hbox3.addWidget(self.strInput4P1)
            self.strInput4P1.show()
            self.hbox4.addWidget(self.strOutput8)
            self.strOutput8.show()
            self.hbox4.addWidget(self.but8)
            self.but8.show()
        elif p == 'Частное от деления':
            self.hbox1.addWidget(self.P9)
            self.P9.show()
            self.hbox2.addWidget(self.strInput1P1)
            self.strInput1P1.show()
            self.hbox2.addWidget(self.strInput3P1)
            self.strInput3P1.show()
            self.hbox3.addWidget(self.strInput2P1)
            self.strInput2P1.show()
            self.hbox3.addWidget(self.strInput4P1)
            self.strInput4P1.show()
            self.hbox4.addWidget(self.strOutput9)
            self.strOutput9.show()
            self.hbox4.addWidget(self.but9)
            self.but9.show()
        elif p == 'Остаток от деления':
            self.hbox1.addWidget(self.P10)
            self.P10.show()
            self.hbox2.addWidget(self.strInput1P1)
            self.strInput1P1.show()
            self.hbox2.addWidget(self.strInput3P1)
            self.strInput3P1.show()
            self.hbox3.addWidget(self.strInput2P1)
            self.strInput2P1.show()
            self.hbox3.addWidget(self.strInput4P1)
            self.strInput4P1.show()
            self.hbox4.addWidget(self.strOutput10)
            self.strOutput10.show()
            self.hbox4.addWidget(self.but10)
            self.but10.show()
        elif p == 'НОД многочленов':
            self.hbox1.addWidget(self.P11)
            self.P11.show()
            self.hbox2.addWidget(self.strInput1P1)
            self.strInput1P1.show()
            self.hbox2.addWidget(self.strInput3P1)
            self.strInput3P1.show()
            self.hbox3.addWidget(self.strInput2P1)
            self.strInput2P1.show()
            self.hbox3.addWidget(self.strInput4P1)
            self.strInput4P1.show()
            self.hbox4.addWidget(self.strOutput11)
            self.strOutput11.show()
            self.hbox4.addWidget(self.but11)
            self.but11.show()
        elif p == 'Производная':
            self.hbox1.addWidget(self.P12)
            self.P12.show()
            self.hbox2.addWidget(self.strInput1P3)
            self.strInput1P3.show()
            self.hbox3.addWidget(self.strInput2P3)
            self.strInput2P3.show()
            self.hbox4.addWidget(self.strOutput12)
            self.strOutput12.show()
            self.hbox4.addWidget(self.but12)
            self.but12.show()
        else:
            self.hbox1.addWidget(self.P13)
            self.P13.show()
            self.hbox2.addWidget(self.strInput1P3)
            self.strInput1P3.show()
            self.hbox3.addWidget(self.strInput2P3)
            self.strInput2P3.show()
            self.hbox4.addWidget(self.strOutput13)
            self.strOutput13.show()
            self.hbox4.addWidget(self.but13)
            self.but13.show()

class About_app(QDialog):
    def __init__(self, parent = None):
        super(About_app, self).__init__(parent)

        self.about = QLabel('''Язык программирования: Python
Интерфейс: Создан на основе библиотеки pyqt
Ссылка на репозиторий: 
https://github.com/jst-liza/dm_2021_py
Архитектор: Елизавета Лоскутова (elizabeth.loskutova@gmail.com)
Ответственный за качество: Кирилл Рузов
Участники:
Марат Гарифуллин
Иван Носов
Евгений Погребицкий
Александр Вячин
Игорь Верхолин
Максим Семухин
Мария Клименко
Кирилл Солкин
Антон Артюхов
Семён Шлаев''')
        self.about.setWordWrap(True)
        
        
        self.butt_hide = QPushButton('Закрыть')
        self.butt_hide.clicked.connect(self.close)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.about)
        vbox.addWidget(self.butt_hide)
        
        self.setLayout(vbox)

        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("О программе")
        self.setFixedSize(560, 380)

class Appli(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

        self.setStyleSheet("""QWidget {color: white; background-color: #583F5A; font: 9pt bold sans-serif;}
                            QPushButton {background-color: #76537D; border: 2px solid rgb(203,203,203); border-radius: 10px; min-width: 100px; max-width: 100px; min-height: 25; max-height: 25px;}
                            QPushButton:pressed {background-color: white;}
                            QLineEdit {background-color: #76537D; border: 2px solid rgb(203,203,203); border-radius: 10px;}
                            QTabBar::tab:selected {background-color: #323232; }
                            QTabBar::tab:!selected {background-color: #76537D;}
                            QTabWidget::pane {border: 0px;}
                            QTabWidget::tab-bar {alignment: center;}
                            QComboBox {background-color: #76537D; border: 2px solid rgb(203,203,203); border-radius: 10px;}
                            QComboBox::drop-down {border-left-color: rgb(203,203,203);}
                            QComboBox QAbstractItemView {selection-background-color: #76537D;}
                            QComboBox QListView {border: none;}""")

    def initUI(self):

        self.aboutApp = QPushButton('Справка', self)
        self.aboutApp.clicked.connect(self.about_app)
        
        vbox = QVBoxLayout()
        vbox.addWidget(Natural_nums())
        vbox.addWidget(Integer_nums())
        vbox.addWidget(Rational_nums())
        vbox.addWidget(Polynomial())
        vbox.addWidget(self.aboutApp)

        self.setLayout(vbox)
        self.setWindowTitle('Коллоквиум по ДМ')
        self.setWindowIcon(QIcon('icon.png'))
        self.show()
        
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def about_app(self):
        abo = About_app(self)
        abo.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ap = Appli()
    ap.setFixedSize(1020, 800)
    sys.exit(app.exec_())
