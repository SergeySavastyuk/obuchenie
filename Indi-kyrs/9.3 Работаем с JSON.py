"""Процесс сериализации в JSON-формат заключается в преобразовании питоновского объекта(обычно словаря,
но можно использовать и другие типы) в строку, сформированную по правилам JSON-формата. Например, такой вот словарь"""
{
 'apple': {"price": 10,"color": "green"},
 'banana': {"price": 4.5, 'color': "yellow"},
}
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
"""
data = json.loads(str_json)
for item in data["response"]["items"]:
    del item["id"]
    item["likes"] = randint(100, 200)
new_json = json.dumps(data)
print(new_json)
print('Ниже json с параметром indent'.center(40, '-'))
# Чтобы строка сформировалась в более красивом виде можно задать значение отступа в параметре indent функции dumps:
json_indent = json.dumps(data, indent = 2)
print(json_indent)
print('-'*40)

# Обратите внимание на нижние значения:
# питоновское значение None будет сконвертировано в значение null в формате JSON
# питоновское значение True будет сконвертировано в значение true в формате JSON
# питоновское значение False будет сконвертировано в значение false в формате JSON
import json
import datetime
from random import randint
str_json = """
{
    "id": 287350527,
    "first_name": "Sonya",
    "last_name": "Kargina",
    "photo_50": "https://pp.vk.me/...2c1/J2EL--qCZa8.jpg"
}
"""
data = json.loads(str_json)
del data["photo_50"]
data["likes"] = randint(100, 200)
data["is_married"] = False
data["is_adult"] = True
data["mail"] = None
json_indent = json.dumps(data, indent=2)
print(json_indent)

for item in data["response"]["items"]:
    del item["id"]
    item["likes"] = randint(100, 200)
    item['a'] = None
    item['b'] = True
    item['now'] = datetime.now().strftime("%d/%m/%y") # функции strftime - преобразует формат времени в строку

# Часто JSON необходимо сохранять в виде файла.
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
print(data)
print(type(data))

"""выполнить сериализацию словаря"""
import json
from string import ascii_lowercase  # строка латинских букв
alphabet = {i:ascii_lowercase.index(i)+1 for i in ascii_lowercase} # сгенерируем словарь, где ключ - буква, значение - индекс в строке
json_data = json.dumps(alphabet) # преобразуем в JSON-строку
print(json_data)


""" Распечатайте информацию о каждом человеке """
people = '[{"name": "Haley Whitney", "country": "British Indian Ocean Territory (Chagos Archipelago)", "age": 54}, ' \
         '{"name": "Matthew King", "country": "Colombia", "age": 34}, ' \
         '{"name": "Sean Sullivan", "country": "Mayotte", "age": 40}, ' \
         '{"name": "Christian Crawford", "country": "Russian Federation", "age": 29}, ' \
         '{"name": "Sarah Contreras", "country": "Honduras", "age": 82}]'
import json
a = sorted([(i['name'], i['country'], i['age']) for i in json.loads(people)], key=lambda x: (x[2],x))
print(*[f'{i[0]}, {i[1]}, {i[2]}' for i in a],sep='\n')