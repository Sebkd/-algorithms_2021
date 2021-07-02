"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым
"""
from timeit import timeit
from random import randint

array = [randint (10, 20) for element in range (15)]


def func_1():
    '''Функция перебора циклом'''
    m_count = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m_count:
            m_count = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m_count} раз(а)'


def func_2():
    '''Функция перебора максимума вхождения через новый список'''
    new_array = []
    for elem in array:
        count2 = array.count(elem)
        new_array.append(count2)
    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

def func_3():
    '''Функция перебора максимума в массиве через ключ функции max'''
    maximum = max(array, key = array.count)
    return f'Чаще всего встречается число {maximum}, ' \
           f'оно появилось в массиве {array.count(maximum)} раз(а)'

print(array)
print(func_1())
print(func_2())
print(func_3())
print (timeit ("func_1()", globals = globals ()))
print (timeit ("func_2()", globals = globals ()))
print (timeit ("func_3()", globals = globals ()))
'''
Быстрее работает func_1: функция берет каждый элемент и проверяет на количество его
вхождений в массив, массив переберется один раз и подбирается тот элемент массива,
количество вхождений которого в массивы максимально. Очень быстрый способ.
Второй способ странный, в нем формируется массив 2, который состоит из количества
вхождений элементов первого массива, потом выбирается максимальное значение, определяется
первый индекс этого максимума в массиве 2, который также является индексом первого
входного массива. Итого за счет создания и сортировки нового списка, получается замедление
по времени. Переборка списка, связана с его длиной O(len), поэтому третий способ может как
быстрее, так и медленнее. Так при малом количестве длине списка, третий способ дольше работает
чем первый, а при большой длине работает быстрее.

[19, 14, 11, 15, 19, 14, 15, 19, 18, 14, 14, 20, 17, 18, 14, 17, 17, 10,
 12, 16, 19, 14, 11, 11, 18, 13, 10, 19, 11, 12]
Чаще всего встречается число 14, оно появилось в массиве 6 раз(а)
Чаще всего встречается число 14, оно появилось в массиве 6 раз(а)
Чаще всего встречается число 14, оно появилось в массиве 6 раз(а)
9.365097400000002
10.293694200000001
8.9896593
'''
