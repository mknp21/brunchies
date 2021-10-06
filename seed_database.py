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

# Create a user
for n in range(5):
    name = 'First Last'
    email = f'testuser{n}@test.com'
    pw = f'password{n}'
    zipcode = f'5555{n}'

    user = crud.create_user(name, email, pw, zipcode)

# Create a restaurant
url = 'https://api.yelp.com/v3/businesses/search'
params = {'location':'Bay Area', 'categories':'breakfast_brunch'}

res = requests.get(url, params=params, headers=headers)
# print(f'The status code is {res.status_code}')

# return json.loads(res.text)
print(json.loads(res.text))
# res.business[id]

# Create a save item