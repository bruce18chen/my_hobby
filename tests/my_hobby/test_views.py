# test_views.py
def test_index_ok(client):
    """
    Test case for the index view when a request is made with the Django test client.
    It verifies that the response status code is 200 (OK).
    """
    # Make a GET request to / and store the response object
    # using the Django test client.
    response = client.get('/')
    # Assert that the status_code is 200 (OK)
    assert response.status_code == 200
