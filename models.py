from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
        db.app = app
        db.init_app(app)


class Pet(db.Model):
    '''Database model for Users'''

    __tablename__ = ''

    def __repr__(self):
        
        u = self
        return f'<User {u.id} '

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    

