from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')

def index():
    return (render_template('index.html'))

@app.route('/about')
def about():
    return(render_template('about.html'))

users = {}

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET": #NO FORM DATA
        return render_template('register.html')
    elif request.method == "POST": #POST FORM DATA
        username, password = request.form['username'], request.form['password']
        for char in username:
            if not char.isalpha() and not char.isdecimal() and char != "_":
                return render_template("register.html", error_msg = "<Wrong Username Input>")

        if len(password) <8 or len(password) > 64:
                return render_template("register.html", error_msg = "<Wrong Password Input. Length of password should be between the ranges of 8 and 64>")

        upper_case_requirement = False
        lower_case_requirement = False
        digit_requirement = False
        for pass_char in password:
            if pass_char.isupper():
                upper_case_requirement = True
            if pass_char.islower():
                lower_case_requirement = True
            if pass_char.isdigit():
                digit_requirement = True


        if upper_case_requirement and lower_case_requirement and digit_requirement:
            users[username] = password
            return (render_template('register.html',success_msg = f"Registered under {username}"))

        return render_template("register.html", error_msg = "<Wrong Password format. Requires an upper & lower case as well as 1 digit>")


    #the 2nd paramete of render template is also the jinja template variable. 
            
@app.route('/login', methods = ["GET" , "POST"])
def login():

    if request.method == "GET":
        return render_template('login.html')

    if request.method == "POST":
        username , password = request.form['username'], request.form['password']
        if username == "" or password == "":
            return render_template('login.html', error_msg = "<Empty Username or Password>")

        if users.get(username) == password:
            return render_template('login.html', success_msg = f"Logged into {username} under password: {password}")

        return(render_template('login.html', error_msg = "<Incorrect Username or Password>"))
            

app.run()
