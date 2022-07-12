# Модули: Z-1 -> Z-10
# Формат входных данных: [знак числа(1 - отрицательное, 0 - положительное), количество разрядов; [число]]

import natural_nums

def STR_TO_INT(num):
    'Выполнил(а): Лоскутова Е.'
    if num[0] == '-':
        mas=[1, len(num)-1, [int(i) for i in (num[1::])]]
    else:
        mas=[0, len(num), [int(i) for i in (num)]]
    return mas

def INT_TO_NORMAL(mas):
    'Выполнил(а): Лоскутова Е.'
    if mas[0] == 1:
        return '-'+''.join([str(i) for i in (mas[2])])
    else:
        return ''.join([str(i) for i in (mas[2])])


def ABS_Z_N(mas1):
    'Выполнил(а): Носов И.'
    mas1 = mas1[1:]     #берем просто все кроме 1ой цифры
    return mas1


def POZ_Z_D(mas):
    'Выполнил(а): Погребицкий Е.'
    #проверим не равно ли 0 число
    if mas[2][0] == 0:
        return 0
    #если число не ноль, то смотрим на знак
    if mas[0] == 0: #знак +
        return 2
    if mas[0] == 1: #знак -
        return 1


def MUL_ZM_Z(mas):
    'Выполнил(а): Семухин М.'
    if mas[0] == 1:      #если знак -
        mas[0] = 0       #меняем на +
    else:                #если знак +
        mas[0] = 1       #меняем на -
    return mas


def TRANS_N_Z(mas):
    'Выполнил(а): Гарифулин М.'
    ##На вход подаётся массив вида [n, A[...]],
    mas = [0]+mas   ##Возвращает массив вида [b, n, A[...]], где b - знак числа,
    return mas      ##записанного в массиве A[...]


def TRANS_Z_N (number):
    'Выполнил(а): Клименко М.'
    if (number[0] == 0):
        number.pop(0)
        return number
    else:
        return [0,'Ошибка! Задано отрицательное число']


def ADD_ZZ_Z(mas1, mas2): #Сложение целых чисел
    'Выполнил(а) Вячин А.:'
    if POZ_Z_D(mas1) == 2 and POZ_Z_D(mas2) == 2:           #если оба числа положительны, складываем их модули, добавляем значение знака 0
        result = natural_nums.ADD_NN_N(ABS_Z_N(mas1),ABS_Z_N(mas2))
        result.insert(0,0)
    elif POZ_Z_D(mas1) == 1 and POZ_Z_D(mas2) == 1:         #если оба числа отрицательны, складываем их модули, добавляем значение знака 1
        result = natural_nums.ADD_NN_N(ABS_Z_N(mas1),ABS_Z_N(mas2))
        result.insert(0,1)
    elif natural_nums.COM_NN_D(ABS_Z_N(mas1), ABS_Z_N(mas2)) == 0:       #если числа одинаковы по модулю и имею разные знаки, вывод 0
        result = [0, 0, [0]]
    elif POZ_Z_D(mas1) == 1 and POZ_Z_D(mas2) == 2:         #если 1е отрицательное, 2е положительное
        if natural_nums.COM_NN_D(ABS_Z_N(mas1), ABS_Z_N(mas2)) == 2:         #1e по модулю больше, добавляем значение знака 1
            result = natural_nums.SUB_NN_N(ABS_Z_N(mas1),ABS_Z_N(mas2))
            result.insert(0,1)
        else:
            result = natural_nums.SUB_NN_N(ABS_Z_N(mas2),ABS_Z_N(mas1))      #2e по модулю больше, добавляем значение знака 0
            result.insert(0,0)
    elif POZ_Z_D(mas1) == 2 and POZ_Z_D(mas2) == 1:
        if natural_nums.COM_NN_D(ABS_Z_N(mas1), ABS_Z_N(mas2)) == 2:     #если 2е отрицательное, 1е положительное
            result = natural_nums.SUB_NN_N(ABS_Z_N(mas1),ABS_Z_N(mas2))      #2e по модулю больше, добавляем значение знака 1
            result.insert(0,0)
        else:
            result = natural_nums.SUB_NN_N(ABS_Z_N(mas2),ABS_Z_N(mas1))      #1e по модулю больше, добавляем значение знака 0
            result.insert(0,1)
    elif POZ_Z_D(mas1) == 0:                                #1е число равно 0, значит присваиваем result 2е число
        result = mas2
    else:                                                   #2е число равно 0, значит присваиваем result 1е число
        result = mas1
    return(result)  #вывод массива по шаблону (b, n; A[..]) - номер старшей позиции


def SUB_ZZ_Z(num1, num2): #num1 - уменьшаемое, num2 - вычитаемое
    'Выполнил: Верхолин И.'
    if natural_nums.COM_NN_D(ABS_Z_N(num1), ABS_Z_N(num2)) == 2: #Вычитаемое меньше уменьшаемого
        if POZ_Z_D(num1) == 2:
            if POZ_Z_D(num2) == 2:  # Оба числа положительные
                return [0, *natural_nums.SUB_NN_N(TRANS_Z_N(num1), TRANS_Z_N(num2))] # возвращаем разность уменьшаемого и вычитаемого
            else:                   # Вычитаемое отрицательные 
                return [0, *natural_nums.ADD_NN_N(TRANS_Z_N(num1), ABS_Z_N(num2))] # возвращаем сумму  
        else:
            if POZ_Z_D(num2) == 2: # Уменьшаемое отрицательно 
                return[1, *natural_nums.ADD_NN_N(ABS_Z_N(num1), TRANS_Z_N(num2))] # Возвращаем сумму абсолютномых значений с минусом
            else:                  # Оба числа отрицатльные 
                return[1, *natural_nums.SUB_NN_N(ABS_Z_N(num1), ABS_Z_N(num2))] # Возвращаем разность абсолютных значений 
                                                                                # уменьшаемого и вычитаемого с минусом 
    else:                          # Вычитаемое больше уменьшаемого
        if POZ_Z_D(num2) == 2:     
            if POZ_Z_D(num1) == 2: # Оба числа положительные 
                return [1, *natural_nums.SUB_NN_N(TRANS_Z_N(num2), TRANS_Z_N(num1))] # Возвращаем разность вычитаемого и уменьшаемого с минусом
            else:                  # уменьшаемое отрицательное 
                return [1, *natural_nums.ADD_NN_N(TRANS_Z_N(num2), ABS_Z_N(num1))] # Возвращаем сумму абсолютных значений с минусом
        else:
            if POZ_Z_D(num1) == 2: # Вычитаемое отрицательно
                return [0, *natural_nums.ADD_NN_N(ABS_Z_N(num2), TRANS_Z_N(num1))] # Возвращаем сумму абсолютных значений
            else:                  #
                return [0, *natural_nums.SUB_NN_N(ABS_Z_N(num2), ABS_Z_N(num1))] # Возвращаем разность вычитаемого и уменьшаемого


def MUL_ZZ_Z(num1, num2): #num1, num2 - множители
    'Выполнил: Верхолин И.'
    if POZ_Z_D(num1) == POZ_Z_D(num2):  # Числа имеют одинаковый знак
        return [0, *natural_nums.MUL_NN_N(ABS_Z_N(num1), ABS_Z_N(num2))] #  Возвращаем положительное произведение
    else:                               # Числа противоположны по знаку
        return [1, *natural_nums.MUL_NN_N(ABS_Z_N(num1), ABS_Z_N(num2))] # Возвращаем отрицательное произведение 


def DIV_ZZ_Z(mas1, mas2):
    'Выполнил(а): Шлаев С.'
    if natural_nums.COM_NN_D(ABS_Z_N(mas1), ABS_Z_N(mas2)) == 2:                    #если первое по модулю больше второго
        if POZ_Z_D(mas1) == 1:                                                      #если первое отрицательное
            if POZ_Z_D(mas2) == 1:                                                  #если второе отрицательное
                if natural_nums.MOD_NN_N(ABS_Z_N(mas1), ABS_Z_N(mas2)) == [1, [0]]:
                    return [0, *natural_nums.DIV_NN_N(ABS_Z_N(mas1), ABS_Z_N(mas2))]
                else:
                    return [0, *natural_nums.ADD_1N_N(natural_nums.DIV_NN_N(ABS_Z_N(mas1), ABS_Z_N(mas2)))]    
            elif POZ_Z_D(mas2) == 2:                                                #если второе положительное
                if natural_nums.MOD_NN_N(ABS_Z_N(mas1), ABS_Z_N(mas2)) == [1, [0]]: 
                    return [1, *natural_nums.DIV_NN_N(ABS_Z_N(mas1), ABS_Z_N(mas2))]
                else:
                    return [1, *natural_nums.ADD_1N_N(natural_nums.DIV_NN_N(ABS_Z_N(mas1), ABS_Z_N(mas2)))]
        elif POZ_Z_D(mas1) == 2:                                                    #если первое положительное
            if POZ_Z_D(mas2) == 2:                                                  #если второе положительное
                return [0, *natural_nums.DIV_NN_N(ABS_Z_N(mas1), ABS_Z_N(mas2))]
            elif POZ_Z_D(mas2) == 1:                                                #если второе отрицательное
                return [1, *natural_nums.DIV_NN_N(ABS_Z_N(mas1), ABS_Z_N(mas2))]
    elif natural_nums.COM_NN_D(ABS_Z_N(mas1), ABS_Z_N(mas2)) == 1:                  #если первое по модулю меньше второго
        if POZ_Z_D(mas1) == 1:                                                      #если первое отрицательное
            if POZ_Z_D(mas2) == 1:                                                  #если второе отрицательное
                return [0, 1, [1]]
            elif POZ_Z_D(mas2) == 2:                                                #если второе положительное
                return [1, 1, [1]]
        elif POZ_Z_D(mas1) == 2:                                                    #если первое положительное
            if POZ_Z_D(mas2) == 2:                                                  #если второе положительное
                return [0, 1, [0]]
            elif POZ_Z_D(mas2) == 1:                                                #если второе отрицательное
                return [0, 1, [0]]
        elif POZ_Z_D(mas1) == 0:                                                    #если первое = 0
            return [0, 1, [0]]
    elif natural_nums.COM_NN_D(ABS_Z_N(mas1), ABS_Z_N(mas2)) == 0:                  #если числа равны
        if POZ_Z_D(mas1) == 1 and POZ_Z_D(mas2) == 2:                               #если первое отрицательное и второе положительное
            return [1, 1, [1]]
        elif POZ_Z_D(mas1) == 2 and POZ_Z_D(mas2) == 1:                             #если первое положительное и второе отрицательное
            return [1, 1, [1]]
        else:
            return [0, 1, [1]]


def MOD_ZZ_Z(mas1,mas2):
    'Выполнил(а): Шлаев С.'
    divz = DIV_ZZ_Z(mas1, mas2)         #неполное частное
    mulz = MUL_ZZ_Z(divz, mas2)         #произведение неполного частного на делитель
    ost = SUB_ZZ_Z(mas1, mulz)          #разность делимого и произведения неполного частного на делитель r = a-b*q
    return ost                          #остаток от деления
