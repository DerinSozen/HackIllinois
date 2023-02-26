from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder = 'HackIllinois/website/templates')
Bootstrap(app)

@app.route("/")
def what():
    return render_template("login.html")

@app.route('/db')
def db():
    return render_template("dashboard.html")

@app.route('/logout')
def logout():
    return render_template("logout.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)