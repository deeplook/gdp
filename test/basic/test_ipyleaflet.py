def test_map():
    "Test map."

    from ipyleaflet import Map

    center = [52.5, 13.4] 
    zoom = 14
    m = Map(center=center, zoom=zoom)
    assert m.center == center
    assert m.zoom == zoom
