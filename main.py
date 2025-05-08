from flask import Flask,render_template,request, session,flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import json
from werkzeug.utils import secure_filename
from datetime import datetime
from flask import redirect, url_for
import os
import math

app = Flask(__name__)

# Load configuration first - using absolute path
basedir = os.path.abspath(os.path.dirname(__file__))
config_path = os.path.join(basedir, 'config.json')
with open(config_path, 'r') as c:
    params = json.load(c)["params"]

# Now set the upload folder after params is defined
app.config['UPLOAD_FOLDER'] = params['upload_location']

# Create upload directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

local_server = True

# Configure Flask-Mail
app.secret_key = 'F4'
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-password']
)

# Configure SQLAlchemy
if(local_server):
    app.config["SQLALCHEMY_DATABASE_URI"] = params["local_uri"]
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params["prod_uri"]

# Initialize extensions
db = SQLAlchemy(app)
mail = Mail(app)


class Contacts(db.Model):
     sl_no=db.Column(db.Integer,primary_key=True)
     name=db.Column(db.String(50),nullable=False)
     phone_no=db.Column(db.String(50),nullable=False)
     email=db.Column(db.String(50),nullable=False)
     date=db.Column(db.String(50),nullable=False)
     msg=db.Column(db.String(50),nullable=False)

# Rename the model class from 'posts' to 'Posts'
class Posts(db.Model):
     sl_no=db.Column(db.Integer,primary_key=True)
     title=db.Column(db.String(80),nullable=False)
     slug=db.Column(db.String(21),nullable=False)
     content=db.Column(db.String(120),nullable=False)
     tagline=db.Column(db.String(120),nullable=False)
     date=db.Column(db.String(12),nullable=False)

@app.route("/")
def home():
     flash("      Welcome to my blog!","success")
     # Use the renamed Posts class
     all_posts = Posts.query.filter_by().all()
     last=math.ceil(len(all_posts)/int(params['no_of_posts']))+1
     num=len(all_posts)
     if 'page' not in request.args:
          page=1
     else:
          page=int(request.args.get('page'))
     if not str(page).isnumeric():
          page=1
     page=int(page)
     all_posts=all_posts[(page-1)*int(params['no_of_posts']):(page-1)*int(params['no_of_posts'])+int(params['no_of_posts'])]
     # First page
     if page==1:         
          prev="#"
          next="/?page="+str(page+1)
     elif page==last:
          prev="/?page="+str(page-1)
          next="#"
     else:
          prev="/?page="+str(page-1)
          next="/?page="+str(page+1)
     first=[]
     last=[]
     for i in range(1,num+1):
          first.append(i)
          if i>num-6:
               last.append(i)
     return render_template('index.html', params=params, posts=all_posts,prev=prev,next=next,first=first,last=last)
@app.route("/dashboard",methods=['GET','POST'])
def dashboard():

     if 'user' in session and session['user']==params['admin_user']:
          all_posts = Posts.query.all()
          return render_template('dashboard.html', params=params, posts=all_posts)


     if request.method == 'POST':
          username=request.form.get('uname')
          userpass=request.form.get('pass')
          if username==params['admin_user'] and userpass==params['admin_password']:
            #    set the session
            session['user']=username
            all_posts = Posts.query.all()
            return render_template('dashboard.html', params=params, posts=all_posts)
     return render_template('login.html', params=params)
@app.route("/about")
def abouts():
     return render_template('about.html', params=params)


@app.route("/edit/<string:sl_no>",methods=['GET','POST'])
def edit(sl_no):
     if 'user' in session and session['user']==params['admin_user']:
          if request.method=='POST':
               box_title=request.form.get('box_title')  # Changed from 'title' to 'box_title'
               tline=request.form.get('tline')
               slug=request.form.get('slug')
               content=request.form.get('content')
               date=datetime.now().strftime("%Y-%m-%d") # Format date as string
               if sl_no=='0':
                    post=Posts(title=box_title,slug=slug,content=content,tagline=tline,date=date)
                    db.session.add(post)
                    db.session.commit()
                    return redirect('/dashboard')  # Redirect to dashboard after adding new post
               else:
                    post=Posts.query.filter_by(sl_no=sl_no).first()
                    post.title=box_title
                    post.slug=slug
                    post.content=content
                    post.tagline=tline
                    post.date=date
                    db.session.commit()
                    return redirect('/dashboard')  # Redirect to dashboard after editing post
          post=Posts.query.filter_by(sl_no=sl_no).first()
          return render_template('edit.html', params=params,post=post,date=datetime.now().strftime("%Y-%m-%d"),sl_no=sl_no)
@app.route("/uploader",methods=['GET','POST'])
def uploader():
     if 'user' in session and session['user']==params['admin_user']:
          if request.method=='POST':
               f=request.files['file1']
               f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
               return "Uploaded successfully"
@app.route("/logout")
def logout():
     session.pop('user')
     return redirect('/dashboard')

@app.route("/delete/<string:sl_no>",methods=['GET','POST'])
def delete(sl_no):
     if 'user' in session and session['user']==params['admin_user']:
          post=Posts.query.filter_by(sl_no=sl_no).first()
          db.session.delete(post)
          db.session.commit()
     return redirect('/dashboard')  


@app.route("/contact",methods=['GET','POST'])
def contacts():
     flash("Thank you!! for submitting your message.","success")
     if request.method == 'POST':
          name=request.form.get('name')
          email=request.form.get('email')
          phone_num=request.form.get('phone_num')
          message=request.form.get('message')
          # In the contacts route - line 131
          entry=Contacts(name=name,phone_no=phone_num,email=email,date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),msg=message)
          db.session.add(entry)
          db.session.commit()
          
          # Send email
          msg = Message(
               subject=f'New message from {name}',
               sender=params['gmail-user'],  # Use your configured email as sender
               recipients=[params['gmail-user']],
               body=f"Name: {name}\nEmail: {email}\nPhone: {phone_num}\nMessage: {message}"
          )
          mail.send(msg)
     return render_template('contact.html', params=params)

@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    # Check if post exists
    post = Posts.query.filter_by(slug=post_slug).first()
    if post is None:
        # Return 404 if post not found
        return render_template('404.html', params=params), 404
    return render_template('post.html', params=params, post=post)

@app.route("/dashboard/google")
def google_login():
    # Add your Google OAuth logic here
    return redirect(url_for('home'))

@app.route("/dashboard/github")
def github_login():
    # Add your GitHub OAuth logic here
    return redirect(url_for('home'))

@app.route("/post")
def posts():
    all_posts = Posts.query.all()
    return render_template('post.html', params=params, post=all_posts)

# Add this after creating the Flask app
from datetime import datetime
app.jinja_env.globals.update(datetime=datetime)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
