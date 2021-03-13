from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index/<name>')
def index(name):
    return render_template('index.html', title=name)

@app.route('/training/<profs>')
def profession(profs):
    return render_template('index.html', prof=profs)

@app.route('/list_prof/<list>')
def list_of_professions(list):
    return render_template('index.html', list=list)

@app.route('/login')
def login():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')