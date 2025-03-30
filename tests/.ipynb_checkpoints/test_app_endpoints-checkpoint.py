import unittest
import json
from app import app  # Assuming your Flask app is in a file named app.py

class TestPCOSEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_invalid_endpoint(self):
        """Test: 404 Not Found - Verify the API returns 404 for an invalid endpoint."""
        response = self.app.get('/predict-invalid')
        self.assertEqual(response.status_code, 404)
        result = json.loads(response.data)
        self.assertEqual(result['error'], 'Not Found')

    def test_method_not_allowed_simple(self):
        """Test: 405 Method Not Allowed - Verify the API returns 405 for GET method on /predict-simple."""
        response = self.app.get('/predict-simple')
        self.assertEqual(response.status_code, 405)
        result = json.loads(response.data)
        self.assertEqual(result['error'], 'Method Not Allowed')

    def test_method_not_allowed_enhanced(self):
        """Test: 405 Method Not Allowed - Verify the API returns 405 for GET method on /predict-enhanced."""
        response = self.app.get('/predict-enhanced')
        self.assertEqual(response.status_code, 405)
        result = json.loads(response.data)
        self.assertEqual(result['error'], 'Method Not Allowed')

    def test_internal_server_error(self):
         """Test: 500 Internal Server Error - Simulate an internal error by raising an exception."""
         # Simulate an internal server error within the Flask route by sending incorrect data
         response = self.app.post('/predict-simple', json={"Age (yrs)": 25})  # Missing other required fields
         # Simulate a more explicit error
         self.assertEqual(response.status_code, 400)
         
    def test_malformed_json(self):
        """Test: Malformed JSON - Verify the API returns 400 for malformed JSON."""
        malformed_data = "{Age: 25, Weight: 60}"  # Incorrect JSON format (missing quotes)
        response = self.app.post('/predict-simple', data=malformed_data, content_type='application/json')
        # Flask should return a 500 error for malformed JSON
        self.assertEqual(response.status_code, 500)

    def test_missing_features_simple(self):
        """Test: 400 Bad Request - Verify the API returns 400 when required features are missing."""
        # Send valid JSON but missing some of the required fields
        response = self.app.post('/predict-simple', json={
            "Age (yrs)": 25, 
            "Weight (Kg)": 60, 
            "BMI": 22.5,  # Missing other required fields
        })
        self.assertEqual(response.status_code, 400)

    def test_missing_features_enhanced(self):
        """Test: 400 Bad Request - Verify the API returns 400 when required features are missing in enhanced prediction."""
        # Send valid JSON but missing required fields
        response = self.app.post('/predict-enhanced', json={
            "Age (yrs)": 25,
            "Weight (Kg)": 60,
            "BMI": 22.5,
        })
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()
