from flask import Flask,render_template,request,redirect
import os.path
from os import path

app = Flask(__name__)
@app.route("/")

def main():
    return render_template("welcomepage.html");

@app.route("/info",methods=["POST"])
def test():
    return render_template("login1.html");

if __name__=="__main__":
    app.run();
