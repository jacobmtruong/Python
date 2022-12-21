from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<int:num>')
def eight_by_four(num):
    return render_template("index.html", num=num)

@app.route('/<int:x>/<int:y>')
def x_by_y(x,y):
    return render_template("index.html", x=x, y=y)

if __name__=="__main__":
    app.run(debug=True)