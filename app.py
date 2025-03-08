from flask import Flask, render_template, url_for
from routes.auth import auth
from routes.upload import upload

app = Flask(__name__)

app.register_blueprint(auth)
app.register_blueprint(upload)


@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)