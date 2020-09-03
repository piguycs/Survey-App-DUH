from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)


@app.route('/')
def blank():
    return render_template("index.html")


@app.route('/lslct', methods=['POST', 'GET'])
def loginselect():
    if request.method == 'POST':
        if request.form["user"] == ("admin"):
            return redirect("/alogin")
        elif request.form["user"] == ("participant"):
            return ("💩")


@app.route('/alogin', methods=['POST', 'GET'])
def alogin():
    return render_template("alogin.html")


@app.route('/azure')
def sso():
    #whatever the f goes here
    return render_template("admin.html")



@app.route('/key/<int:key>')
def adminkey(key):
    return render_template("admin.html", key = key)


if __name__ == '__main__':
    app.run(debug=True)
