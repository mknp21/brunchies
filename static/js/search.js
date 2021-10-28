const brunchList = document.getElementById('all-restaurants');
const searchBar = document.getElementById('searchBar');
let restaurants = [];

// testing purposes
console.log(restaurants);
console.log('brunchList =', brunchList.children);

// event listener for dynamic search bar
searchBar.addEventListener('keyup', (e) => {
    const searchString = e.target.value.toLowerCase();

    // want to filter by name, zipcode/distance, rating, and price
    const filteredRestaurants = restaurants.filter((restaurant) => {
        return (
            restaurant.name.toLowerCase().includes(searchString) || 
            restaurant.zipcode.includes(searchString) || 
            restaurant.price == searchString);
    });
    console.log('filtered restaurants =', filteredRestaurants);
    displayRestaurants(filteredRestaurants);
});


// grabs restaurant info
const loadRestaurants = () => {
    $.get('/restinfo.json', res => {
    for (const restaurant of JSON.parse(res).results) {
        restaurants.push(restaurant);
    };
    displayRestaurants(restaurants);
});
}
// displays restaurant info
const displayRestaurants = (restaurants) => {
    const htmlString = restaurants
        .map((restaurant) => {
            return `
            <li class="restaurant">
                <h2>${restaurant.name}</h2>
                <p>Price: ${restaurant.price}</p>
                <img src="${restaurant.img}"></img>
            </li>
        `;
        })
        .join('');
    brunchList.innerHTML = htmlString;
};

loadRestaurants();
