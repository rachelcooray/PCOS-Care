# import unittest
# import json
# import time
# from app import app  # Assuming your Flask app is in a file named app.py

# class TestPCOSEndpoints(unittest.TestCase):

#     def setUp(self):
#         self.app = app.test_client()
#         self.app.testing = True

#     # 4. BOUNDARY TESTS
#     def test_edge_case_numerical_data(self):
#         """Test: Verify API handles edge numerical values like 0, 999, negative values."""
#         extreme_values = {
#             "Age (yrs)": -1,  # Negative age (should be rejected)
#             "Weight (Kg)": 999,  # Extremely high weight
#             "BMI": 0,  # Edge case BMI
#             "Pulse rate(bpm)": 200,  # Very high pulse rate
#         }
#         response = self.app.post('/predict-simple', json=extreme_values)
#         self.assertEqual(response.status_code, 400)  # Expecting a validation error

#     def test_edge_case_categorical_data(self):
#         """Test: Verify API handles unexpected categorical values."""
#         invalid_categorical = {
#             "Cycle length(days)": "Unknown",  # Invalid category
#             "Marital Status": "Alien",  # Completely unexpected value
#         }
#         response = self.app.post('/predict-enhanced', json=invalid_categorical)
#         self.assertEqual(response.status_code, 400)  # Expecting a validation error

#     # 6. PERFORMANCE TESTS
#     def test_response_time_valid_prediction(self):
#         """Test: Measure response time for a valid request."""
#         valid_input = {
#             "Age (yrs)": 25,
#             "Weight (Kg)": 60,
#             "BMI": 22.5,
#             "Pulse rate(bpm)": 75,
#         }
#         start_time = time.time()
#         response = self.app.post('/predict-simple', json=valid_input)
#         end_time = time.time()
#         self.assertEqual(response.status_code, 200)
#         self.assertLess(end_time - start_time, 2)  # Ensure it responds within 2 seconds

#     def test_response_time_invalid_input(self):
#         """Test: Measure response time when invalid data is provided."""
#         invalid_input = {"Age (yrs)": "Twenty-five"}  # Invalid format
#         start_time = time.time()
#         response = self.app.post('/predict-simple', json=invalid_input)
#         end_time = time.time()
#         self.assertEqual(response.status_code, 400)
#         self.assertLess(end_time - start_time, 2)  # Should also be quick

#     # 7. MODEL-SPECIFIC TESTS
#     def test_model_compatibility_check(self):
#         """Test: Verify models are loaded and working correctly."""
#         valid_input = {
#             "Age (yrs)": 25,
#             "Weight (Kg)": 60,
#             "BMI": 22.5,
#             "Pulse rate(bpm)": 75,
#         }
#         response = self.app.post('/predict-simple', json=valid_input)
#         self.assertEqual(response.status_code, 200)
#         result = json.loads(response.data)
#         self.assertIn("prediction", result)

#     def test_feature_scaling_consistency(self):
#         """Test: Ensure feature scaling does not distort inputs."""
#         inputs = [
#             {"Age (yrs)": 18, "Weight (Kg)": 45, "BMI": 19.5},
#             {"Age (yrs)": 35, "Weight (Kg)": 80, "BMI": 27.5},
#         ]
#         for data in inputs:
#             response = self.app.post('/predict-simple', json=data)
#             self.assertEqual(response.status_code, 200)
#             self.assertIn("prediction", json.loads(response.data))

#     def test_model_output_verification(self):
#         """Test: Ensure model's output is consistent."""
#         valid_input = {
#             "Age (yrs)": 25,
#             "Weight (Kg)": 60,
#             "BMI": 22.5,
#             "Pulse rate(bpm)": 75,
#         }
#         response1 = self.app.post('/predict-simple', json=valid_input)
#         response2 = self.app.post('/predict-simple', json=valid_input)
#         self.assertEqual(json.loads(response1.data), json.loads(response2.data))  # Predictions should match

#     # 8. MISCELLANEOUS TESTS
#     def test_json_response_structure(self):
#         """Test: Verify API response has expected JSON structure."""
#         valid_input = {
#             "Age (yrs)": 25,
#             "Weight (Kg)": 60,
#             "BMI": 22.5,
#             "Pulse rate(bpm)": 75,
#         }
#         response = self.app.post('/predict-simple', json=valid_input)
#         self.assertEqual(response.status_code, 200)
#         result = json.loads(response.data)
#         self.assertIn("prediction", result)
#         self.assertIsInstance(result["prediction"], int)  # Expecting a 0 or 1

#     def test_empty_request_body(self):
#         """Test: Ensure API returns 400 for empty request body."""
#         response = self.app.post('/predict-simple', data={}, content_type='application/json')
#         self.assertEqual(response.status_code, 400)
#         result = json.loads(response.data)
#         self.assertEqual(result['error'], "Request body is empty")

# if __name__ == "__main__":
#     unittest.main()
