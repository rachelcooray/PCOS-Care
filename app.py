from flask import Flask, request, jsonify
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

## https://flask.palletsprojects.com/en/stable/errorhandling/

# Load the trained SVM model and scaler
with open("best_svm_model.pkl", "rb") as model_file:
    loaded_svm = pickle.load(model_file)

# Load the trained Random Forest model and scaler
with open("best_random_forest_model.pkl", "rb") as model_file:
    loaded_random_forest = pickle.load(model_file)


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

numerical_columns_gen = [
    ' Age (yrs)', 'Weight (Kg)', 'Height(Cm) ', 'BMI', 'Pulse rate(bpm) ', 
    'RR (breaths/min)', 'Cycle(R/I)', 'Cycle length(days)', 
    'Marraige Status (Yrs)', 'No. of aborptions', 'Hip(inch)', 'Waist(inch)', 'Waist:Hip Ratio', 
    'BP _Systolic (mmHg)', 'BP _Diastolic (mmHg)'
]

categorical_columns_gen = [
    'Blood Group', 'Pregnant(Y/N)', 'Weight gain(Y/N)', 'hair growth(Y/N)', 'Skin darkening (Y/N)', 
    'Hair loss(Y/N)', 'Pimples(Y/N)', 'Fast food (Y/N)', 'Reg.Exercise(Y/N)'
]

numerical_columns_scan = [
    ' Age (yrs)', 'Weight (Kg)', 'Height(Cm) ', 'BMI', 'Pulse rate(bpm) ', 
    'RR (breaths/min)', 'Hb(g/dl)', 'Cycle(R/I)', 'Cycle length(days)', 
    'Marraige Status (Yrs)', 'No. of aborptions', 
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


# Endpoint for simple prediction
@app.route("/predict-simple", methods=["POST"])
def predict_simple():
    try:
        if not request.is_json:
            return jsonify({"error": "Unsupported Media Type. Only JSON requests are allowed."}), 415
        
        data = request.json

        # Get user input for numerical columns
        user_inputs = []
        for col in numerical_columns_gen:
            if col in data:
                user_inputs.append(data[col])
            else:
                return jsonify({"error": f"Missing feature: {col}"}), 400

        # Prepare the DataFrame with numerical inputs (before scaling)
        numerical_inputs_df = pd.DataFrame([user_inputs], columns=numerical_columns_gen)

        # Scale only numerical features using StandardScaler
        scaler = StandardScaler()
        scaled_numerical_inputs = scaler.fit_transform(numerical_inputs_df)

        # Get user input for categorical columns and append them
        categorical_inputs = []
        for col in categorical_columns_gen:
            if col in data:
                categorical_inputs.append(data[col])
            else:
                return jsonify({"error": f"Missing feature: {col}"}), 400

        # Combine scaled numerical inputs and categorical inputs into a final DataFrame
        final_inputs = pd.DataFrame(scaled_numerical_inputs, columns=numerical_columns_gen)
        final_inputs[categorical_columns_gen] = categorical_inputs

        # Ensure the column order matches the model's expectation
        final_inputs = final_inputs[features_general_public]

        # Make prediction using the trained SVM model
        prediction = loaded_svm.predict(final_inputs)

        # Output the prediction result
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

        user_inputs = []
        for col in numerical_columns_scan:
            if col in data:
                user_inputs.append(data[col])
            else:
                return jsonify({"error": f"Missing feature: {col}"}), 400

        numerical_inputs_df = pd.DataFrame([user_inputs], columns=numerical_columns_scan)

        scaler = StandardScaler()
        scaled_numerical_inputs = scaler.fit_transform(numerical_inputs_df)

        categorical_inputs = []
        for col in categorical_columns_scan:
            if col in data:
                categorical_inputs.append(data[col])
            else:
                return jsonify({"error": f"Missing feature: {col}"}), 400

        final_inputs = pd.DataFrame(scaled_numerical_inputs, columns=numerical_columns_scan)
        final_inputs[categorical_columns_scan] = categorical_inputs

        final_inputs = final_inputs[features_scan]

        prediction = loaded_random_forest.predict(final_inputs)

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