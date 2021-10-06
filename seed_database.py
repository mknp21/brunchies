"""Drop db, create db, and automatically populate db with data."""

import os
import json

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()