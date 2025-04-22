from flask import Flask,render_template,request,redirect
import os.path

global whichfilename;
whichfilename = "LoginAccounts.doc";
app=Flask(__name__)

@app.route("/")
def main():
    return render_template("login1.html");

@app.route("/info",methods=["POST"])
def getinfo():
    global username
    global userpasswd
    username=request.form.get('txtusername');
    userpasswd=request.form.get('tctpassword');
    if(username=="" or userpasswd==""):
        return render_template()

if __name__=="__main__":
    app.run();
