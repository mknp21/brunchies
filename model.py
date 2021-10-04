"""Models for brunch locator app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(25), nullable=False, unique=True)
    pw = db.Column(db.String(20), nullable=False)
    zipcode = db.Column(db.String(10))

    # saves = a list of SaveList objects

    def __repr__(self):
        return f"User name={self.name} email={self.email}"

class Restaurants(db.Model):
    """A restaurant."""

    __tablename__ = 'restaurants'

    rest_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    category = db.Column(db.String(25))
    rest_name = db.Column(db.String(50))
    rest_zip = db.Column(db.String(10))
    coord = db.Column(db.Float)
    attributes = db.Column(db.String(100))
    rating = db.Column(db.Float)

    # saves = a list of SaveList objects

    def __repr__(self):
        return f"Restaurant name={self.rest_name} category={self.category}"

class SaveList(db.Model):
    """List of saved restaurants."""

    __tablename__ = "saves"

    save_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    rest_id = db.Column(db.Integer, db.ForeignKey('restaurants.rest_id'))

    user = db.relationship("User", backref="saves")
    # save.user returns related User object
    restaurant = db.relationship("Restaurant", backref="saves")
    # save.restaurant returns related Restaurant object

# relationships between classes:
# a user has many saves
# many favorites each point to one restaurant
# a restaurant has many saves from different users

def connect_to_db(flask_app, db_uri="postgresql:///brunch", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)