#! --*-- coding: utf-8 --*--
__author__ = 'gaoxingsheng'

from flask import Flask, render_template

app = Flask(__name__)

t_title = "First"


@app.route("/")
def hello():
    # return "Hello World!"
    content = "Hello World!"
    return render_template("simple.html", content=content, title=t_title)


if __name__ == "__main__":
    app.run()