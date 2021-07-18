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
        
        c = self
        return f'<Cupcake {c.id} flavor={c.flavor} size={c.size} rating={c.rating} image={c.image}'

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

    def serialize(self):
        return {
            'id' : self.id,
            'flavor' : self.flavor,
            'size' : self.size,
            'rating' : self.rating,
            'image' : self.image
        }
    

