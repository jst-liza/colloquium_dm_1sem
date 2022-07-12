# Модули: Q-1 -> Q-8
# Формат входных данных: [[числитель]; [знаменатель]]

import natural_nums
import integer_nums

def STR_TO_RAT(num,den):
    'Выполнил(а): Лоскутова Е.'
    mas = [integer_nums.STR_TO_INT(num), natural_nums.STR_TO_NAT(den)]
    return mas

def RAT_TO_NORMAL(mas):
    'Выполнил(а): Лоскутова Е.'
    return integer_nums.INT_TO_NORMAL(mas[0])+'/'+natural_nums.NAT_TO_NORMAL(mas[1])

def RED_Q_Q(num):#Сокращение дроби
    'Выполнил(а): Вячин А.'
    answer = []
    gcd = natural_nums.GCF_NN_N(integer_nums.ABS_Z_N(num[0]), num[1])#нахождение НОДа между числителем и знаменателем
    gcd.insert(0,0)#для корректной работы DIV_ZZ_Z определяем знак gcd как положительный
    num[1].insert(0,0)#аналогично со знаменателем
    answer.append(integer_nums.DIV_ZZ_Z(num[0], gcd))#добавляем элемент answer[0] = числитель, поделенный на НОД
    answer.append(integer_nums.DIV_ZZ_Z(num[1], gcd))#добавляем элемент answer[1] = знаменатель, поделенный на НОД
    answer[1].pop(0)#убираем "элемент знака" у знаменателя(из условия, знаменатель дроби - натуральное число)
    return answer#вывод массива пары чисел: числитель/знаменатель сокращенной дроби


def INT_Q_B(number):
    'Выполнил(а): Клименко М.'
    a = int(''.join((str(i) for i in number[0][2])))
    b = int(''.join((str(i) for i in number[1][1])))
    if a%b == 0:
        return 'да'
    else:
        return 'нет'


def TRANS_Z_Q(mas):
    'Выполнил(а): Вячин А.'
    mas_rational = []#массив для дроби
    mas_rational.append(mas)
    mas_rational.append([1, [1]])
    return mas_rational


def TRANS_Q_Z(mas):
    'Выполнил(а): Гарифулин М.'
    if mas[1][0] == 1:
        if mas[0][0] == 1:
            new_mas = [1, len(mas[0])-1, mas[0][2]]
        else:
            new_mas = [0, len(mas[0])-1, mas[0][2]]
        return new_mas
    else:
        return [0, 0, 'Знаменатель отличен от 1']


def ADD_QQ_Q(frac1, frac2):
    "Выполнил: Погребицкий"
    #[[sign,n,[num]],[n,[num]]]
    den = natural_nums.LCM_NN_N([frac1[1][0],frac1[1][1]],[frac2[1][0],frac2[1][1]]) #знаменатель равен НОК знаменталей
    #числитель = числ1*(знам_общ/знам1)+числ2*(знам_общ/знам2)=
    # =frac1[0]*(НОК/frac2[1])+frac2[0]*(НОК/frac1[1])
    dopmn1 = natural_nums.DIV_NN_N([den[0], den[1]], [frac1[1][0],frac1[1][1]]) #доп. множитель для 1 дроби
    dopmn2 = natural_nums.DIV_NN_N([den[0], den[1]], [frac2[1][0],frac2[1][1]]) #доп. множитель для 2 дроби
    new_num1 = integer_nums.MUL_ZZ_Z([frac1[0][0], frac1[0][1], frac1[0][2]], [0, dopmn1[0], dopmn1[1]]) #новый числ 1 дроби
    new_num2 = integer_nums.MUL_ZZ_Z([frac2[0][0], frac2[0][1], frac2[0][2]], [0, dopmn2[0], dopmn2[1]]) #новый числ 2 дроби
    num = integer_nums.ADD_ZZ_Z([new_num1[0], new_num1[1], new_num1[2]], [new_num2[0], new_num2[1], new_num2[2]]) #сумма 2-ух числителей
    #получаем НЕСОКРАЩЕННУЮ дробь [[числ],[знам]]
    ans=[num,den]
    return(ans)



def SUB_QQ_Q(num1, num2):  # num1 - уменьшаемое, num2 - вычитаемое
    'Выполнил(а): Верхолин И.'
    lcm = natural_nums.LCM_NN_N(num1[1], num2[1])  # НОК знаменателей
    mult1 = natural_nums.DIV_NN_N(lcm, num1[1])  # Множитель числителя первой дроби
    mult2 = natural_nums.DIV_NN_N(lcm, num2[1])  # Множитель числителя второй дроби
    return [integer_nums.SUB_ZZ_Z(integer_nums.MUL_ZZ_Z(num1[0], integer_nums.TRANS_N_Z(mult1)), integer_nums.MUL_ZZ_Z(num2[0], integer_nums.TRANS_N_Z(mult2))), lcm]


def MUL_QQ_Q(num1, num2): #умножение дробей (исп. MUL_NN_N т.к. знаменатель - натуральное)
    'Выполнил(а): Верхолин И.'
    return [integer_nums.MUL_ZZ_Z(num1[0], num2[0]), natural_nums.MUL_NN_N(num1[1], num2[1])]


def DIV_QQ_Q(num1,num2):
    "Выполнил: Артюхов"
    num1[1] = integer_nums.TRANS_N_Z(num1[1]) ## Знаменатель приводим в вид целого  числа
    num2[1] = integer_nums.TRANS_N_Z(num2[1]) ## Знаменатель приводим в вид целого  числа
    if ((num1[0][0]== 1) and (num2[0][0]==1)): ## Если в числителях минус ставим в них плюс
        num1[0][0] = 0
        num2[0][0] = 0
    elif ((num1[0][0] == 1) or (num2[0][0] == 1)):
        ## Если только один из числителей отрицателен делаем первый отрицательным а второй положительным
        num1[0][0] = 1
        num2[0][0] = 0
    num3 = (integer_nums.MUL_ZZ_Z(num1[1], num2[0]))
    integer_nums.TRANS_Z_N(num3) ##целое число приводим к виду натурального
    return [integer_nums.MUL_ZZ_Z(num1[0], num2[1]), num3]
