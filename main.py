# Напишите функцию, которая будет принимать номер кредитной карты
# и показывать только последние 4 цифры. Остальные цифры должны заменяться звездочками
def number(card):
    return '*' * (len(card) - 4) + card[-4:]
print(number('123456765675'))



# Напишите функцию, которая проверяет: является ли слово палиндромом
def polindrom(string):
    line = str(string)
    if line [::-1] == line:
        print('Слово полиндром')
    else:
        print('Слово не полиндром')
polindrom('dddfddf')
