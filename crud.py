"""CRUD operations."""

from model import db, User, Restaurant, SaveList, connect_to_db

def create_user(name, email, pw, zipcode):
    """Create and return a new user."""

    user = User(name=name, email=email, pw=pw, zipcode=zipcode)
    db.session.add(user)
    db.session.commit()

    return user

def create_restaurant(name, category, zipcode, coordinates=None, attributes=None, rating=None):
    """Create and return a new restaurant."""

    restaurant = Restaurant(rest_name=name,
                            category=category,
                            rest_zip=zipcode,
                            coord=coordinates,
                            attributes=attributes,
                            rating=rating)
    db.session.add(restaurant)
    db.session.commit()

    return restaurant

if __name__ == '__main__':
    from server import app
    connect_to_db(app)