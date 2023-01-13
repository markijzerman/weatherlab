# FIBER Weather lab
## Open weather data workshop 21-01-2023

In this workshop we will:
- discuss where weather data comes from
- learn how to access this data in different forms
- use open data in your creative practice
- discuss on novel ways of using weather data

Included are various example in Touchdesigner, Max, and Max4Live.

### Live data

During the workshop, there will be a live weather station at A-lab, our location. More information and repository here: https://github.com/markijzerman/weatherStationWebsockets
It offers the data over websockets, JSON as well as a HTML page.

### Open data

Open data examples include Buienradar, Weatherstack, and OpenWeatherMaps. Examples are implemented in Touchdesigner and Max.

### How to use open data

A lot of open data comes in JSON format. Most examples in this repo work with JSON data. Examples of APIs that work with JSON are:
- Buienradar, https://data.buienradar.nl/2.0/feed/json
- Weatherstack, https://api.weatherstack.com/historical?access_key=%3CACCESS-KEY%3E&query=New%20York&historical_date=2015-10-21
- OpenWeatherMaps, https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=<API-KEY>
- ...

Some other are examples of using Slippy Maps, or XYZ Tiles as they're sometimes called. This is a standard by OpenStreetMaps and one can get several different sorts of tilesets. More information can be found here: https://developers.planet.com/docs/planetschool/xyz-tiles-and-slippy-maps/
In TD I have created a .tox (GeoMapObject) to work with these. Some examples are:

- OpenStreetmaps, https://tile.openstreetmap.org/{z}/{x}/{y}.png


- Satellite imagery by Maptiler, https://api.maptiler.com/tiles/satellite-v2/{z}/{x}/{y}.jpg?key=<APIKEY>

- Watercolor-like tiles, http://stamen-tiles-c.a.ssl.fastly.net/watercolor/12/654/1584.jpg

- Precipitation by OpenWeatherMaps, https://tile.openweathermap.org/map/precipitation/X/Y/Z.png?appid=<APIKEY>

More on the tile maps by OWM: https://openweathermap.org/api/weathermaps
