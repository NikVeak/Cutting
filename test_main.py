
import unittest
from fastapi.testclient import TestClient
from main import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_test_linear_endpoint(self):
        response = self.client.get("/test_linear")
        self.assertEqual(response.status_code, 200)
        # Добавьте дополнительные проверки, чтобы убедиться, что результат соответствует ожидаемому

    def test_linear_cut_endpoint(self):
        data = {"original_length": 6000, "cut_length": [1500, 1450, 1300, 1150, 1000], "cut_count": [10, 3, 6, 9, 10]}
        response = self.client.post("/linear-cut/", json=data)
        self.assertEqual(response.status_code, 200)
        # Добавьте дополнительные проверки, чтобы убедиться, что результат соответствует ожидаемому

if __name__ == '__main__':
    unittest.main()