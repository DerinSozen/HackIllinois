from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from website import create_app

if __name__ == "__main__":
    app = create_app()
    Bootstrap(app)
    app.run(debug=True, port=5000)