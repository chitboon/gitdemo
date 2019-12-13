from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def home1():
    return render_template('home.html')

@app.route('/user')
def home2():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()
