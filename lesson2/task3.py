"""
Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

Необходимо его обработать —
1) обособить каждое целое число (вещественные не трогаем) кавычками
2) дополнить нулём до двух целочисленных разрядов:
  ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

3) Сформировать из обработанного списка строку:
  в "05" часов "17" минут температура воздуха была "+05" градусов
4) Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
5) Как модифицировать это условие для чисел со знаком?

Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
Главное: дополнить числа до двух разрядов нулём!

"""
str_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

a = ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

