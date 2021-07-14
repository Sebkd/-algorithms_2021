"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1

Предприятия, с прибылью ниже среднего значения: Фирма_2
"""

from collections import namedtuple
from functools import reduce

if __name__ == '__main__':
    list_firms = []
    FIRMS = namedtuple('Firm', 'id name_firm annual_profit')
    numbers = int(input('Введите количество предприятий для расчёта прибыли: '))
    for index in range(numbers):
        name_firm = str (input ('Введите название предприятия: '))
        annual_profit = str (input ('через пробел введите прибыль данного предприятия '
                                    'за каждый квартал(Всего 4 квартала):'))
        annual_profit = sum([int(string) for string in annual_profit.split ()])
        FIRMS_ARRAY = FIRMS (
            id = index,
            name_firm = name_firm,
            annual_profit = annual_profit
        )
        list_firms.append(FIRMS_ARRAY)
    avg_profit = reduce (lambda x, y: x + y,
                         [list_firms[index].annual_profit for index in range(len(list_firms))]) \
                 / len(list_firms)
    print(f'Средняя годовая прибыль всех предприятий: ', avg_profit)
    print (f'Предприятия, с прибылью выше среднего значения: ',
           ' ,'.join([list_firms[index].name_firm for index in range(len(list_firms))
                    if list_firms[index].annual_profit >= avg_profit]))
    print (f'Предприятия, с прибылью ниже среднего значения: ',
           ' ,'.join([list_firms[index].name_firm for index in range(len(list_firms))
                    if list_firms[index].annual_profit < avg_profit]))

