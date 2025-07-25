from flask import Flask, render_template, request
import pandas as pd
import joblib
import numpy as np
from features import extract_features_per_cycle  # ton script d'extraction

app = Flask(__name__)

# Charger le modèle
model = joblib.load("models/XGBoost.pkl")

# Charger les données
ps2_data = pd.read_csv("data/raw_data/PS2.txt", sep='\t', header=None)
fs1_data = pd.read_csv("data/raw_data/FS1.txt", sep='\t', header=None)
profile = pd.read_csv("data/raw_data/profile.txt", sep='\t', header=None)
profile.columns = ['cooler_cond', 'valve_cond', 'pump_leakage', 'accumulator_press', 'stable_flag']

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    proba = None
    ground_truth = None
    error = None
    cycle_id = None

    if request.method == 'POST':
        try:
            cycle_id = int(request.form['cycle_id'])
            if cycle_id < 0 or cycle_id >= len(profile):
                raise ValueError("ID de cycle hors plage.")

            ps2_cycle = ps2_data.iloc[cycle_id]
            fs1_cycle = fs1_data.iloc[cycle_id]

            features = extract_features_per_cycle(ps2_cycle, fs1_cycle)
            features_df = pd.DataFrame([features])

            prediction = model.predict(features_df)[0]
            proba = model.predict_proba(features_df)[0][int(prediction)]
            ground_truth = int(profile.iloc[cycle_id]["valve_cond"] == 100)

        except Exception as e:
            error = str(e)

    return render_template(
        "index.html",
        prediction=prediction,
        proba=proba,
        ground_truth=ground_truth,
        cycle_id=cycle_id,
        error=error
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

