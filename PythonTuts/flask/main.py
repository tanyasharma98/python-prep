from flask import Flask, escape, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail
import json
import jinja2

local_server = True
with open("config.json", "r") as f:
    params = json.load(f)["params"]
app = Flask(__name__)

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-password']
)
mail = Mail(app)
if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)


class Contact(db.Model):
    """ sno , name , email, number , msg ,date"""
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(20), unique=False, nullable=False)
    number = db.Column(db.String(12), unique=False, nullable=False)
    msg = db.Column(db.String(120), unique=False, nullable=False)
    date = db.Column(db.String(12), unique=False, nullable=True)


class Posts(db.Model):
    """ sno , title, slug, content, date , img_file"""
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    slug = db.Column(db.String(20), unique=False, nullable=False)
    content = db.Column(db.String(120), unique=False, nullable=False)
    date = db.Column(db.String(12), unique=False, nullable=True)
    img_file = db.Column(db.String(20))


@app.route('/')
def home():
    return render_template('/index.html', params=params)


@app.route('/about')
def about():
    name = request.args.get("name", "Tanya")
    return render_template('/about.html', name2=name, params=params)


@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    img_file = request.__add__('img_file')
    return render_template('/post.html', params=params, post=post,img_file=img_file)


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        msg = request.form['msg']
        """ sno , name , email, number , msg ,date"""
        entry = Contact(name=name, email=email, date=datetime.now(), number=phone, msg=msg)
        db.session.add(entry)
        db.session.commit()
        mail.send_message(f"New message from {name}", recipients=[params['gmail-user']], sender=email,
                          body=msg + "\n" + phone)
    return render_template('/contact.html', params=params)


app.run(debug=True)
