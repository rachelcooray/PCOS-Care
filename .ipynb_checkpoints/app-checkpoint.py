from flask import Flask, request, jsonify
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging to save messages to 'app.log'
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') 

# Load pre-trained models 
try:
    with open("best_logistic_reg_simple_smote.pkl", "rb") as model_file:
        loaded_simple = pickle.load(model_file) # Model for Simple risk
    with open("best_logistic_reg_enhanced_smote.pkl", "rb") as model_file:
        loaded_enhanced = pickle.load(model_file) # Model for Enhanced risk
    logging.info("Models loaded successfully.")
except Exception as e:
    logging.error(f"Error loading models: {e}")
    loaded_simple = None
    loaded_enhanced = None


# Features lists
features_general_public = [
    ' Age (yrs)', 'Weight (Kg)', 'Height(Cm) ', 'BMI', 'Blood Group', 'Pulse rate(bpm) ', 
    'RR (breaths/min)', 'Cycle(R/I)', 'Cycle length(days)', 
    'Pregnant(Y/N)', 'No. of aborptions', 'Hip(inch)', 'Waist(inch)', 'Waist:Hip Ratio',  
    'Weight gain(Y/N)', 'hair growth(Y/N)', 'Skin darkening (Y/N)', 'Hair loss(Y/N)', 
    'Pimples(Y/N)', 'Fast food (Y/N)', 'Reg.Exercise(Y/N)', 'BP _Systolic (mmHg)', 
    'BP _Diastolic (mmHg)'
]

features_scan = [
    ' Age (yrs)', 'Weight (Kg)', 'Height(Cm) ', 'BMI',
       'Blood Group', 'Pulse rate(bpm) ', 'RR (breaths/min)', 'Hb(g/dl)',
       'Cycle(R/I)', 'Cycle length(days)',
       'Pregnant(Y/N)', 'No. of aborptions', '  I   beta-HCG(mIU/mL)',
       'II    beta-HCG(mIU/mL)', 'FSH(mIU/mL)', 'LH(mIU/mL)', 'FSH/LH',
       'Hip(inch)', 'Waist(inch)', 'Waist:Hip Ratio', 'TSH (mIU/L)',
       'AMH(ng/mL)', 'PRL(ng/mL)', 'Vit D3 (ng/mL)', 'PRG(ng/mL)',
       'RBS(mg/dl)', 'Weight gain(Y/N)', 'hair growth(Y/N)',
       'Skin darkening (Y/N)', 'Hair loss(Y/N)', 'Pimples(Y/N)',
       'Fast food (Y/N)', 'Reg.Exercise(Y/N)', 'BP _Systolic (mmHg)',
       'BP _Diastolic (mmHg)', 'Follicle No. (L)', 'Follicle No. (R)',
       'Avg. F size (L) (mm)', 'Avg. F size (R) (mm)', 'Endometrium (mm)'
]

# Separate numerical and categorical columns
numerical_columns_gen = [
    ' Age (yrs)', 'Weight (Kg)', 'Height(Cm) ', 'BMI', 'Pulse rate(bpm) ', 
    'RR (breaths/min)', 'Cycle(R/I)', 'Cycle length(days)', 
    'No. of aborptions', 'Hip(inch)', 'Waist(inch)', 'Waist:Hip Ratio', 
    'BP _Systolic (mmHg)', 'BP _Diastolic (mmHg)'
]

categorical_columns_gen = [
    'Blood Group', 'Pregnant(Y/N)', 'Weight gain(Y/N)', 'hair growth(Y/N)', 'Skin darkening (Y/N)', 
    'Hair loss(Y/N)', 'Pimples(Y/N)', 'Fast food (Y/N)', 'Reg.Exercise(Y/N)'
]

numerical_columns_scan = [
    ' Age (yrs)', 'Weight (Kg)', 'Height(Cm) ', 'BMI', 'Pulse rate(bpm) ', 
    'RR (breaths/min)', 'Hb(g/dl)', 'Cycle(R/I)', 'Cycle length(days)', 
    'No. of aborptions', 
    '  I   beta-HCG(mIU/mL)', 'II    beta-HCG(mIU/mL)', 'FSH(mIU/mL)', 'LH(mIU/mL)', 
    'FSH/LH', 'Hip(inch)', 'Waist(inch)', 'Waist:Hip Ratio', 'TSH (mIU/L)', 
    'AMH(ng/mL)', 'PRL(ng/mL)', 'Vit D3 (ng/mL)', 'PRG(ng/mL)', 'RBS(mg/dl)', 
    'BP _Systolic (mmHg)', 'BP _Diastolic (mmHg)', 'Follicle No. (L)', 
    'Follicle No. (R)', 'Avg. F size (L) (mm)', 'Avg. F size (R) (mm)', 'Endometrium (mm)'
]

categorical_columns_scan = [
    'Blood Group', 'Pregnant(Y/N)', 'Weight gain(Y/N)', 'hair growth(Y/N)', 'Skin darkening (Y/N)', 
    'Hair loss(Y/N)', 'Pimples(Y/N)', 'Fast food (Y/N)', 'Reg.Exercise(Y/N)'
]

# ----- ROUTES -----
# Endpoint for simple prediction
@app.route("/predict-simple", methods=["POST"])
def predict_simple():
    try:
        # Ensure incoming request is JSON
        if not request.is_json:
            return jsonify({"error": "Unsupported Media Type. Only JSON requests are allowed."}), 415
        
        data = request.json
        logging.debug(f"Received data: {data}")

        # Get user input for numerical columns
        user_inputs = []
        for col in numerical_columns_gen:
            if col in data:
                user_inputs.append(data[col])
            else:
                logging.error(f"Missing numerical feature: {col}")
                return jsonify({"error": f"Missing feature: {col}"}), 400

        # Convert to DataFrame and scale
        numerical_inputs_df = pd.DataFrame([user_inputs], columns=numerical_columns_gen)
        scaler = StandardScaler()
        scaled_numerical_inputs = scaler.fit_transform(numerical_inputs_df)

        # Get user input for categorical columns and append them
        categorical_inputs = []
        for col in categorical_columns_gen:
            if col in data:
                categorical_inputs.append(data[col])
            else:
                logging.error(f"Missing categorical feature: {col}")
                return jsonify({"error": f"Missing feature: {col}"}), 400

        # Combine scaled numerical inputs and categorical inputs 
        final_inputs = pd.DataFrame(scaled_numerical_inputs, columns=numerical_columns_gen)
        final_inputs[categorical_columns_gen] = categorical_inputs

        # Reorder columns to match model expectations
        final_inputs = final_inputs[features_general_public]

        # Make prediction using the trained Logistic Regression model
        prediction = loaded_simple.predict(final_inputs)

        # Return the prediction result
        result = "You are likely to have PCOS" if prediction[0] == 1 else "You are unlikely to have PCOS"
        return jsonify({"prediction": result})

    except ValueError as e:
        return jsonify({"error": "Bad Request", "message": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500


# Endpoint for enhanced prediction
@app.route("/predict-enhanced", methods=["POST"])
def predict_enhanced():
    try:
        # Ensure incoming request is JSON
        if not request.is_json:
            return jsonify({"error": "Unsupported Media Type. Only JSON requests are allowed."}), 415
        
        data = request.json
        logging.debug(f"Received data: {data}")

        # Get user input for numerical columns
        user_inputs = []
        for col in numerical_columns_scan:
            if col in data:
                user_inputs.append(data[col])
            else:
                logging.error(f"Missing numerical feature: {col}")
                return jsonify({"error": f"Missing feature: {col}"}), 400

        # Convert to DataFrame and scale
        numerical_inputs_df = pd.DataFrame([user_inputs], columns=numerical_columns_scan)
        scaler = StandardScaler()
        scaled_numerical_inputs = scaler.fit_transform(numerical_inputs_df)

        # Get user input for categorical columns and append them
        categorical_inputs = []
        for col in categorical_columns_scan:
            if col in data:
                categorical_inputs.append(data[col])
            else:
                logging.error(f"Missing categorical feature: {col}")
                return jsonify({"error": f"Missing feature: {col}"}), 400

        # Combine scaled numerical inputs and categorical inputs 
        final_inputs = pd.DataFrame(scaled_numerical_inputs, columns=numerical_columns_scan)
        final_inputs[categorical_columns_scan] = categorical_inputs

        final_inputs = final_inputs[features_scan]

        # Make prediction using the trained Logistic Regression model
        prediction = loaded_enhanced.predict(final_inputs)

        result = "You are likely to have PCOS" if prediction[0] == 1 else "You are unlikely to have PCOS"
        return jsonify({"prediction": result})

    except ValueError as e:
        return jsonify({"error": "Bad Request", "message": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500


# Error Handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"error": "Method Not Allowed"}), 405
    
# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)


# Reference: Flask error handling docs - https://flask.palletsprojects.com/en/stable/errorhandling/
