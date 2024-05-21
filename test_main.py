import unittest
from fastapi.testclient import TestClient
from main import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_linear_cut_endpoint(self):

        data = {"original_length": 6000, "cut_length": [1500, 1450, 1300, 1150, 1000], "cut_count": [10, 3, 6, 9, 10],
                "blade_thickness": 1,
                "cutting_angle": 45,
                "original_thickness": 25
                }
        response = self.client.post("/linear-cut/", json=data)
        self.assertEqual(response.status_code, 200)
        # Добавьте дополнительные проверки, чтобы убедиться, что результат соответствует ожидаемому

    def test_linear_cut_dynamic_endpoint(self):
        data = {"original_length": 6000, "cut_length": [1500, 1450, 1300, 1150, 1000], "cut_count": [10, 3, 6, 9, 10],
                "blade_thickness": 1,
                "cutting_angle": 45,
                "original_thickness": 25
                }
        response = self.client.post("/linear-cut-dynamic", json=data)
        self.assertEqual(response.status_code, 200)

    def test_linear_cut_multi_endpoint(self):
        data = {"originals_length": [6000, 5000], "cut_length": [1500, 1450, 1300, 1150, 1000], "cut_count": [10, 3, 6, 9, 10],
                "blade_thickness": 1,
                "cutting_angle": 45,
                "original_thickness": 25
                }
        response = self.client.post("/linear-multi-cut", json=data)
        self.assertEqual(response.status_code, 200)

    def test_bivariate_cut_endpoint(self):
        data = {"original_square": 6000, "cut_length": [1500, 1450, 1300, 1150, 1000], "cut_count": [10, 3, 6, 9, 10]}
        response = self.client.post("/bivariate-cut", json=data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()