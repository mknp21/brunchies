'use strict';

let map;

function initMap() {
    const sfCoords = {
        lat: 37.7749,
        lng: -122.4194,
    };
    
    map = new google.maps.Map(document.querySelector('#map'), {
        center: sfCoords,
        zoom: 12,
    });

    const brunchMarker = new google.maps.Marker({
        position: sfCoords,
        title: 'SF',
        map: map,
    });
}

