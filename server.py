from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index/<name>')
def index(name):
    return render_template('index.html', title=name)

@app.route('/training/<profs>')
def profession(profs):
    return render_template('index.html', prof=profs)

if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')