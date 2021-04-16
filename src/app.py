from flask import *

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/home/<name>')
def home(name=None):
    return render_template('index.html', name=name)

