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

def create_saved_item(user, restaurant):
    """Create and return a new saved item."""

    saved_item = SaveList(user=user, restaurant=restaurant)
    db.session.add(saved_item)
    db.session.commit()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)