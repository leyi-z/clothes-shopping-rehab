from flask_sqlalchemy import SQLAlchemy


database_name = "db_csrp"
database_path = "postgres://{}@{}/{}".format('leyi_psql', 'localhost:5432', database_name)


db = SQLAlchemy()


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    

def db_drop():
    db.drop_all()

def db_create():
    db.create_all()
    

class Location(db.Model):
    __tablename__ = 'location'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)
    
    def format(self):
        return {
            'id': self.id,
            'name': self.name
        }
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
  
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
        
    
    
class Clothes(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.Integer, db.ForeignKey('location.id'))
    category = db.Column(db.String())
    description = db.Column(db.String())
    
    def format(self):
        return {
            'id': self.id,
            'location': self.location,
            'category': self.category,
            'description': self.description,
        }
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
  
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()