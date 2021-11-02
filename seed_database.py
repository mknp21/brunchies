"""Drop db, create db, and automatically populate db with data."""

import os
import json
import requests

from random import choice

import crud
import model
import server

API_KEY = os.environ['YELP_KEY']
headers = {'Authorization': 'Bearer %s' % API_KEY}

os.system('dropdb brunch')
os.system('createdb brunch')

model.connect_to_db(server.app)
model.db.create_all()

# Retrieve business info from Yelp API and add business id to db
url = 'https://api.yelp.com/v3/businesses/search' 
params = {'location':'San Francisco', 'categories':'breakfast_brunch', 'limit':50}

res = requests.get(url, params=params, headers=headers)
data = json.loads(res.text)     #  data is a dictionary
# print(data)
businesses = data['businesses']

restaurants = []
# yelp_ids = []

for business in businesses:
    yelp_id = business['id']
    # yelp_ids.append(yelp_id)

    rest_name = business['name']
    rating = business['rating']
    review_count = business['review_count']
    price = business['price']
    phone = business['phone']
    address = business['location']['address1']
    city = business['location']['city']
    zipcode = business['location']['zip_code']
    state = business['location']['state']
    latitude = business['coordinates']['latitude']
    longitude = business['coordinates']['longitude']
    img_url = business['image_url']
    url = business['url']
    transactions = business['transactions']

    restaurant = crud.create_restaurant(yelp_id, 
                                        rest_name, 
                                        rating, 
                                        review_count, 
                                        price, 
                                        phone, 
                                        address,
                                        city,
                                        zipcode,
                                        state,
                                        latitude,
                                        longitude, 
                                        img_url, 
                                        url,
                                        transactions)
    restaurants.append(restaurant)

# Create reviews table
# for yelp_id in yelp_ids:
    reviews_url = f"https://api.yelp.com/v3/businesses/{yelp_id}/reviews"
    reviews_res = requests.get(reviews_url, headers=headers)
    data = json.loads(reviews_res.text)
    reviews = data['reviews']

    for review in reviews:
        creator = review['user']['name']
        prof_pic = review['user']['image_url']
        rating = review['rating']
        content = review['text']
        date_created = review['time_created']

        review = crud.create_review(yelp_id,
                                    creator,
                                    prof_pic,
                                    rating,
                                    content,
                                    date_created)

# Create test users
for n in range(10):
    name = 'First Last'
    email = f'testuser{n}@test.com'
    pw = f'password{n}'
    zipcode = f'5555{n}'

    user = crud.create_user(name, email, pw, zipcode)

    # create a save item
    for n in range(10):
        random_restaurant = choice(restaurants)
        user_saved_item = crud.create_saved_item(user, random_restaurant)


