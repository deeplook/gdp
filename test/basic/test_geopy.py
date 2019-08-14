def test_geolocation():
    "Test geolocation."
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="test")
    location = geolocator.geocode("175 5th Avenue NYC")
    addr = location.address
    assert addr.startswith('Flatiron Building, 175, 5th Avenue, Flatiron District')
