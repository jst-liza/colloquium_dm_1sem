# Модули: P-1 -> P-13
# Формат входных данных: [степень многочлена; [коэффициенты]]

import rational_nums
import integer_nums
import natural_nums
import copy

def STR_TO_POL(grade, coefs):
    'Выполнил(а): Лоскутова Е.'
    mas = [0, []]
    mas[0] = grade
    coefs = coefs.split(';')
    for i in range(grade + 1):
        coef_i = coefs[i].split('/')
        mas[1].append([integer_nums.STR_TO_INT(coef_i[0]), natural_nums.STR_TO_NAT(coef_i[1])])
    return mas


def POL_TO_NORMAL(pol):
    'Выполнил(а): Солкин К.'
    ans = ''
    for i in range(pol[0] + 1):
        rat = rational_nums.RAT_TO_NORMAL(pol[1][i])
        if rat[0] != '-':
            rat = '+' + rat
        ans = ans + rat + '*x^' + str(pol[0] - i)
    if ans[0] == '+':
        ans = ans[1:]
    return ans


def ADD_PP_P(sumnd1, sumnd2):#1е слагаемое и 2е слагаемое
    'Выполнил(а): Вячин А.'
    if(sumnd1[0] > sumnd2[0]):#выбор многочлена с бОльшей степенью как 1е слагаемое
        sum = sumnd1#многочлен с бОльшей степенью
        sum2 = sumnd2#2й многочлен
    else:
        sum = sumnd2
        sum2 = sumnd1
    sum[1] = sum[1][::-1]
    sum2[1] = sum2[1][::-1]#переворачиваем массив многочлена для удобства счeта
    for i in range(sum2[0]+1):#сложение одночленов начиная с конца многочлена с меньшей степенью
        sum[1][i] = rational_nums.ADD_QQ_Q(sum[1][i], sum2[1][i])
    sum[1] = sum[1][::-1]#переворачиваем многочлен обратно
    return(sum)


def SUB_PP_P(minuend, subtrahend):
    'Выполнил(а): Клименко М.'
    mm = minuend[0]
    sm = subtrahend[0]
    result = [sm, []]
    if (sm > mm):
        minuend[0] = sm
        for i in range(sm-mm):
            minuend[1].insert(0, [0, 0, [0]])
    for i in range(sm):
        result[1].append(rational_nums.SUB_QQ_Q(minuend[1][i], subtrahend[1][i]))
    return result


def MUL_PQ_P(mult, polynomial):
    'Выполнил(а): Клименко М.'
    m = polynomial[0]
    for i in range (m+1): #умножаем каждый коэффициент на рациональное число
        polynomial[1][i] = rational_nums.MUL_QQ_Q(polynomial[1][i], mult)


def MUL_Pxk_P(pol, k):#множители:массив и степень x^k
    'Выполнил(а): Вячин А.'
    for i in range(k):
        pol[1].append([[[0, 1, [0]], [1, [1]]]])#добавляем k нулей
    pol[0] = pol[0] + k - 1 #прибавляем к степени полинома k
    return(pol)


def LED_P_Q(mas):
    'Выполнил(а): Семухин М.'
    return mas[1][0]


def DEG_P_N(polynom):
    'Выполнил(а): Верхолин И.'
    return polynom[0]


def FAC_P_Q (mas):
    "Выполнил(а): Артюхов А."
    t = mas[0] ## переменная для хранения количества чисел в массиве
    for j in range(t+1, 0, -1):
        mas[1][j-1][0] = integer_nums.ABS_Z_N(mas[1][j-1][0])  ## Приводим числители к виду натуральных числел
    mas_nod = natural_nums.GCF_NN_N(mas[1][t][0], mas[1][t-1][0])  ## Находим НОД предпоследнего и последнего элементов
    mas_nok = natural_nums.LCM_NN_N(mas[1][t][1], mas[1][t-1][1]) ## Находим НОК предпоследнего и последнего элементов
    for j in range(t, 0, -1):
        mas_nod = natural_nums.GCF_NN_N(mas_nod, mas[1][j-1][0])##Продолжаем искать НОД
        mas_nok = natural_nums.LCM_NN_N(mas_nok, mas[1][j-1][1])##Продолжаем искать НОК
    result = [mas_nod, mas_nok]
    return result


def MUL_PP_P(pol1, pol2):
    'Выполнил(а): Солкин К.'
    answer = STR_TO_POL(0, '0/1') #создаем полином-ответ
    for i in range(pol1[0] + 1):#Проходимся по всем стпеням 1-ого полинома
        mult = copy.deepcopy(pol2) #копируем 2-ой полином
        mult = MUL_PQ_P(pol1[1][i], mult)#умножаем полином на коэффициент при x^i
        mult = MUL_Pxk_P(mult, pol1[0] - i)#умножаем полином на x^i
        answer = ADD_PP_P(answer, mult)#прибавляем полином к полиному-ответу
    return(answer)


def DIV_PP_P(pol1, pol2):#делимое и делитель
    'Выполнил(а): Солкин К.'
    answer = [0, [[[0, 1, [0]], [1, [1]]]]]#полином-слагаемое для ответа
    while(pol1[0] >= pol2[0]):#пока старшая степень делимого больше или равна старшей степени делителя
        sub = []#полином-вычитаемое из делимого
        sub.append(pol1[0]-pol2[0])#степень полинома sub равна разности степеней pol1 и pol2
        sub.append([])
        sub[1].append(rational_nums.DIV_QQ_Q(pol1[1][0], pol2[1][0]))#коэф перед одночленом полинома sub равна частному от коэфов делимого и делителя
        for i in range(sub[0]):#все коэфы одночленам со степенью меньше sub[0] равны нулю
            sub[1].append([[0, 1, [0]], [1, [1]]])#
        answer = polynomial.ADD_PP_P(sub, answer)#сложить sub  полиномом-ответом
        pol1 = polynomial.SUB_PP_P(pol1, polynomial.MUL_PP_P(sub, pol2))#вычитание из делимого делителя, умноженного на sub
    return(answer)#вывод частного от деления


def MOD_PP_P(pol1, pol2):#полином-частное умножается на полином-делителль и вычитается из полинома-делимого
    return(polynomial.SUB_PP_P(pol1, polynomial.MUL_PP_P(polynomial.DIV_PP_P(pol1, pol2), pol2)))


def GCF_PP_P(pol1, pol2):
    'Выполнил(а): Вячин А.'
    divid = pol1#Делимое
    divis = pol2#Делитель
    while(divis[1][0][0][2][0] != 0):#Проверка, равен ли делитель нулю
        bubble = divis#Метод пузырька
        divis = polynomial.MOD_PP_P(divid, divis)#Делим полиномы и принимаем делитель за делимое, а остаток за делитель
        divid = bubble
    return(divid)#последнее делимое перед остатком ноль - НОД полиномов


def DER_P_P(mas):
    'Выполнил(а): Солкин К.'
    for i in range(mas[0]):
        b = mas[0] - i
        b = integer_nums.STR_TO_INT(str(b))
        print(b)
        mas[1][i] = rational_nums.MUL_QQ_Q(mas[1][i], rational_nums.TRANS_Z_Q(b))
    mas[0] -= 1
    mas[1].pop()
    return mas


##NMR_P_P
