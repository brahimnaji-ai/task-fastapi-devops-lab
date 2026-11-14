def test_create_task(client):
    r = client.post("/tasks", json={"title": "Learn DevOps", "description": "CI/CD lab"})
    assert r.status_code == 201
    data = r.json()
    assert data["id"] == 1
    assert data["title"] == "Learn DevOps"
    assert data["done"] is False
def test_create_task_requires_title(client):
    r = client.post("/tasks", json={"description": "no title"})
    assert r.status_code == 422
