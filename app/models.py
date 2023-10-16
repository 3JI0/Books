from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(64), index=True, unique=False)
    books= db.Column(db.String(140))
   
   
    def __repr__(self):
        return '<Author: {}>'.format(self.author)