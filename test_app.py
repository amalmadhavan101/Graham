import unittest
from app import create_app
import redis

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        # Create a test Flask app and Redis connection
        self.app = create_app().test_client()
        self.redis_db = redis.StrictRedis(host='redis', port=6379, db=0)

    def tearDown(self):
        # Clean up after each test
        self.redis_db.flushdb()

    def test_store_and_retrieve_data(self):
        # Test storing and retrieving data from Redis via Flask app endpoints

        # Store data
        key = 'test_key'
        value = 'test_value'
        response = self.app.post('/store_data', data={'key': key, 'value': value})
        self.assertEqual(response.status_code, 200)

        # Retrieve data
        response = self.app.get(f'/retrieve/{key}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(key, response.json)
        self.assertEqual(response.json[key], value)

    def test_store_missing_data(self):
        # Test storing data with missing key or value

        # Missing key
        response = self.app.post('/store_data', data={'value': 'test_value'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('error', response.json)

        # Missing value
        response = self.app.post('/store_data', data={'key': 'test_key'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('error', response.json)

if __name__ == '__main__':
    unittest.main()
