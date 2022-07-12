# Модули: N-1 -> N-14
##Формат входных данных: [количество разрядов; [число]]

def STR_TO_NAT(num):
    'Выполнил(а): Лоскутова Е.'
    mas = [len(num), [int(i) for i in (num)]]
    return mas

def NAT_TO_NORMAL(mas):
    'Выполнил(а): Лоскутова Е.'
    return ''.join([str(i) for i in (mas[1])])


def COM_NN_D(mas1, mas2):
    'Выполнил: Погребицкий Е.'
    if mas1[0] > mas2[0]:   #если в 1-ом числе разрядов больше, то оно больше 2-ого числа
        return 2
    if mas1[0] < mas2[0]:   #если в 1-ом числе разрядов меньше, то оно меньше 2-ого числа
        return 1
    if mas1[0] == mas2[0]:
        n = mas1[0]
        for i in range(n):
            if mas1[1][i] > mas2[1][i]:
                return 2
            if mas1[1][i] < mas2[1][i]:
                return 1
        return 0    #если весь цикл прошел, и функция не вернула значения, то числа равны и мы возвращаем 0


def NZER_N_B(mas):
    'Выполнил: Гарифулин'
    check = True    #Возвращаемое значение функции
    if mas[1][0] == 0:
        check = False
    return check


def ADD_1N_N(mas):
    'Выполнил: Семухин'
    if mas[1][-1] < 9:                             #если последняя цифра числа < 9, то
        mas[1][-1] = mas[1][-1] + 1                #последняя цифра +1

    else:                                          #если последняя цифра = 9, то
        c = mas[0]                                 #запоминаем кол-во разрядов числа в переменной c
        i = 1
        while (c > 1) and (mas[1][-i] == 9):       #пока кол-во разрядов макссива > 1 и текущее цифра = 9
            mas[1][-i] = 0
            c -= 1
            i += 1
            p = i                                  #запоминаем индекс цифры, на которой остановились
        mas[1][-p] = mas[1][-p] + 1                #прибавляем к ней 1
        if mas[1][0] == 10:                        #при переполнении
            mas[1].insert(0, 1)                    #если первый эл-т массива = 10, то создаём на первом месте в массиве новый эл-т,
            mas[1][1] = 0                          #равный 1, а эл-т равный 10 обнуляем
            mas[0] = mas[0] + 1                    #увеличиваем кол-во разрядов на 1
    return(mas)


def ADD_NN_N(mas1, mas2):
    'Выполнил: Носов'
    n=0
    s=[]
    if mas1[0] == mas2[0]:                          #если кол-во разрядов одинаковое, то на всякий случай
        s = [mas1[0], [0] * (mas1[0] + 1)]          #cоздаем массив на 1 эл-нт больше максимального
        for i in range(-1, -(mas1[0] + 1), -1):
            s[1][i] = mas1[1][i] + mas2[1][i]       #складываем эл-ты по разрядно
        n = mas1[0]
    elif COM_NN_D(mas1, mas2) == 2:
        s = [mas1[0], [0] * (mas1[0]+1)]
        for j in range(-mas1[0], -mas2[0]):         #элементы, которые не меняются сохраняем
            s[1][j] = mas1[1][j]
        for i in range(-1, -(mas2[0]+1), -1):
            s[1][i] = mas1[1][i]+mas2[1][i]         #складываем эл-ты по разрядно
        n = mas1[0]
    elif COM_NN_D(mas1, mas2) == 1:
        s = [mas2[0], [0] * (mas2[0] + 1)]
        for j in range(-mas2[0], -mas1[0]):         #элементы, которые не меняются сохраняем
            s[1][j] = mas2[1][j]
        for i in range(-1, -(mas1[0] + 1), -1):
            s[1][i] = mas1[1][i] + mas2[1][i]       #складываем эл-ты по разрядно
        n = mas2[0]

    for j in range(-1, -(n + 1), -1):                #проверяем если эл-ты массива >10 и приводим число к нормальному виду
        if s[1][j] >= 10:
            s[1][j] = s[1][j] - 10
            s[1][j - 1] = s[1][j - 1] + 1

    if s[1][0] == 0:                                #если лишний разряд не понадобился, то перезаписываем
        d = [n, [0] * n]
        for i in range(n):
            d[1][i] = s[1][i+1]
        s = d
    else:
        s[0] += 1
    return s


def SUB_NN_N(mas1, mas2):
    'Выполнил: Носов'
    if COM_NN_D(mas1, mas2) == 2 or COM_NN_D(mas1, mas2) == 0:    #сравниваем два числа, чтобы 1ое было >= 2го
        sum_e = 0
        s = [mas1[0], [0] * (mas1[0])]
        for i in range(-1, -(mas2[0]+1), -1):
            if mas1[1][i] < mas2[1][i]:                         #если цифра в разряде 1го числа меньше цифры 2го, то делаем что и при обычном вычитании
                mas1[1][i] += 10
                mas1[1][i-1] -= 1
            s[1][i] = mas1[1][i]-mas2[1][i]
            if mas1[1][i] >= 10:
                mas1[1][i] -= 10
        for j in range(-mas1[0], -mas2[0]):                     #сохраняем не использованные цифры
            s[1][j] = mas1[1][j]
        i = 0
        r = [mas1[0], [0] * mas1[0]]                            #создаем рез-ий массив, в котором будем избавляться от 0
        while (s[1][i] == 0) and (i < mas1[0]-1):
            r[1] = s[1][i+1:]
            i += 1
        for k in range(mas1[0]):                                #считаем сумму эл-ов, важна только если все 0
            sum_e += s[1][k]
        r[0] = mas1[0] - i                                      #считаем кол-во разрядов нового числа
        if sum_e == 0:
            r[1] = s[1][0:1]
            s = r
        elif r[1][0] != 0:
            s = r
        return s


def MUL_ND_N(multiplier, number): # Умножение числа number на цифру multiplier(0-10)
    'Выполнил: Верхолин'
    if multiplier == 0:           # Если множитель равен нулю 
        number[:] = [0, [0]]
    elif 10 > multiplier > 0:
        overflow = number[1][len(number[1]) - 1] * multiplier // 10  # Переменная, хранящее перполнение разряда (для прибавления к следующему разряду)
        number[1][len(number[1]) - 1] = number[1][len(number[1]) - 1] * multiplier % 10
        for i in range(len(number[1]) - 2, -1, -1):
            tmp = number[1][i]                                      # Буфер, хранящий изначальное значение разярда для вычисления overflow после умножения 
            number[1][i] = (number[1][i] * multiplier + overflow) % 10  
            overflow = (tmp * multiplier + overflow) // 10
        if overflow > 0:                    # Если переполнен самый старший разряд исходного числа, создаём новый со значением overflow 
            number[1].insert(0, overflow)
            number[0] += 1


def MUL_Nk_N (number, deg): #number - число, deg - степень
    'Выполнила: Клименко'
    if deg > 0:
        number[0] += deg
        for i in range (deg):
            number[1].append(0)
    elif deg < 0:
        return [0, "Неверное значение степени"]


def MUL_NN_N(a, b): #a и b - множители
    'Выполнила: Клименко'
    s = [1, [0]]
    c = [1, [0]]
    for i in range(0, len(b[1])):
        c[0] = a[0]
        c[1] = a[1].copy()
        MUL_ND_N(b[1][len(b[1])-1-i], c)
        MUL_Nk_N(c, i)
        s = ADD_NN_N(s, c)
    return s


def SUB_NDN_N(num1, num2, mult):  # ВЫчитаение из num1(уменьшаемое) num2(вычитаемое) умноженного на mult, для неотрицательного результата
    'Выполнил: Верхолин'
    MUL_ND_N(mult, num2)
    if COM_NN_D(num1, num2) == 2 or COM_NN_D(num1, num2) == 0:  # Вычитаем только если уменьшаемое не меньше домноженного вычитаемого
        return SUB_NN_N(num1, num2)
    else:
        return [0, 'Отрицательный результат']


def DIV_NN_Dk(mas1, mas2): #Вычисление первой цифры деления большего натурального на меньшее,
    'Выполнил: Вячин'
                           #домноженное на 10^k,где k - номер позиции этой цифры (номер считается с нуля)
    num1 = 0          #переменная для "сборки числа" из mas1
    num2 = 0          #переменная для "сборки числа" из mas2
    count = 0         #переменная для подсчета номера
    result = [0,[]] #переменная для результата выполнения функции
    for i in range(mas1[0]):
        num1 = num1 + mas1[1][i] * (10 ** (mas1[0] - i - 1))
    for i in range(mas2[0]):
        num2 = num2 + mas2[1][i] * (10 ** (mas2[0] - i - 1)) #сборка num1 и num2 из массивов mas1 и mas2
    if COM_NN_D(mas1, mas2) == 1: #если num2 > num1
        quot = num2 // num1
        while quot//10 != 0:
            count += 1
            quot = quot // 10     #деление num2 на num1, вычисление первой цифры и ее номера
    else:                         #если num2 <= num1
        quot = num1 // num2
        while quot//10 != 0:
            count += 1
            quot = quot // 10     #деление num1 на num2, вычисление первой цифры и ее номера
    result[1].append(quot)        #массиву result присваивание вычисленной цифры
    MUL_Nk_N (result, count)      #умножение цифры на 10^(номер цифры)
    return(result) #вывод массива по шаблону (n; A[..]) - номер старшей позиции


def DIV_NN_N(mas1, mas2):
    'Выполнил: Носов'
    num1 = 0
    num2 = 0
    count = 0
    result = [1, []]
    for i in range(mas1[0]):
        num1 = num1 + mas1[1][i] * (10 ** (mas1[0] - i - 1))
    for i in range(mas2[0]):
        num2 = num2 + mas2[1][i] * (10 ** (mas2[0] - i - 1)) #тут код Сани, вообще без изменений, см. его комы
    if COM_NN_D(mas1, mas2) == 1:
        quot = num2 // num1
        k = -1
        ost = quot % 10                                      #сэйвим последнию цифру числа, т.к она не попадет в цикл
        while quot // 10 != 0:
            count += 1
            quot = quot // 10
            if quot < 10:                                    #если наша целая часть > 10, то добавляем остаток этого числа в конец массива
                result[1].insert(k, quot)
                k -= 1
            else:
                result[1].insert(k, quot % 10)
                k -= 1
        result[1].append(ost)
        result[0] = count + 1
    else:
        quot = num1 // num2
        k = -1
        ost = quot % 10                                     #сэйвим последнию цифру числа, т.к она не попадет в цикл
        while quot // 10 != 0:
            count += 1
            quot = quot // 10
            if quot < 10:                                   #если наша целая часть > 10, то добавляем остаток этого числа в конец массива
                result[1].insert(k, quot)
                k -= 1
            else:
                result[1].insert(k, quot % 10)
                k -= 1
        result[1].append(ost)
        result[0] = count + 1                               #т.к count не учитывает наш последний разряд, то увеличиваем его на 1
    return result



def MOD_NN_N(mas1, mas2):                                               #происходит все тоже самое что и в DIV_NN_N, кроме
    'Выполнил: Носов'
    num1 = 0
    num2 = 0
    count = 0
    result = [1, []]
    for i in range(mas1[0]):
        num1 = num1 + mas1[1][i] * (10 ** (mas1[0] - i - 1))
    for i in range(mas2[0]):
        num2 = num2 + mas2[1][i] * (10 ** (mas2[0] - i - 1))
    if COM_NN_D(mas1, mas2) == 1:
        quot = num2 % num1                                              #считаем остаток, а не целую часть, алгоритм точно такой же
        k = -1
        ost = quot % 10                                                 #сэйвим последнию цифру числа, т.к она не попадет в цикл
        while quot // 10 != 0:
            count += 1
            quot = quot // 10   
            if quot < 10:                                               #если наша целая часть > 10, то добавляем остаток этого числа в конец массива
                result[1].insert(k, quot)
                k -= 1
            else:
                result[1].insert(k, quot % 10)
                k -= 1
        result[1].append(ost)
        result[0] = count + 1
    else:
        quot = num1 % num2                                              #считаем остаток, а не целую часть, алгоритм точно такой же
        k = -1
        ost = quot % 10                                                 #сэйвим последнию цифру числа, т.к она не попадет в цикл                                                
        while quot // 10 != 0:
            count += 1
            quot = quot // 10
            if quot < 10:                                               #если наша целая часть > 10, то добавляем остаток этого числа в конец массива
                result[1].insert(k, quot)
                k -= 1
            else:
                result[1].insert(k, quot % 10)
                k -= 1
        result[1].append(ost)
        result[0] = count + 1                                           #т.к count не учитывает наш последний разряд, то увеличиваем его на 1
    return result


def GCF_NN_N(mas1, mas2):                                                   #алгоритм Евклида для поиска НОД
    'Выполнил: Шлаев'
    while NZER_N_B(mas1) == True and NZER_N_B(mas2) == True:
        if COM_NN_D(mas1, mas2) == 2:
            mas1 = MOD_NN_N(mas1, mas2)
        else:
            mas2 = MOD_NN_N(mas2, mas1)
    return ADD_NN_N(mas1, mas2)

def LCM_NN_N(mas1, mas2):
    'Выполнил: Гарифулин'
    mas_GCF = GCF_NN_N(mas1, mas2) #Вычисляем нод чисел
    mas_div1 = DIV_NN_N(mas1, mas_GCF) #Вычисляем частное от деления первого числа на НОД
    mas_div2 = DIV_NN_N(mas2, mas_GCF) #Вычисляем частное от деления второго числа на НОД
    return MUL_NN_N(mas_GCF, MUL_NN_N(mas_div1, mas_div2)) #Перемножаем НОД с двумя частными
