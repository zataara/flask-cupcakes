from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
        db.app = app
        db.init_app(app)


DEFAULT_IMAGE = "https://tinyurl.com/demo-cupcake"

class Cupcake(db.Model):
    '''Database model for Users'''

    __tablename__ = 'cupcakes'

    def __repr__(self):
        
        u = self
        return f'<Cupcake {u.id} '

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    flavor = db.Column(db.Text,
                        nullable=False)
    size = db.Column(db.Text,
                        nullable=False)
    rating = db.Column(db.Integer,
                        nullable=False)
    image = db.Column(db.Text,
                        nullable=False,
                        default=DEFUALT_IMAGE)
    

