"""CRUD operations."""


from model import db, User, Restaurant, SaveList, connect_to_db


def create_user(name, email, pw, zipcode):
    """Create and return a new user."""

    user = User(name=name, email=email, pw=pw, zipcode=zipcode)
    db.session.add(user)
    db.session.commit()

    return user

def create_restaurant(yelp_id, 
                      rest_name, 
                      rating, 
                      review_count, 
                      price, 
                      phone, 
                      address,
                      city,
                      zipcode,
                      state, 
                      img_url, 
                      url):
    """Create and return a new restaurant."""

    restaurant = Restaurant(yelp_id=yelp_id, 
                            rest_name=rest_name,
                            rating=rating,
                            review_count=review_count,
                            price=price,
                            phone=phone,
                            address=address,
                            city=city,
                            zipcode=zipcode,
                            state=state,
                            img_url=img_url,
                            url=url)
    db.session.add(restaurant)
    db.session.commit()

    return restaurant

def create_saved_item(user, restaurant):
    """Create and return a new saved item."""

    saved_item = SaveList(user=user, restaurant=restaurant)
    db.session.add(saved_item)
    db.session.commit()

    return saved_item

def get_users():
    """Return all users."""

    return User.query.all()

def get_user_by_id(user_id):
    """Return a user by their id."""

    return User.query.get(user_id)

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def get_restaurants():
    """Return all restaurants."""

    return Restaurant.query.all()

def get_restaurant_by_id(rest_id):
    """Return a restaurant using the restaurant id."""

    return Restaurant.query.get(rest_id)


if __name__ == '__main__':
    from server import app
    connect_to_db(app)