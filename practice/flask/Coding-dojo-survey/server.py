from flask import Flask, render_template, request
app = Flask (__name__)
app.secret_key = "just your survey"

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/result', methods=['post'])
def submitted_info():
    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comments = request.form["comments"]
    return render_template("result.html", name=name,location=location,language=language, comments=comments)

if __name__=="__main__":
    app.run(debug=True)
