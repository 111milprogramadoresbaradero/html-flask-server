
from flask import Flask, request, redirect, send_from_directory
import db

# set the project root directory as the static folder, you can set others.
app = Flask(__name__)


@app.route('/')
def root():
    return send_from_directory('static', 'index.html')


@app.route('/test/curso')
def send_test_curso():
    return '<html><head><title>Test</title></head><body><h1>Pagina de prueba</h1></body></html>'

@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/sendForm')
def send_form():
    firstname = request.args.get('firstname')
    lastname = request.args.get('lastname')
    username1 = request.args.get('username1')
    username2 = request.args.get('username2')
    print("Agregando {}, {}, {}, {}".format(firstname, lastname, username1, username2))
    db.insertPersona(firstname, lastname, username1, username2)
    return root()


if __name__ == "__main__":
    db.init()
    app.run(host='0.0.0.0', port=9200)

