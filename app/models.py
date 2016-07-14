from app import db
from app import bcrypt

class Blog(db.Model):

    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    content = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __init__(self, title, content, author_id, category_id, pub_date=None):
        self.title = title
        self.content = content
        self.author_id = author_id
        self.category_id = category_id

        from datetime import datetime
        if not pub_date:
            self.pub_date = datetime.now()  #.strftime('%Y-%m-%d %X')

    def __repr__(self):
        return '<Post %r>' % self.title

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))

    blogs = db.relationship('Blog', backref='author', lazy='dynamic')

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % self.name

class Category(db.Model):

    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    blogs = db.relationship('Blog', backref='category', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_all(cls):
        results = []
        for c in cls.query.all():
            results.append((str(c.id), c.name))
        return results

    def __repr__(self):
        return '<Category %r>' % self.name
