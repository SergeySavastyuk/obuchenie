from flask import Flask,render_template
from requests import request

app = Flask(__name__)

@app.route('/', methods=['get','post'])
def index():
    client_message = ''
    server_message = ''
    if request.methods =='post':
        client_message =request.form.get('message')


    if client_message != '':
        server_message = 'how are you'

    return render_template('4.1 GET и POST-запросы.html', message=server_message)
if __name__=='__main__':
    app.run(debug=True)


print(*sorted([input() for i in '___'],reverse=True),sep='\n')