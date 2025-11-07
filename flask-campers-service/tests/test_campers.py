from flask import Flask, jsonify
import unittest

class TestCampers(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_get_campers(self):
        response = self.client.get('/api/campers')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_create_camper(self):
        response = self.client.post('/api/campers', json={'name': 'John Doe', 'age': 10})
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)

    def test_update_camper(self):
        response = self.client.put('/api/campers/1', json={'name': 'Jane Doe'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Jane Doe')

    def test_delete_camper(self):
        response = self.client.delete('/api/campers/1')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()