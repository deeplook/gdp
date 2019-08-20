def test():
    "Test."

    import ipyrest
    url = 'http://google.com'
    api = ipyrest.Api(url)
    assert api.url == url
