def test():
    "Test."

    from keplergl import KeplerGl 
    height = 500
    m = KeplerGl(height=height)
    assert m.height == height

    # renders ok in Jupyter classic, but not yet in lab
    # m
