import unittest
import json
from app import app  # Assuming your Flask app is in a file named app.py

class TestPCOSPredictionSimple(unittest.TestCase):
    
    def setUp(self):
        """Create a test client for the Flask application."""
        self.app = app.test_client()
        self.app.testing = True

    def test_valid_input(self):
        """Test: Valid Input - Check if /predict-simple returns a valid prediction."""
        valid_data = {
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
        
        response = self.app.post('/predict-simple', json=valid_data)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        self.assertIn('prediction', result)
        self.assertIn(result['prediction'], ['You are likely to have PCOS', 'You are unlikely to have PCOS'])

    def test_missing_numerical_feature(self):
        """Test: Missing Numerical Feature - Returns 400 if a numerical feature is missing."""
        invalid_data = {
            ' Age (yrs)': 25,
            'Weight (Kg)': 60,
            'Height(Cm) ': 160,
            # 'BMI' is missing
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
        
        response = self.app.post('/predict-simple', json=invalid_data)
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertIn("Missing feature:", result["error"])

    def test_missing_categorical_feature(self):
        """Test: Missing Categorical Feature - Returns 400 if a categorical feature is missing."""
        invalid_data = {
            ' Age (yrs)': 25,
            'Weight (Kg)': 60,
            'Height(Cm) ': 160,
            'BMI': 23.4,
            'Blood Group': 11,
            'Pulse rate(bpm) ': 72,
            'RR (breaths/min)': 16,
            'Cycle(R/I)': 2,
            'Cycle length(days)': 30,
            # 'Pregnant(Y/N)' is missing
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
        
        response = self.app.post('/predict-simple', json=invalid_data)
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertIn("Missing feature:", result["error"])

    def test_invalid_media_type(self):
        """Test: Invalid Media Type (Non-JSON Request) - Returns 415 error."""
        invalid_data = "Invalid data, should be JSON"
        
        response = self.app.post('/predict-simple', data=invalid_data, content_type='text/plain')
        self.assertEqual(response.status_code, 415)
        result = json.loads(response.data)
        self.assertEqual(result["error"], "Unsupported Media Type. Only JSON requests are allowed.")

    def test_incomplete_numerical_data(self):
        """Test: Incomplete Numerical Data - Returns 400 error with a missing value."""
        incomplete_data = {
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
            # Numerical fields like 'Hip(inch)' are missing
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
            
        
        response = self.app.post('/predict-simple', json=incomplete_data)
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertIn("Missing feature:", result["error"])

    def test_incomplete_categorical_data(self):
        """Test: Incomplete Categorical Data - Returns 400 error with a missing value."""
        incomplete_data = {
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
            # Missing 'hair growth(Y/N)'
            'Skin darkening (Y/N)': 0,
            'Hair loss(Y/N)': 0,
            'Pimples(Y/N)': 0,
            'Fast food (Y/N)': 1,
            'Reg.Exercise(Y/N)': 1,
            'BP _Systolic (mmHg)': 120,
        }

        response = self.app.post('/predict-simple', json=incomplete_data)
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertIn("Missing feature:", result["error"])

    def test_model_prediction(self):
        """Test: Model Prediction - Check if the prediction is within expected outcomes."""
        valid_data = {
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
        
        response = self.app.post('/predict-simple', json=valid_data)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        self.assertIn(result['prediction'], ['You are likely to have PCOS', 'You are unlikely to have PCOS'])

if __name__ == '__main__':
    unittest.main()
