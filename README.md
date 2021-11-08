# Brunchies

Learn more about the developer: https://www.linkedin.com/in/mika-patterson/

## About Brunchies
*Brunchies* is a full-stack business directory web application that serves as a tool for users to locate prime brunch locations in San Francisco.  Users can search for a restaurant by name or filter their search by a restaurant's zipcode, rating, or price and Brunchies will dynamically generate all businesses that match the given filters. The *Yelp Fusion API* was utilized to pull business details and reviews which are displayed on each restaurant's page. Integration of the *Google Maps API* allows users to see saved restaurants pinned to a custom map on the user's profile.

### User Interface
#### Login/Account Creation Modals
*Bootstrap modals to control user flow.*
![Login and create account modals](https://github.com/mknp21/brunchies/blob/1658c5ffd98817fb473f0d7827169ba6e86237b4/static/img/ezgif.com-gif-maker.gif "Modals")

#### Dynamic Search Bar
![Dynamic search bar](https://github.com/mknp21/brunchies/blob/main/static/img/SearchBar.gif "Search Bar") *Javascript and jQuery allowed for creation of a dynamic search bar that filters locations by name, zipcode, rating, or price.*

#### Saved Restaurants
![Saved restaurants](https://github.com/mknp21/brunchies/blob/main/static/img/SavetoMap.gif "Saved Restaurants") *Integration of Google Maps API to allow users to see pins of their saved restaurants.*

### Technology
* Python
* Flask
* Javascript
* jQuery
* AJAX
* JSON
* PostgreSQL
* SQLAlchemy
* Jinja
* HTML
* CSS
* Bootstrap


## Version 2.0
* Incorporate cluster markers to improve load times for a larger number of pins
* Utilize Google's Directions API to allow users to get directions to saved restaurants
* Utilize Twilio's SMS API to allow users to share restaurants with friends