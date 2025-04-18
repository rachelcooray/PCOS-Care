import unittest
import json
import time
from app import app  

class TestPCOSOther(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # BOUNDARY TESTS
    def test_edge_case_numerical_data(self):
        """Test: Verify API handles edge numerical values like 0, 999, negative values."""
        extreme_values = {
            "Age (yrs)": -1,  # Negative age (should be rejected)
            "Weight (Kg)": 999,  # Extremely high weight
            "BMI": 0,  # Edge case BMI
            "Pulse rate(bpm)": 200,  # Very high pulse rate
        }
        response = self.app.post('/predict-simple', json=extreme_values)
        self.assertEqual(response.status_code, 400)  # Expecting a validation error

    def test_edge_case_categorical_data(self):
        """Test: Verify API handles unexpected categorical values."""
        invalid_categorical = {
            "Cycle length(days)": "Unknown",  # Invalid category
            "Marital Status": "Alien",  # Completely unexpected value
        }
        response = self.app.post('/predict-enhanced', json=invalid_categorical)
        self.assertEqual(response.status_code, 400)  # Expecting a validation error

    # PERFORMANCE TESTS
    def test_response_time_valid_prediction(self):
        """Test: Measure response time for a valid request."""
        valid_input = {
            ' Age (yrs)': 25,
            'Weight (Kg)': 60,
            'Height(Cm) ': 160,
            'BMI': 23.4,
            'Blood Group': 11,
            'Pulse rate(bpm) ': 72,
            'RR (breaths/min)': 16,
            'Cycle(R/I)': 2,
            'Cycle length(days)': 30,
            'Pregnant(Y/N)': 0,
            'No. of aborptions': 0,
            'Hip(inch)': 36,
            'Waist(inch)': 28,
            'Waist:Hip Ratio': 0.78,
            'Weight gain(Y/N)': 0,
            'hair growth(Y/N)': 0,
            'Skin darkening (Y/N)': 0,
            'Hair loss(Y/N)': 0,
            'Pimples(Y/N)': 0,
            'Fast food (Y/N)': 1,
            'Reg.Exercise(Y/N)': 1,
            'BP _Systolic (mmHg)': 120,
            'BP _Diastolic (mmHg)': 80
        }
        start_time = time.time()
        response = self.app.post('/predict-simple', json=valid_input)
        end_time = time.time()
        self.assertEqual(response.status_code, 200)
        self.assertLess(end_time - start_time, 2)  # Ensure it responds within 2 seconds

    def test_response_time_invalid_input(self):
        """Test: Measure response time when invalid data is provided."""
        invalid_input = {"Age (yrs)": "Twenty-five"}  # Invalid format
        start_time = time.time()
        response = self.app.post('/predict-simple', json=invalid_input)
        end_time = time.time()
        self.assertEqual(response.status_code, 400)
        self.assertLess(end_time - start_time, 2)  # Should also be quick

    # 7. MODEL-SPECIFIC TESTS
    def test_model_compatibility_check(self):
        """Test: Verify models are loaded and working correctly."""
        valid_input = {
            ' Age (yrs)': 25,
            'Weight (Kg)': 60,
            'Height(Cm) ': 160,
            'BMI': 23.4,
            'Blood Group': 11,
            'Pulse rate(bpm) ': 72,
            'RR (breaths/min)': 16,
            'Cycle(R/I)': 2,
            'Cycle length(days)': 30,
            'Pregnant(Y/N)': 0,
            'No. of aborptions': 0,
            'Hip(inch)': 36,
            'Waist(inch)': 28,
            'Waist:Hip Ratio': 0.78,
            'Weight gain(Y/N)': 0,
            'hair growth(Y/N)': 0,
            'Skin darkening (Y/N)': 0,
            'Hair loss(Y/N)': 0,
            'Pimples(Y/N)': 0,
            'Fast food (Y/N)': 1,
            'Reg.Exercise(Y/N)': 1,
            'BP _Systolic (mmHg)': 120,
            'BP _Diastolic (mmHg)': 80
        }
        response = self.app.post('/predict-simple', json=valid_input)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        self.assertIn("prediction", result)

    def test_model_compatibility_check_enhanced(self):
        """Test: Verify models are loaded and working correctly."""
        valid_input = {
            ' Age (yrs)': 25,
            'Weight (Kg)': 60,
            'Height(Cm) ': 160,
            'BMI': 23.4,
            'Blood Group': 11,
            'Pulse rate(bpm) ': 72,
            'RR (breaths/min)': 16,
            'Cycle(R/I)': 2,
            'Cycle length(days)': 30,
            'Pregnant(Y/N)': 0,
            'No. of aborptions': 0,
            'Hip(inch)': 36,
            'Waist(inch)': 28,
            'Waist:Hip Ratio': 0.78,
            'Weight gain(Y/N)': 0,
            'hair growth(Y/N)': 0,
            'Skin darkening (Y/N)': 0,
            'Hair loss(Y/N)': 0,
            'Pimples(Y/N)': 0,
            'Fast food (Y/N)': 1,
            'Reg.Exercise(Y/N)': 1,
            'BP _Systolic (mmHg)': 120,
            'BP _Diastolic (mmHg)': 80
        }
        response = self.app.post('/predict-enhanced', json=valid_input)
        # Expecting 400 because the request is missing required features
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        # Check that the response contains an error message instead of a prediction
        self.assertIn("error", result)
        self.assertIn("Missing feature", result["error"])


    def test_model_output_verification(self):
        """Test: Ensure model's output is consistent."""
        valid_input = {
            ' Age (yrs)': 25,
            'Weight (Kg)': 60,
            'Height(Cm) ': 160,
            'BMI': 23.4,
            'Blood Group': 11,
            'Pulse rate(bpm) ': 72,
            'RR (breaths/min)': 16,
            'Cycle(R/I)': 2,
            'Cycle length(days)': 30,
            'Pregnant(Y/N)': 0,
            'No. of aborptions': 0,
            'Hip(inch)': 36,
            'Waist(inch)': 28,
            'Waist:Hip Ratio': 0.78,
            'Weight gain(Y/N)': 0,
            'hair growth(Y/N)': 0,
            'Skin darkening (Y/N)': 0,
            'Hair loss(Y/N)': 0,
            'Pimples(Y/N)': 0,
            'Fast food (Y/N)': 1,
            'Reg.Exercise(Y/N)': 1,
            'BP _Systolic (mmHg)': 120,
            'BP _Diastolic (mmHg)': 80
        }
        response1 = self.app.post('/predict-simple', json=valid_input)
        response2 = self.app.post('/predict-simple', json=valid_input)
        self.assertEqual(json.loads(response1.data), json.loads(response2.data))  # Predictions should match

if __name__ == "__main__":
    unittest.main()
