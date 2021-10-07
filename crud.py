"""CRUD operations."""


from model import db, User, Restaurant, SaveList, connect_to_db


def create_user(name, email, pw, zipcode):
    """Create and return a new user."""

    user = User(name=name, email=email, pw=pw, zipcode=zipcode)
    db.session.add(user)
    db.session.commit()

    return user

def create_restaurant(yelp_id):
    """Create and return a new restaurant."""

    restaurant = Restaurant(yelp_id=yelp_id)
    db.session.add(restaurant)
    db.session.commit()

    return restaurant

def create_saved_item(user_id, rest_id):
    """Create and return a new saved item."""

    saved_item = SaveList(user_id=user_id, rest_id=rest_id)
    db.session.add(saved_item)
    db.session.commit()

def get_users():
    """Return all users."""

    return User.query.all()

def get_user_by_id():
    """Return a user using their user id."""

    return User.query.get(user_id).one()

def get_user_by_email(email):
    """Return user email"""

    return User.query.filter(User.email == email).one()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)