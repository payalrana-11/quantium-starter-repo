from app import app

def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("#dashboard-header")
    assert header is not None

def test_visualisation_exists(dash_duo):
    dash_duo.start_server(app)
    visualisation = dash_duo.find_element("#sales-graph")
    assert visualisation is not None

def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    region_picker = dash_duo.find_element("#region-filter")
    assert region_picker is not None