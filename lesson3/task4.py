
employees = ['Игорь Чеботкевич',
             'Виктор Чеботкевич',
             'Илья Лавров',
             'Вольдемар Лангерн',
             'Никита Лавров',
             'Ирина Мун',
             'Наталья Миронова',
             'Владимир Черепков',
             'Нина Макарова']


def thesaurus_adv(*args):
    dict_employees = {}
    for el in args:
        el = el.split()
        key = el[1]
        key2 = key[0]
        if key2 not in dict_employees.keys():
            dict_employees[key2] = []
        dict_employees[key2].append(' '.join(el))
    return dict_employees


print(thesaurus_adv(*employees))