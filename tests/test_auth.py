def test_logout():
    response = client.post("/logout")

    assert response.status_code == 200

def test_session_cleanup():
    response = client.post("/logout")

    assert response.json()["status"] == "logged_out"