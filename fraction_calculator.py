import math
def fraction_calculator(v):

    """Функция калькулятор с дробной частью"""
    """Дробная часть автоматически сокращается на возможное значение"""
    list_v = v.split('/')       #список с делимый и делителем
    chislo_1 = int(list_v[0])       #делимое
    chislo_2 = int(list_v[1])       #делитель

    try:                        #проверка деления на 0
        chislo_1/chislo_2
    except:
        print('На ноль делить нельзя!!!')

    math_ = math.modf(chislo_1/chislo_2)        #при помощи модуля "math" добываем целую часть от деления
    big_part = int(math_[1])        #вытаскием уже целочисленное значение в целую часть от деления
    if(math_[0] == 0.0):           #если без остатка,то сразу выводим значение
        return big_part
    small_part = chislo_1 - (chislo_2*big_part)         #высчитываем числитель остатка
    if(small_part<0):           #если пользователь забивал делимое как отрицательно, то числитель всегда положительное
        small_part *= -1

    max_delitel = 1             #максимальный общий делитель числителя и знаменателя
    for i in range(2,small_part): #цикл высчитывает max_delitel для числителя и знаменателя
        if ('.0' in str(small_part/i)) and ('.0' in str(chislo_2/i)):
            max_delitel = i
        else:
            continue

    small_part = small_part // max_delitel #выполняем сокращение
    chislo_2 = chislo_2 // max_delitel

    sring_complete = f'{big_part} {small_part}/{chislo_2}' #готовим итоговую строку вывода для пользователя
    return sring_complete

m = fraction_calculator('7/3')
print(m)

