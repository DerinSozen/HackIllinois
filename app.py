
app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route('/cal')
def cal():
    return render_template("kanban.html")

@app.route('/logout')
def logout():
    return render_template("logout.html")

@app.route('/login')
def login():
    return "login placeholder"

if __name__ == "__main__":
    app.run(debug=True, port=5000)