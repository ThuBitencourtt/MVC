from app import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    @property
    def is_authenticated(self):
        return True 

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
    

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email


    def __repr__(self):
        return "<User %r>" % self.username


class Livro(db.Model):
     __tablename__ = "book"

     id = db.Column(db.Integer, primary_key=True)
     livro = db.Column(db.String, unique=True)
     autor = db.Column(db.String)
     editora = db.Column(db.String)
     cidade = db.Column(db.String, unique=True)

     def __init__(self, livro, autor, editora, cidade):
         self.livro = livro
         self.autor = autor
         self.editora = editora
         self.cidade = cidade        


     def __repr__(self):
        return "<Livro %r>" % self.id 


