from flask import Flask , render_template, request, redirect, url_for
import pandas as pd

site = Flask("Site")

# TASK: update the webpage which include "password not the same" if the password is not the same
# TASK: make a list of emails from csv file and check whether email is taken or not
# TASK: email and password should be correct in login and take them to home

@site.route("/")
def main():
    return render_template("home.html")

@site.route("/signup", methods = ["POST", "GET"])
def signup():
    db = pd.read_csv("user_data.csv")
    email_list = list(db["email"])
    if request.method == "POST":

        name = request.form.get("f_name")
        email = request.form.get("email")
        pwd = request.form.get("password")
        c_pass = request.form.get("c_pass")
        print(pwd,c_pass)

        if email in email_list:
            return render_template("signup.html"
                                    ,error="Email is already taken")
        elif pwd != c_pass:
            return render_template("signup.html"
                                   ,error="Password does not match. Try again!") 
        
        data = f"{name},{email},{pwd}" + "\n"
        print(data)
        
        with open("user_data.csv", "r") as userdata:
            u_d = userdata.readlines()
            u_d.append(data)
            print(u_d)
            u_d = "".join(u_d)
            print(u_d)
            

        with open("user_data.csv","w") as userdata2:
            userdata2.writelines(u_d)


        return redirect(url_for("login"))
    return render_template("signup.html")

@site.route("/login", methods = ["POST","GET"])
def login():
    db = pd.read_csv("user_data.csv")
    if request.method == "POST":

        email = request.form.get("mail")
        password = request.form.get("pwd")
        dic = db.set_index("email")["password"].to_dict()
        print(email,password)
        try:
            if password == str(dic[email]):
                return redirect(url_for("home")) 
            else: render_template("login.html",error="Password does not match") 
        except KeyError:
            return render_template("login.html",error="Email not registered")   
    return render_template("login.html")

@site.route("/home")
def home():
    # Stuff for logged in user (Coming Soon)
    return render_template("home.html")
    
site.run(debug=True)