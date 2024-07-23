""" Flask это фреймворк для написания сайтов и приложений """

""" Настройка и запуск """
""" pip install flask """
""" python -m venv venv
    venv\Scripts\activate
    """
""" У каждого Flask-приложения должен быть экземпляр сервера: """
from flask import Flask

app = Flask(__name__) # создадим экземпляр(переменную app) класса Flask и передадим аргумент __name__

@app.route('/index') # используем декоратор route и укажем url-адрес по которому будет обрабатываться нижня функция представления
@app.route('/')      # если по определённым url-адресам нужно выболнять один и тот же обработчик(функцию), то прописываем декораторы друг за дружкой
def index():         # Во Flask декоратор route используется, чтобы связать URL-адрес с функцией.
    return "INDEX"

# если хотим добавить ещё один обработчик, то нужно добавить ещё один декоратор route
@app.route('/about')
def about():
    return '<h1> О сайте <h1>'

""" Динамические маршруты """
""" для этого переменная передается в декоратор внутри знаков <> и указывается под таким же названием в качестве параметра метода."""
# Можно воспользоваться несколькими переменными, разделив их знаком (например, слэш /).
# Если разделение не сделать, все написанное сольется в одну переменную
@app.route('/albus/<number>/<song_name>')
def albus(number,song_name):
    return f'это альбом номер {number}, композиция {song_name}'

# передадим в нашу функцию представления информацию и как она долджна выглядить на html-странице
@app.route('/gl2/')
def index2():
    return  """<h1><p>Hello, Flask!</p></h1>"""

""" для передачи одной и тойже инфы на все страницы используются шаблоны, они храняться в папке templates, для этого """
from flask import render_template  # импортируем модуль render_template. Эта функция вызывает механизм шаблонов Jinja2
@app.route('/gl3/')  # указываем путь
def index3():
    return  render_template('first.html')  # и указываем html-файл, который грузим

@app.route('/second/')
def second():
    return render_template('second.html')

# чтобы передать переменные в шаблон файл.html, в самом файле переменные берутся в двойный фигруные скобки {{}},
# а в файле запуска после return render_template(ипя файла, далее перечень переменных со значениями)
@app.route('/4/')
def index4():
    return render_template('first.html',name='Вася', age=25)

# на вход в адрес строки пишется вещественное число
@app.route('/<float:number>/')
def index5(number):
    return render_template('calculator.html',
                           text = f"Ваше число {number}, умноженное на 2: {number*2}")


# на вход в адрес строки пишется вещественное число, нужно передать его как радиус и ещё число пи туда отправить
@app.route('/<float:number>/')
def index6(number):
    return render_template('calculator.html',
                           r=number, pi=3.14)

@app.route('/<float:n1>/<z>/<float:n2>/')
def calculator(n1,z,n2):
    return render_template('calculator.html', n1=n1, z=z, n2=n2)






if __name__=='__main__':
    app.run(debug=True) # запустим локальный веб-сервер и параметр debug=True позволяет в браузере видеть
    # все ошибки разработки сайта/приложения. После окончания разработки нужно изменить True на False,
    # чтобы случайные ошибки реальный пользователь уже не видел
