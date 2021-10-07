"""Drop db, create db, and automatically populate db with data."""

import os
import json
import requests

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
params = {'location':'San Francisco', 'categories':'breakfast_brunch'}

res = requests.get(url, params=params, headers=headers)
data = json.loads(res.text)     #  data is a dictionary
businesses = data['businesses']

for business in businesses:
    yelp_id = business['id']

    restaurant = crud.create_restaurant(yelp_id)
    restaurant_ids.append(restaurant)

# Create test users
for n in range(5):
    name = 'First Last'
    email = f'testuser{n}@test.com'
    pw = f'password{n}'
    zipcode = f'5555{n}'

    user = crud.create_user(name, email, pw, zipcode)

    # create a save item
    # user_saved_item = crud.create_saved_item()

