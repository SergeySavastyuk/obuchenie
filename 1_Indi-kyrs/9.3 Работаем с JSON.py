"""Процесс сериализации в JSON-формат заключается в преобразовании питоновского объекта(обычно словаря,
но можно использовать и другие типы) в строку, сформированную по правилам JSON-формата. Например, такой вот словарь
{
 'apple': {"price": 10,"color": "green"},
 'banana': {"price": 4.5, 'color': "yellow"},
} """
"""будет преобразован вот в такую строку """
'{"apple": {"price": 10, "color": "green"}, "banana": {"price": 4.5, "color": "yellow"}}'
# Сериализацию можно использовать для хранения объектов на диске,
# для передачи его по сети или для передачи объекта другому процессу.


"""Десериализация это обратный процесс. Это «раскодирование» строки определенного формата обратно в питоновский словарь."""
# Итак, если вам нужно отправить данные из своей программы например на сервер, то речь идет о преобразовании в
# JSON - это сериализация. И обратно - получить данные из вне в виде JSON для использования в вашей программе - это десериализация.

import json
"""Для процесса сериализации модуль json предлагает две функции:
функция dumps преобразует объект в строку в формате json
функция dump преобразует объект в строку в формате json и записывает в файл

Для процесса десериализации модуль json предлагает также две функции:
функция loads десериализует JSON-строку в питоновский объект
функция load десериализует файл, хранящий JSON-строку, в питоновский объект"""

import json
import datetime
from random import randint

str_json = """ 
{
    "response": {
        "count": 32363,
        "items": [
            {
                "id": 287350527,
                "first_name": "Sonya",
                "last_name": "Kargina",
                "photo_50": "https://pp.vk.me/...2c1/J2EL--qCZa8.jpg"
            },
            {
                "id": 341523166,
                "first_name": "Slava",
                "last_name": "Kholod",
                "photo_50": "https://pp.vk.me/...321/eTxKNQSJMuk.jpg"
            }
        ]
    }
}
""" # здесь храниться данные из json файла
data = json.loads(str_json) # превращает строку в словарь с которым можно работать
for item in data["response"]["items"]:  # перебираем по нужному ключу
    del item["id"]
    item["likes"] = randint(100, 200)
    item['a'] = None
    item['b'] = True
    item['now'] = datetime.datetime.now().strftime("%d/%m/%y") # функции strftime - преобразует формат времени в строку
new_json = json.dumps(data)  # вернём обратно словарь в формат json для загрузки
print(new_json)

print('Ниже json с параметром indent'.center(40, '-'))
# Чтобы строка сформировалась в более красивом виде можно задать значение отступа в параметре indent функции dumps:
json_indent = json.dumps(data, indent = 2)
print(json_indent)
print('-'*60)
print()

# Обратите внимание на нижние значения:
# питоновское значение None будет сконвертировано в значение null в формате JSON
# питоновское значение True будет сконвертировано в значение true в формате JSON
# питоновское значение False будет сконвертировано в значение false в формате JSON
""" объекты преобразования
Python	                JSON
dict	                object
list, tuple	            array
str         	        string
int, long, float	    number
True	                true
False	                false
None	                null
"""

print('ниже добавление и удаление данных из файла')
import json

from random import randint
str_json2 = """
{
    "id": 287350527,
    "first_name": "Sonya",
    "last_name": "Kargina",
    "photo_50": "https://pp.vk.me/...2c1/J2EL--qCZa8.jpg"
}
"""
data = json.loads(str_json2)
del data["photo_50"]
data["likes"] = randint(100, 200)
data["is_married"] = False
data["is_adult"] = True
data["mail"] = None
json_indent = json.dumps(data, indent=2)
print(json_indent)
print(data, ' - тот же файл но без indent')
print(type(data), ' - тип нашего фала')
print()

'''Часто JSON необходимо сохранять в виде файла.'''
# Для этого в json есть метод dump, который принимает 2 аргумента: 1 – объект, который хотите сохранить,
# 2 – название файлика. Для этого воспользуемся инструкцией with.
with open("my.json", "w") as file:
    json.dump(data, file)
# В итоге создался файл my.json, который не очень удобный, из-за того, что он в 1 строку.
# Можно также воспользоваться параметром indent:
with open("my.json", "w") as file:
    json.dump(data, file, indent=2)
# Теперь файл с json будет более красивым.
# И раз мы можем сохранять это в файл, то мы сможем и забирать из него. Откроем его для чтения в чистом файле:
with open("my.json", "r") as file:
    json.load(file)
"""удалим файл чтобы не мешал в дереве   """
import os
os.remove('my.json')

print('Задания'.center(60,'-'))
print('---№1 Выполнить сериализацию словаря, дана строка латинских букв, сгенерируем словарь')
import json
from string import ascii_lowercase  # строка латинских букв
alphabet = {i:ascii_lowercase.index(i)+1 for i in ascii_lowercase} # сгенерируем словарь, где ключ - буква, значение - индекс в строке
json_data = json.dumps(alphabet) # преобразуем в JSON-строку
print(json_data)
print()

print('---№2 Распечатайте информацию о каждом человеке')
people = '[{"name": "Haley Whitney", "country": "British Indian Ocean Territory (Chagos Archipelago)", "age": 54}, ' \
         '{"name": "Matthew King", "country": "Colombia", "age": 34}, ' \
         '{"name": "Sean Sullivan", "country": "Mayotte", "age": 40}, ' \
         '{"name": "Christian Crawford", "country": "Russian Federation", "age": 29}, ' \
         '{"name": "Sarah Contreras", "country": "Honduras", "age": 82}]'
import json
a = sorted([(i['name'], i['country'], i['age']) for i in json.loads(people)], key=lambda x: (x[2],x))
print(*[f'{i[0]}, {i[1]}, {i[2]}' for i in a],sep='\n')