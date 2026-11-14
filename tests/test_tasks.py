# === test 1 ===
def test_create_task(client):
    r = client.post("/api/v1/tasks", json={"title": "Learn DevOps", "description": "CI/CD lab"})
    assert r.status_code == 201
    data = r.json()
    assert data["id"] == 1
    assert data["title"] == "Learn DevOps"
    assert data["done"] is False
def test_create_task_requires_title(client):
    r = client.post("/api/v1/tasks", json={"description": "no title"})
    assert r.status_code == 422

# === test 2 ===
def test_list_tasks_empty(client):
    r = client.get("/api/v1/tasks")
    assert r.status_code == 200
    assert r.json() == []

def test_list_tasks(client):
    client.post("/api/v1/tasks", json={"title": "A"})
    client.post("/api/v1/tasks", json={"title": "B"})
    r = client.get("/api/v1/tasks")
    assert r.status_code == 200
    assert [t["title"] for t in r.json()] == ["A", "B"]

# === test 3 ===
def test_get_task(client):
    created = client.post("/api/v1/tasks", json={"title": "A"}).json()
    r = client.get(f"/api/v1/tasks/{created['id']}")
    assert r.status_code == 200
    assert r.json()["title"] == "A"

def test_get_task_not_found(client):
    r = client.get("/api/v1/tasks/999")
    assert r.status_code == 404

# === test 4 ===
def test_update_task(client):
    created = client.post("/api/v1/tasks", json={"title": "A"}).json()
    r = client.patch(f"/api/v1/tasks/{created['id']}", json={"done": True})
    assert r.status_code == 200
    assert r.json()["done"] is True
    assert r.json()["title"] == "A"
def test_update_task_not_found(client):
    r = client.patch("/api/v1/tasks/999", json={"done": True})
    assert r.status_code == 404

# === test 5 ===
def test_delete_task(client):
    created = client.post("/api/v1/tasks", json={"title": "A"}).json()
    r = client.delete(f"/api/v1/tasks/{created['id']}")
    assert r.status_code == 204
    assert client.get(f"/api/v1/tasks/{created['id']}").status_code == 404

