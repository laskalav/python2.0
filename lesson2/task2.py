"""
Задание 2
Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и
кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел
со знаком?
Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное:
дополнить числа до двух разрядов нулём!
"""
initial_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

result_list = []
for word in initial_list:
    if word.isdigit():
        result_list.append('"')
        result_list.append(word.zfill(2))
        result_list.append('"')
    elif (word[0] == '+') and word[1:].isdigit():
        sing = word[0]
        result_list.extend(['"' + sing + f'{int(word[1:]):02}"'])
    else:
        result_list.append(word)

print(' '.join(result_list))