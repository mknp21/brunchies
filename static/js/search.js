const searchBar = document.getElementById('searchBar');
let restaurants = []

searchBar.addEventListener('keyup', (e) => {
    const searchString = e.target.value;

    // want to filter by name, zipcode/distance, rating, and price
    const filtereedRestaurants = restaurants.filter(restaurant => {
        return (
            restaurant.name.contain(searchString) || 
            restaurant.zipcode.contain(searchString) || 
            restaurant.price.contain(searchString));
    });



})