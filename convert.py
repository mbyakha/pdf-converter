from flask import Flask, render_template, redirect

convert=Flask(__name__)

@convert.route("/")
def index_page():
    return render_template("index.html")

@convert.route("/convert")
def con():
    return render_template("convert.html")



if __name__=="__main__":
    convert.run(port="2032", debug=True)
