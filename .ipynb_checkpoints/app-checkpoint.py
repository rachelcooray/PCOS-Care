from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained SVM model and scaler
with open("best_svm_model.pkl", "rb") as model_file:
    loaded_svm = pickle.load(model_file)

with open("scaler_svm.pkl", "rb") as scaler_file:
    loaded_scaler_svm = pickle.load(scaler_file)

# Load the trained Random Forest model and scaler
with open("best_random_forest_model.pkl", "rb") as model_file:
    loaded_random_forest = pickle.load(model_file)

with open("scaler_random_forest.pkl", "rb") as scaler_file:
    loaded_scaler_rf = pickle.load(scaler_file)

# Features
features_general_public = [
    ' Age (yrs)', 'Weight (Kg)', 'Height(Cm) ', 'BMI', 'Blood Group', 'Pulse rate(bpm) ', 
    'RR (breaths/min)', 'Cycle(R/I)', 'Cycle length(days)', 'Marraige Status (Yrs)', 
    'Pregnant(Y/N)', 'No. of aborptions', 'Hip(inch)', 'Waist(inch)', 'Waist:Hip Ratio',  
    'Weight gain(Y/N)', 'hair growth(Y/N)', 'Skin darkening (Y/N)', 'Hair loss(Y/N)', 
    'Pimples(Y/N)', 'Fast food (Y/N)', 'Reg.Exercise(Y/N)', 'BP _Systolic (mmHg)', 
    'BP _Diastolic (mmHg)'
]

features_scan = [
    ' Age (yrs)', 'Weight (Kg)', 'Height(Cm) ', 'BMI',
       'Blood Group', 'Pulse rate(bpm) ', 'RR (breaths/min)', 'Hb(g/dl)',
       'Cycle(R/I)', 'Cycle length(days)', 'Marraige Status (Yrs)',
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

# Endpoint for simple prediction
@app.route("/predict-simple", methods=["POST"])
def predict_simple():
    try:
        if not request.is_json:
            return jsonify({"error": "Unsupported Media Type. Only JSON requests are allowed."}), 415
        
        data = request.json

        for feature in features_general_public:
            if feature not in data:
                return jsonify({"error": f"Missing feature: {feature}"}), 400

        user_input_df = pd.DataFrame([data], columns=features_general_public)

        for feature in [' Age (yrs)', 'Weight (Kg)', 'Height(Cm) ', 'BMI', 
                        'Pulse rate(bpm) ', 'RR (breaths/min)', 'Cycle length(days)', 
                        'Marraige Status (Yrs)', 'No. of aborptions', 
                        'Hip(inch)', 'Waist(inch)', 'Waist:Hip Ratio', 
                        'BP _Systolic (mmHg)', 'BP _Diastolic (mmHg)']:
            if isinstance(data[feature], (int, float)) and data[feature] < 0:
                return jsonify({"error": f"Invalid input: {feature} cannot be negative."}), 422

        user_input_scaled = loaded_scaler_svm.transform(user_input_df)
        prediction = loaded_svm.predict(user_input_scaled)
        result = "Positive for PCOS" if prediction[0] == 1 else "Negative for PCOS"
        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint for enhanced prediction
@app.route("/predict-enhanced", methods=["POST"])
def predict_enhanced():
    try:
        if not request.is_json:
            return jsonify({"error": "Unsupported Media Type. Only JSON requests are allowed."}), 415
        
        data = request.json

        for feature in features_scan:
            if feature not in data:
                return jsonify({"error": f"Missing feature: {feature}"}), 400

        user_input_df = pd.DataFrame([data], columns=features_scan)

        for feature in features_scan:
            if isinstance(data[feature], (int, float)) and data[feature] < 0:
                return jsonify({"error": f"Invalid input: {feature} cannot be negative."}), 422

        user_input_scaled = loaded_scaler_rf.transform(user_input_df)
        prediction = loaded_random_forest.predict(user_input_scaled)
        result = "Positive for PCOS" if prediction[0] == 1 else "Negative for PCOS"
        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"error": "Method Not Allowed"}), 405

if __name__ == "__main__":
    app.run(debug=True)
