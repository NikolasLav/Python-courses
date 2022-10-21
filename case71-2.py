import os
from pprint import pprint
import unicodedata  #пришлось добавить, иначе некоторые пробелы и символы '|' воспринимались некорректно


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for item in cook_book[dish]:
                ing, val, ms = item.values()
                val = val * person_count 
                if ing in shop_list:
                    shop_list[ing]['quantity'] += val
                else:
                    shop_list[ing] = {'measure': ms, 'quantity': val}
        else:
            print(f'Блюда "{dish}" нет в кулинарной книге')
    return pprint(shop_list)


with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
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
pprint(cook_book)

get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)











