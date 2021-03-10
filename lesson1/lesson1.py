u_seconds = int(input("Введите время: "))

minutes = u_seconds // 60  # вводные данные
seconds = u_seconds % 60  # остаток секунд
hours = minutes // 60  # кол - во часов
minutes = minutes % 60
days = hours // 24  # количество дней
hours = hours % 24

if u_seconds <= 59:
    print("%02d sec" % seconds)
elif 60 <= u_seconds <= 3600:
    print("%02d min %02d sec" % (minutes, seconds))
elif 3600 <= u_seconds <= 86390:
    print("%02d hours %02d min %02d sec" % (hours, minutes, seconds))
elif u_seconds >= 86400:
    print("%02d days %02d hours %02d min %02d sec" % (days, hours, minutes, seconds))
