"use strict";

// Save a restaurant and add it to the user's list of saved restaurants

const saveBtn = $('#save-button');
// const saveList = $('ul');
let restaurantName = $('#restaurant-name').first().html();

function saveRestaurant(restaurantName) {
  alert('Restaurant saved!');
  $('ul').append(`<li>${restaurantName}</li>`);
};

saveBtn.on('click', saveRestaurant);

