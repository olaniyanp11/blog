from blog import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True,unique=True,nullable=False)
    username = db.Column(db.String(20), unique=True,nullable=False)
    email = db.Column(db.String(20), unique=True,nullable=False)
    image_file = db.Column(db.String(20),nullable=False,default="default.jpg")
    password = db.Column(db.String(60),nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

    
class Post(db.Model):
      id = db.Column(db.Integer, primary_key=True,unique=True,nullable=False)
      title = db.Column(db.String(100),nullable=False)
      date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
      content = db.Column(db.Text, nullable=False)
      user_id= db.Column(db.Integer, db.ForeignKey('user_id'),nullable =False)

      def __repr__(self):
        return f"Post('{self.title}', '{self.date}')"

