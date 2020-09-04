from flask import Flask, abort, redirect, url_for, request, render_template
app = Flask(__name__)


#Renders the main incex.html
@app.route('/', methods=['POST', 'GET'])
def home():
  if request.method == 'POST':
    if request.form["user"] == ("admin"):
      print("Let's go. In and out. Twenty minute adventure.")
      try:
        return redirect(url_for("alogin"))
      except Exception as e:
        print("I dont know, Rick")
        return e
    elif request.form["user"] == ("participant"):
      return redirect(url_for("survey"))
  return render_template("index.html")


#Azure SSO
@app.route('/alogin', methods=['POST', 'GET'])
def alogin():
    return render_template("alogin.html")


#Azure SSO more
@app.route('/azure')
def sso():
    #whatever the f goes here
    return render_template("admin.html")


@app.route('/survey', methods=['POST', 'GET'])
def survey():
    if request.method == "POST":
      req = request.form
      q1 = req.get("gender")
      print(q1)
    questions = [["Are you a Dutch citizen?","radio","yes","no"]]
    
    return render_template("survey.html", questions = questions)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)
