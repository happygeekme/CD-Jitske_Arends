from main import app

def test_index():
    response = app.test_client().get('/')
    
    assert response.data == b'Hello, world! Hello, world! Het is me gelukt! Nelius en Samuel zijn er ook bij!'
    assert response.status_code == 200