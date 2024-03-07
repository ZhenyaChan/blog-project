from flask import Flask, render_template
import requests


app = Flask(__name__)

posts = requests.get("https://api.npoint.io/e7889fd9caee6c0e8d92").json()


@app.route("/")
def home():
    return render_template("index.html", all_posts=posts)


@app.route("/<path:page>")
def static_page(page):
    return render_template(f"{page}.html")


if __name__ == "__main__":
    app.run(debug=True)
