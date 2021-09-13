// Foursquare API Info
const clientId = 'ROYPA4F5GI3C4SR45BCG2GBICR0IPRC0EITXDR34YWKFXY0F';
const clientSecret = 'RPAUIIJJWYJW1YWES3S53QCCB2F3TVX5MIGJOI00I2PQC4DB';
const url = 'https://api.foursquare.com/v2/venues/explore?near=';

// OpenWeather Info
const openWeatherKey = 'cadb6ff5525089577f772c01a2e80e7b';
const weatherUrl = 'https://api.openweathermap.org/data/2.5/weather';

// Page Elements
const $input = $('#city');
const $submit = $('#button');
const $destination = $('#destination');
const $container = $('.container');
const $venueDivs = [$("#venue1"), $("#venue2"), $("#venue3"), $("#venue4")];
const $weatherDiv = $("#weather1");
const weekDays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

// Add AJAX functions here:
const getVenues = async () => {
    const city = $input.val();
    const urlToFetch = `${url}${city}&limit=10&client_id=${clientId}&client_secret=${clientSecret}&v=20210814`;
    try {
        const response = await fetch(urlToFetch, {method: 'GET'});
        if (response.ok) {            
            const jsonResponse = await response.json();            
            const venues = jsonResponse.response.groups[0]['items'].map(element => element.venue);
            // console.log(venues);
            return venues;
        };        
    } catch (error) {
        console.log(error.message);
    };    
}

const getForecast = async () => {
    const userInput = $input.val();
    const urlToFetch = `${weatherUrl}?q=${userInput}&APPID=${openWeatherKey}`;
    try {
        const response = await fetch(urlToFetch, {method: 'GET'});
        if (response.ok) {
            const jsonResponse = await response.json();
            // console.log(jsonResponse);
            return jsonResponse;
        };
    } catch(error) {
        console.log(error.message);
    };
}


// Render functions
const renderVenues = (venues) => {
    $venueDivs.forEach(($venue, index) => {
        const venue = venues[index];
        const venueIcon = venue.categories[0].icon;
        const venueImgSrc = `${venueIcon.prefix}bg_64${venueIcon.suffix}`;
        let venueContent = createVenueHTML(venue.name, venue.location, venueImgSrc);
        $venue.append(venueContent);
    });
    $destination.append(`<h2>${venues[0].location.city}</h2>`);
}

const renderForecast = (day) => {
    let weatherContent = createWeatherHTML(day);
    $weatherDiv.append(weatherContent);
}

const executeSearch = () => {
    $venueDivs.forEach(venue => venue.empty());
    $weatherDiv.empty();
    $destination.empty();
    $container.css("visibility", "visible");
    getVenues().then(venues => renderVenues(venues));
    getForecast().then(forecast => renderForecast(forecast));
    return false;
}

$submit.click(executeSearch)