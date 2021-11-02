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
    zipcode = db.Column(db.String(10), nullable=False)

    # saves = a list of SaveList objects

    def __repr__(self):
        return f"<User name={self.name} email={self.email}>"

class Restaurant(db.Model):
    """A restaurant."""

    __tablename__ = 'restaurants'

    rest_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    yelp_id = db.Column(db.String(50), unique=True, nullable=False)
    rest_name = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    review_count = db.Column(db.Integer, nullable=True)
    price = db.Column(db.String(10), nullable=True)
    phone = db.Column(db.String(25), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(25), nullable=False)
    zipcode = db.Column(db.String(15), nullable=False)
    state = db.Column(db.String(5), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    transactions = db.Column(db.String(50), nullable=True)

    # saves = a list of SaveList objects
    # reviews = a list of Review objects

    def __repr__(self):
        return f"<Restaurant name={self.rest_name} id={self.rest_id} Yelp id={self.yelp_id}>"

class Review(db.Model):
    """Restaurant reviews."""

    __tablename__ = "reviews"

    review_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # make yelp_id unique??
    yelp_id = db.Column(db.String(50), db.ForeignKey('restaurants.yelp_id'), nullable=False)
    creator = db.Column(db.String(50), nullable=False)
    prof_pic = db.Column(db.String(250), nullable=True)
    rating = db.Column(db.Float, nullable=False)
    content = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.String(50), nullable=False)

    restaurant = db.relationship("Restaurant", backref="reviews")
    # review.restaurant returns related Restaurant object

    def __repr__(self):
        return f"<Review ID={self.review_id} rating={self.rating}>"

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

    def __repr__(self):
        return f"<Save Item save_id={self.save_id} user_id={self.user_id} rest_id={self.rest_id}>"

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
    connect_to_db(app, echo=False)

    # Call connect_to_db(app, echo=False) to tell SQLAlchemy 
    # not to print out every query it executes.

    connect_to_db(app)