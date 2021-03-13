from sys import argv
from mymodule import get_currency_rate

for el in argv[1:]:
    print(get_currency_rate(el))

print([(get_currency_rate(el)) for el in argv[1:]])
