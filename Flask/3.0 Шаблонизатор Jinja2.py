from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def calculator():
    return render_template('Jinja2.html',
                           name = 'Вася',
                           age = 26,
                           text= 'ТЕКСТ',
                           comment = 'КОММЕНТАРИЙ',
                           Title=' Заглавие ')


""" расширерение / наследование """

@app.route('/about/')
def about():
    return render_template('about.html',
                           name='Вася',
                           age=26,
                           text='ТЕКСТ',
                           comment='КОММЕНТАРИЙ',
                           Title=' Заглавие '
                           )

if __name__ == "__main__":
    app.run(debug=True)