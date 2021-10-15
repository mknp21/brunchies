'use strict';

let map;

function initMap() {
    const sfCoords = {
        lat: 37.601773,
        lng: -122.20287,
    };
    
    map = new google.maps.Map(document.querySelector('#map'), {
        center: sfCoords,
        zoom: 10,
    });

}

