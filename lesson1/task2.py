user_number = input('Введите число. Для завершения программы введите 0: ')

res = 0
for i in user_number:
    res += int(i)

print(res)
