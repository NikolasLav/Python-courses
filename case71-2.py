import os
from pprint import pprint
import unicodedata  #пришлось добавить, иначе некоторые пробелы и символы '|' воспринимались некорректно

with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    item = 'yyyyy'
    for line in file:
        s = unicodedata.normalize("NFKD", line.strip()).split(
            ' | ')  #вкорячил костыль, ибо на реплите не читается файл норм
        if len(s) == 1 and s[0] != '' and not s[0].isdigit():
            item = s[0]
            cook_book[item] = []
        elif len(s) == 3:
            cook_book[item].append({
                'ingredient_name': s[0],
                'quantity': int(s[1]),
                'measure': s[2]
            })

print(cook_book)
