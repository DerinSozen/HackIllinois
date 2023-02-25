from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route('/cal')
def cal():
    return render_template("kanban.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)