
from flask import Flask, request, redirect, send_from_directory

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9200)
