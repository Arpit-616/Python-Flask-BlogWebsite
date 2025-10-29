from flask import Flask, render_template, request, session, flash, redirect, url_for
from flask_mail import Mail, Message
import json
from werkzeug.utils import secure_filename
from datetime import datetime
import os
import math

app = Flask(__name__)

# Load configuration
basedir = os.path.abspath(os.path.dirname(__file__))
config_path = os.path.join(basedir, 'config.json')
with open(config_path, 'r') as c:
    params = json.load(c)["params"]

# Set upload folder
app.config['UPLOAD_FOLDER'] = params['upload_location']
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

app.secret_key = 'F4'

# Configure Flask-Mail
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-password']
)
mail = Mail(app)

# Dummy in-memory storage for posts and contacts (no database)
posts_data = [
    {
        "sl_no": 1,
        "title": "Welcome Post",
        "slug": "welcome-post",
        "content": "This is your first post!",
        "tagline": "Excited to start blogging",
        "date": datetime.now().strftime("%Y-%m-%d")
    }
]

contacts_data = []

# -------------------- ROUTES --------------------

@app.route("/")
def home():
    flash("Welcome to my blog!", "success")
    all_posts = posts_data
    last = math.ceil(len(all_posts) / int(params['no_of_posts'])) + 1
    num = len(all_posts)

    page = int(request.args.get('page', 1))
    if not str(page).isnumeric():
        page = 1

    start = (page - 1) * int(params['no_of_posts'])
    end = start + int(params['no_of_posts'])
    all_posts = all_posts[start:end]

    prev = "#" if page == 1 else f"/?page={page-1}"
    next = "#" if page == last else f"/?page={page+1}"

    first = list(range(1, num + 1))
    last_pages = [i for i in range(num - 5, num + 1)] if num > 6 else first

    return render_template('index.html', params=params, posts=all_posts,
                           prev=prev, next=next, first=first, last=last_pages)


@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    if 'user' in session and session['user'] == params['admin_user']:
        return render_template('dashboard.html', params=params, posts=posts_data)

    if request.method == 'POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if username == params['admin_user'] and userpass == params['admin_password']:
            session['user'] = username
            return render_template('dashboard.html', params=params, posts=posts_data)
    return render_template('login.html', params=params)


@app.route("/about")
def abouts():
    return render_template('about.html', params=params)


@app.route("/uploader", methods=['GET', 'POST'])
def uploader():
    if 'user' in session and session['user'] == params['admin_user']:
        if request.method == 'POST':
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            return "Uploaded successfully"


@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect('/dashboard')


@app.route("/contact", methods=['GET', 'POST'])
def contacts():
    flash("Thank you for submitting your message!", "success")
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone_num = request.form.get('phone_num')
        message = request.form.get('message')

        # Store contact locally (no DB)
        contacts_data.append({
            "name": name,
            "email": email,
            "phone": phone_num,
            "message": message,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        # Send email
        msg = Message(
            subject=f'New message from {name}',
            sender=params['gmail-user'],
            recipients=[params['gmail-user']],
            body=f"Name: {name}\nEmail: {email}\nPhone: {phone_num}\nMessage: {message}"
        )
        mail.send(msg)
    return render_template('contact.html', params=params)


@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = next((p for p in posts_data if p["slug"] == post_slug), None)
    if post is None:
        return render_template('404.html', params=params), 404
    return render_template('post.html', params=params, post=post)


@app.route("/post")
def posts():
    return render_template('post.html', params=params, post=posts_data)


# Jinja helper
app.jinja_env.globals.update(datetime=datetime)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
