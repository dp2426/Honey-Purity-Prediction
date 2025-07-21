# 🍯 Honey Purity & Price Prediction System

---
Try this project by clicking on Link: [Honey-Pure](https://honey-purity.onrender.com)
---
Public Dataset used : [Honey Pricing By Statistics Department of Bangalore University](https://www.kaggle.com/datasets/ravikumarbangalore/honey-price-analysis)
## 📖 Story Behind the Project

On a family trip to the serene hill station of **Saputara in Gujarat**, the roads were lined with small shops shouting **100% Organic Honey!** and **Pure Forest Honey**.  
While I was admiring the hills, my sister squinted at a vendor and whispered, **There are way too many. Why would we even trust these labels?**

My parents were hooked on the local charm — **This is better than the supermarket stuff!**  
And that’s when the golden question came in from my sister:

> **How much better, exactly?**

Boom. Silence.

And *that* stuck with me.

How can we **quantify** something as vague as *purity* in a marketplace flooded with marketing jargon?  
That moment sparked this idea — a tool to evaluate honey's **purity** and **price fairness**, backed by **data** and **machine learning**, not packaging buzzwords.

---

## 🔍 Project Overview

This system takes in a few **scientific and measurable features** of honey (like electrical conductivity, fructose content, acidity, etc.) and:

1. **Predicts Honey Purity (%)**
2. **Estimates a Fair Market Price**
3. **Classifies a Deal as "Great", "Fair", or "Overpriced"**
4. **Predicts the Pollen Source (Botanical Origin)**

All of this is handled with user-friendly web forms and trained regression/classification models under the hood.

---

## 🧪 Dataset Features & Their Role

| Feature | Description | Importance |
|--------|-------------|------------|
| `CS` | Color Score (1.0–10.0) | Indicates honey color (light to dark) |
| `Density` | g/cm³ at 25°C (1.21–1.86) | Physical property, helps verify authenticity |
| `WC` | Water Content (12.0%–25.0%) | High water = lower purity |
| `pH` | Acidity (2.50–7.50) | Freshness and fermentation marker |
| `EC` | Electrical Conductivity (mS/cm) | Mineral/ion concentration, botanical marker |
| `F` | Fructose Level (20–50) | Natural sugar, higher = purer |
| `G` | Glucose Level (20–45) | Sugar balance |
| `Pollen_Analysis` | Botanical source (categorical) | Verifies floral origin |
| `Viscosity` | 1500–10000 cP (optimal: 2500–9500) | Texture and purity marker |
| `Purity` | 0.01–1.00 | Target variable |
| `Price` | Calculated price | Used for deal evaluation |

---

## 🛠️ Tech Stack

| Component | Tech |
|----------|------|
| Programming Language | Python 3.11 |
| Data Handling | Pandas, NumPy |
| Model Training | scikit-learn, XGBoost |
| Web App | Flask |
| Frontend | HTML, CSS (custom, Tailwind-inspired) |
| Model Persistence | Pickle, Joblib |
| Deployment | Render.com (or any Flask-compatible host) |

---

## 🔮 Machine Learning Models Used

### 🔹 Honey Purity Predictor (Regression)
- **Algorithm**: `XGBRegressor`
- **Tuned via**: `RandomizedSearchCV + 5-Fold Cross-Validation`
- **RMSE**: `0.0`
- **R² Score**: `0.98`
- ✅ Highly accurate — can be trusted for purity prediction within 2% margin.

### 🔹 Price Prediction Model (Regression)
- **Algorithm**: `XGBRegressor`
- **Trained with Same Inputs + Optional "Purity %"**
- **Used for**: Estimating fair price per unit weight
- **RMSE Score**: `0.91`

### 🔹 Deal Classification (Great Deal / Fair / Overpriced)
- **Post-processing Step** using price delta:
    - Great Deal → Predicted Price > Actual Price by > 5%
    - Fair → within ±5%
    - Overpriced → Actual Price > Predicted by > 5%

### 🔹 Pollen Source Predictor (Classification)
- **Algorithm**: `XGBClassifier`
- **Predicts**: Botanical origin of honey based on technical features

---

## 🎯 Goals Achieved

- ✅ Purity estimation with high accuracy
- ✅ Price prediction for quality control
- ✅ Deal evaluation from customer's POV
- ✅ Pollen source prediction
- ✅ Fully ML-driven insight to combat fake "organic" claims
- ✅ Modern, user-friendly web interface

---

---

## 🌐 Deployment

- This app is ready for deployment on [Render.com](https://render.com/)
- Make sure your `requirements.txt` is up to date and your model files are included.

---

## 🧠 TL;DR

> **A transparent, ML-based solution to expose truth behind the "pure honey" labels flooding the market — using science, not slogans.**

