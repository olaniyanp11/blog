from flask import render_template,flash,redirect, url_for
from blog import app
from blog.forms import Registrarionform, Loginform
from blog.models import User, Post
from datetime import datetime

date = datetime.today()
posts = [
    {
        'authors': 'permac',
        'title':'Blog post 1',
        'content': """
        well i dont really have something to say
        """,
        'date' : date
    },
    {
        'authors': 'jane Doe',
        'title':'Blog post 2',
        'content': """
        well i dont really have something to say
        """,
        'date' : date
    }
]

@app.route("/")
@app.route("/index")
def index():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html",About='About')


@app.route("/register",methods=['GET','POST'])
def register():
    form = Registrarionform()
    if form.validate_on_submit():
        flash(f'Account created for{form.username.data}','success')
        return redirect(url_for('index'))
    return render_template("register.html",About='register',form=form)


@app.route("/login",methods=['GET','POST'])
def login():
    form = Loginform()
    if form.validate_on_submit():
        if form.email.data == "pisrael070@gmail.com" and form.password.data == "12345":
            flash(f' welcome user {form.email.data}','success')
            return redirect(url_for('index'))
        else:
            flash(f'Unsuccessful Login . Please check Credentials ','danger')
    return render_template("login.html",About='login',form=form)

