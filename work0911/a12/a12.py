from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/p1")
def page01():
    return render_template('p1.html')

@app.route("/p2")
def page02():
    return render_template('p2.html')


@app.route("/p3")
def page03():
    return render_template('p3.html')


@app.route("/p4")
def page04():
    return render_template('p4.html')


if __name__=='__main__':
    app.run()