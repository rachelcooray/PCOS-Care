import unittest
import json
from app import app  

class TestPCOSPredictionEnhanced(unittest.TestCase):
    
    def setUp(self):
        """Create a test client for the Flask application."""
        self.app = app.test_client()
        self.app.testing = True

    def test_valid_input(self):
        """Test: Valid Input - Check if /predict-enhanced returns a valid prediction."""
        valid_data = {
            " Age (yrs)": 28,
            "Weight (Kg)": 65.0,
            "Height(Cm) ": 165,
            "BMI": 23.9,
            "Blood Group": 11,
            "Pulse rate(bpm) ": 72,
            "RR (breaths/min)": 18,
            "Hb(g/dl)": 13.5,
            "Cycle(R/I)": 2,
            "Cycle length(days)": 30,
            "Pregnant(Y/N)": 0,
            "No. of aborptions": 0,
            "  I   beta-HCG(mIU/mL)": 1.0,
            "II    beta-HCG(mIU/mL)": 1.2,
            "FSH(mIU/mL)": 6.5,
            "LH(mIU/mL)": 8.0,
            "FSH/LH": 0.81,
            "Hip(inch)": 38,
            "Waist(inch)": 30,
            "Waist:Hip Ratio": 0.79,
            "TSH (mIU/L)": 2.1,
            "AMH(ng/mL)": 3.2,
            "PRL(ng/mL)": 15.0,
            "Vit D3 (ng/mL)": 25.0,
            "PRG(ng/mL)": 0.5,
            "RBS(mg/dl)": 90,
            "Weight gain(Y/N)": 1,
            "hair growth(Y/N)": 1,
            "Skin darkening (Y/N)": 1,
            "Hair loss(Y/N)": 1,
            "Pimples(Y/N)": 1,
            "Fast food (Y/N)": 1,
            "Reg.Exercise(Y/N)": 1,
            "BP _Systolic (mmHg)": 120,
            "BP _Diastolic (mmHg)": 80,
            "Follicle No. (L)": 8,
            "Follicle No. (R)": 10,
            "Avg. F size (L) (mm)": 10.2,
            "Avg. F size (R) (mm)": 11.0,
            "Endometrium (mm)": 8.0
        }
        
        response = self.app.post('/predict-enhanced', json=valid_data)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        self.assertIn('prediction', result)
        self.assertIn(result['prediction'], ['You are likely to have PCOS', 'You are unlikely to have PCOS'])

    def test_missing_numerical_feature(self):
        """Test: Missing Numerical Feature - Returns 400 if a numerical feature is missing."""
        invalid_data = {
            " Age (yrs)": 28,
            "Weight (Kg)": 65.0,
            "Height(Cm) ": 165,
            "BMI": 23.9,
            "Blood Group": 11,
            "Pulse rate(bpm) ": 72,
            "RR (breaths/min)": 18,
            # 'Hb(g/dl)' is missing
            "Cycle(R/I)": 2,
            "Cycle length(days)": 30,
            "Pregnant(Y/N)": 0,
            "No. of aborptions": 0,
            "  I   beta-HCG(mIU/mL)": 1.0,
            "II    beta-HCG(mIU/mL)": 1.2,
            "FSH(mIU/mL)": 6.5,
            "LH(mIU/mL)": 8.0,
            "FSH/LH": 0.81,
            "Hip(inch)": 38,
            "Waist(inch)": 30,
            "Waist:Hip Ratio": 0.79,
            "TSH (mIU/L)": 2.1,
            "AMH(ng/mL)": 3.2,
            "PRL(ng/mL)": 15.0,
            "Vit D3 (ng/mL)": 25.0,
            "PRG(ng/mL)": 0.5,
            "RBS(mg/dl)": 90,
            "Weight gain(Y/N)": 1,
            "hair growth(Y/N)": 1,
            "Skin darkening (Y/N)": 1,
            "Hair loss(Y/N)": 1,
            "Pimples(Y/N)": 1,
            "Fast food (Y/N)": 1,
            "Reg.Exercise(Y/N)": 1,
            "BP _Systolic (mmHg)": 120,
            "BP _Diastolic (mmHg)": 80,
            "Follicle No. (L)": 8,
            "Follicle No. (R)": 10,
            "Avg. F size (L) (mm)": 10.2,
            "Avg. F size (R) (mm)": 11.0,
            "Endometrium (mm)": 8.0
        }
        
        response = self.app.post('/predict-enhanced', json=invalid_data)
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertIn("Missing feature:", result["error"])

    def test_missing_categorical_feature(self):
        """Test: Missing Categorical Feature - Returns 400 if a categorical feature is missing."""
        invalid_data = {
            " Age (yrs)": 28,
            "Weight (Kg)": 65.0,
            "Height(Cm) ": 165,
            "BMI": 23.9,
            "Blood Group": 11,
            "Pulse rate(bpm) ": 72,
            "RR (breaths/min)": 18,
            "Hb(g/dl)": 13.5,
            "Cycle(R/I)": 2,
            "Cycle length(days)": 30,
            # 'Pregnant(Y/N)' is missing
            "No. of aborptions": 0,
            "  I   beta-HCG(mIU/mL)": 1.0,
            "II    beta-HCG(mIU/mL)": 1.2,
            "FSH(mIU/mL)": 6.5,
            "LH(mIU/mL)": 8.0,
            "FSH/LH": 0.81,
            "Hip(inch)": 38,
            "Waist(inch)": 30,
            "Waist:Hip Ratio": 0.79,
            "TSH (mIU/L)": 2.1,
            "AMH(ng/mL)": 3.2,
            "PRL(ng/mL)": 15.0,
            "Vit D3 (ng/mL)": 25.0,
            "PRG(ng/mL)": 0.5,
            "RBS(mg/dl)": 90,
            "Weight gain(Y/N)": 1,
            "hair growth(Y/N)": 1,
            "Skin darkening (Y/N)": 1,
            "Hair loss(Y/N)": 1,
            "Pimples(Y/N)": 1,
            "Fast food (Y/N)": 1,
            "Reg.Exercise(Y/N)": 1,
            "BP _Systolic (mmHg)": 120,
            "BP _Diastolic (mmHg)": 80,
            "Follicle No. (L)": 8,
            "Follicle No. (R)": 10,
            "Avg. F size (L) (mm)": 10.2,
            "Avg. F size (R) (mm)": 11.0,
            "Endometrium (mm)": 8.0
        }
        
        response = self.app.post('/predict-enhanced', json=invalid_data)
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertIn("Missing feature:", result["error"])

    def test_invalid_media_type(self):
        """Test: Invalid Media Type (Non-JSON Request) - Returns 415 error."""
        invalid_data = "Invalid data, should be JSON"
        
        response = self.app.post('/predict-enhanced', data=invalid_data, content_type='text/plain')
        self.assertEqual(response.status_code, 415)
        result = json.loads(response.data)
        self.assertEqual(result["error"], "Unsupported Media Type. Only JSON requests are allowed.")

    def test_incomplete_numerical_data(self):
        """Test: Incomplete Numerical Data - Returns 400 error with a missing value."""
        incomplete_data = {
            " Age (yrs)": 28,
            "Weight (Kg)": 65.0,
            "Height(Cm) ": 165,
            "BMI": 23.9,
            "Blood Group": 11,
            "Pulse rate(bpm) ": 72,
            "RR (breaths/min)": 18,
            "Hb(g/dl)": 13.5,
            "Cycle(R/I)": 2,
            "Cycle length(days)": 30,
            "Pregnant(Y/N)": 0,
            "No. of aborptions": 0,
            # Numerical fields like 'Hip(inch)' are missing
            "Waist(inch)": 30,
            "Waist:Hip Ratio": 0.79,
            "TSH (mIU/L)": 2.1,
            "AMH(ng/mL)": 3.2,
            "PRL(ng/mL)": 15.0,
            "Vit D3 (ng/mL)": 25.0,
            "PRG(ng/mL)": 0.5,
            "RBS(mg/dl)": 90,
            "Weight gain(Y/N)": 1,
            "hair growth(Y/N)": 1,
            "Skin darkening (Y/N)": 1,
            "Hair loss(Y/N)": 1,
            "Pimples(Y/N)": 1,
            "Fast food (Y/N)": 1,
            "Reg.Exercise(Y/N)": 1,
            "BP _Systolic (mmHg)": 120,
            "BP _Diastolic (mmHg)": 80,
            "Follicle No. (L)": 8,
            "Follicle No. (R)": 10,
            "Avg. F size (L) (mm)": 10.2,
            "Avg. F size (R) (mm)": 11.0,
            "Endometrium (mm)": 8.0
        }
        
        response = self.app.post('/predict-enhanced', json=incomplete_data)
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertIn("Missing feature:", result["error"])

    def test_incomplete_categorical_data(self):
        """Test: Incomplete Categorical Data - Returns 400 error with a missing value."""
        incomplete_data = {
            " Age (yrs)": 28,
            "Weight (Kg)": 65.0,
            "Height(Cm) ": 165,
            "BMI": 23.9,
            "Blood Group": 11,
            "Pulse rate(bpm) ": 72,
            "RR (breaths/min)": 18,
            "Hb(g/dl)": 13.5,
            "Cycle(R/I)": 2,
            "Cycle length(days)": 30,
            "Pregnant(Y/N)": 0,
            "No. of aborptions": 0,
            "  I   beta-HCG(mIU/mL)": 1.0,
            "II    beta-HCG(mIU/mL)": 1.2,
            "FSH(mIU/mL)": 6.5,
            "LH(mIU/mL)": 8.0,
            "FSH/LH": 0.81,
            "Hip(inch)": 38,
            "Waist(inch)": 30,
            "Waist:Hip Ratio": 0.79,
            "TSH (mIU/L)": 2.1,
            "AMH(ng/mL)": 3.2,
            "PRL(ng/mL)": 15.0,
            "Vit D3 (ng/mL)": 25.0,
            "PRG(ng/mL)": 0.5,
            "RBS(mg/dl)": 90,
            # Missing 'Weight gain(Y/N)'
            "hair growth(Y/N)": 1,
            "Skin darkening (Y/N)": 1,
            "Hair loss(Y/N)": 1,
            "Pimples(Y/N)": 1,
            "Fast food (Y/N)": 1,
            "Reg.Exercise(Y/N)": 1,
            "BP _Systolic (mmHg)": 120,
            "BP _Diastolic (mmHg)": 80,
            "Follicle No. (L)": 8,
            "Follicle No. (R)": 10,
            "Avg. F size (L) (mm)": 10.2,
            "Avg. F size (R) (mm)": 11.0,
            "Endometrium (mm)": 8.0
        }

        response = self.app.post('/predict-enhanced', json=incomplete_data)
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertIn("Missing feature:", result["error"])

    def test_model_prediction(self):
        """Test: Model Prediction - Check if the prediction is within expected outcomes."""
        valid_data = {
            " Age (yrs)": 28,
            "Weight (Kg)": 65.0,
            "Height(Cm) ": 165,
            "BMI": 23.9,
            "Blood Group": 11,
            "Pulse rate(bpm) ": 72,
            "RR (breaths/min)": 18,
            "Hb(g/dl)": 13.5,
            "Cycle(R/I)": 2,
            "Cycle length(days)": 30,
            "Pregnant(Y/N)": 0,
            "No. of aborptions": 0,
            "  I   beta-HCG(mIU/mL)": 1.0,
            "II    beta-HCG(mIU/mL)": 1.2,
            "FSH(mIU/mL)": 6.5,
            "LH(mIU/mL)": 8.0,
            "FSH/LH": 0.81,
            "Hip(inch)": 38,
            "Waist(inch)": 30,
            "Waist:Hip Ratio": 0.79,
            "TSH (mIU/L)": 2.1,
            "AMH(ng/mL)": 3.2,
            "PRL(ng/mL)": 15.0,
            "Vit D3 (ng/mL)": 25.0,
            "PRG(ng/mL)": 0.5,
            "RBS(mg/dl)": 90,
            "Weight gain(Y/N)": 1,
            "hair growth(Y/N)": 1,
            "Skin darkening (Y/N)": 1,
            "Hair loss(Y/N)": 1,
            "Pimples(Y/N)": 1,
            "Fast food (Y/N)": 1,
            "Reg.Exercise(Y/N)": 1,
            "BP _Systolic (mmHg)": 120,
            "BP _Diastolic (mmHg)": 80,
            "Follicle No. (L)": 8,
            "Follicle No. (R)": 10,
            "Avg. F size (L) (mm)": 10.2,
            "Avg. F size (R) (mm)": 11.0,
            "Endometrium (mm)": 8.0
        }
        
        response = self.app.post('/predict-enhanced', json=valid_data)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        self.assertIn(result['prediction'], ['You are likely to have PCOS', 'You are unlikely to have PCOS'])

if __name__ == '__main__':
    unittest.main()
