from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load models at startup
purity_model = joblib.load('xgb_purity_predictor.pkl')
price_model = joblib.load('xgb_price_predictor.pkl')
pollen_model = joblib.load('xgb_pollen_classifier.pkl')

# Mapping for Pollen_Analysis
pollen_plant_map = {
    'Acacia': 0, 'Alfalfa': 1, 'Avocado': 2, 'Blueberry': 3, 'Borage': 4,
    'Buckwheat': 5, 'Chestnut': 6, 'Clover': 7, 'Eucalyptus': 8, 'Heather': 9,
    'Lavender': 10, 'Manuka': 11, 'Orange Blossom': 12, 'Rosemary': 13,
    'Sage': 14, 'Sunflower': 15, 'Thyme': 16, 'Tupelo': 17, 'Wildflower': 18
}
# Reverse mapping for label to name
pollen_label_to_name = {v: k for k, v in pollen_plant_map.items()}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/purity', methods=['GET', 'POST'])
def purity():
    purity = None
    predicted_price = None
    deal = None
    pollen_plant_options = list(pollen_plant_map.keys())
    if request.method == 'POST':
        # Extract form data
        cs = float(request.form.get('CS'))
        density = float(request.form.get('Density'))
        wc = float(request.form.get('WC'))
        ph = float(request.form.get('pH'))
        ec = float(request.form.get('EC'))
        f = float(request.form.get('F'))
        g = float(request.form.get('G'))
        pollen_plant = request.form.get('PollenPlant')
        pollen_plant_encoded = pollen_plant_map.get(pollen_plant, -1)
        viscosity = float(request.form.get('Viscosity'))
        price = float(request.form.get('Price'))
        if pollen_plant_encoded == -1:
            deal = 'Unknown pollen plant. Please select a valid option.'
        else:
            # Prepare input for purity model (all 10 features, in order)
            purity_features = np.array([[cs, density, wc, ph, ec, f, g, pollen_plant_encoded, viscosity, price]])
            purity_pred = 100*purity_model.predict(purity_features)[0]
            # Cap purity at 99.8%
            if purity_pred > 99.8:
                purity_pred = 99.8
            purity = f'{purity_pred:.2f}%'
            # Prepare input for price model (same order, but use predicted purity instead of actual)
            price_features = np.array([[cs, density, wc, ph, ec, f, g, pollen_plant_encoded, viscosity, purity_pred]])
            predicted_price_val = price_model.predict(price_features)[0]
            predicted_price = f'₹{predicted_price_val:.2f}'
            # Deal verdict logic with 5% error margin
            error_margin = 0.05 * price
            if price < predicted_price_val - error_margin:
                deal = f'Great deal! (Predicted price : ₹{predicted_price_val - error_margin:.2f} - ₹{predicted_price_val + error_margin:.2f})'
            elif price > predicted_price_val + error_margin:
                deal = f'Expensive! (Predicted price : ₹{predicted_price_val - error_margin:.2f} - ₹{predicted_price_val + error_margin:.2f})'
            else:
                deal = f'Fair deal. (Predicted price : ₹{predicted_price_val - error_margin:.2f} - ₹{predicted_price_val + error_margin:.2f})'
    else:
        pollen_plant_options = list(pollen_plant_map.keys())
    return render_template('purity.html', purity=purity, predicted_price=predicted_price, deal=deal, pollen_plant_options=pollen_plant_options)

@app.route('/pollen', methods=['GET', 'POST'])
def pollen():
    pollen_result = None
    if request.method == 'POST':
        cs = float(request.form.get('CS'))
        density = float(request.form.get('Density'))
        wc = float(request.form.get('WC'))
        ph = float(request.form.get('pH'))
        ec = float(request.form.get('EC'))
        f = float(request.form.get('F'))
        g = float(request.form.get('G'))
        viscosity = float(request.form.get('Viscosity'))
        purity = float(request.form.get('Purity'))
        price = float(request.form.get('Price'))
        # Prepare input for pollen model
        pollen_features = np.array([[cs, density, wc, ph, ec, f, g, viscosity, purity, price]])
        pollen_pred = pollen_model.predict(pollen_features)[0]
        pollen_name = pollen_label_to_name.get(int(pollen_pred), f'Unknown (label {pollen_pred})')
        pollen_result = f'Predicted Pollen Plant: {pollen_name}'
    return render_template('pollen.html', pollen_result=pollen_result)

if __name__ == '__main__':
    app.run(debug=True) 