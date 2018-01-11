import os
from flask import Flask, url_for, render_template, redirect
app = Flask(__name__)

@app.route('/...')
@app.route('/<path:name>/...')
def back(name=None):
    print(url_for('index', name=name))
    return redirect(url_for('index', name=name))

@app.route('/')
@app.route('/<path:name>')
def index(name=''):
    file_list = list()
    root_path = './static/' + name
    for x in os.listdir(root_path):
        path = os.path.join(root_path, x)
        if name == '':
            filename = x
        else:
            filename='{}/{}'.format(name, x)
        if not os.path.isdir(path):
            file = {
                'is_file': True,
                'filename': x,
                'url': url_for('static', filename=filename)
            }
        else:
            file = {
                'is_file': False,
                'filename': x,
                'url': url_for('index', name=filename)
            }
        file_list.append(file)
    return render_template('main.html', files=file_list)

