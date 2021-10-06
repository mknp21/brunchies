"""Drop db, create db, and automatically populate db with data."""

import os
import json
import requests

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

# Create a user
user = crud.create_user(email, password)

# Create a restaurant

# Create a save item