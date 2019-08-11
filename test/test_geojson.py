def test_point():
    "Test point."
    from geojson import Point
    p = Point((-115.81, 37.24))  
    assert p == {"coordinates": [-115.81, 37.24], "type": "Point"}
