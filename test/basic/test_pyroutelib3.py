def test_routing():
    "Test routing."

    import pyroutelib3
    
    router = pyroutelib3.Router('car')
    start = router.findNode(52.523427, 13.413677) # Alex
    end = router.findNode(52.516121, 13.38003) # Adlon

    status, route = router.doRoute(start, start)
    assert (status, route) == ('no_route', [])

    # status, route = router.doRoute(start, end) # Find the route - a list of OSM nodes
    # assert status == 'success'
    # routeLatLons = list(map(router.nodeLatLon, route)) # Get actual route coordinates
