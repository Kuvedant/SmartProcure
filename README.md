# 🛠️ SmartProcure: Procurement Intelligence System

![SmartProcure Screenshot](./dashboard_preview.png)

**SmartProcure** is an intelligent decision-support system that automates the classification of procurement items using the **Kraljic Matrix** and predicts **lead time** using machine learning. It helps organizations make strategic sourcing decisions by assessing cost, risk, volume, and environmental impact.

---

## 🚀 Project Overview

In supply chain management, classifying items based on **supply risk** and **profit impact** is critical but often subjective and time-consuming. **SmartProcure** leverages machine learning to:

- 📊 **Classify items** into Kraljic quadrants: Strategic, Leverage, Bottleneck, Non-Critical.
- ⏱️ **Predict lead time** for procurement items.
- 🌱 Integrate **sustainability and risk insights** into procurement decision-making.

---

## 🧠 Models Used

| Task                         | Algorithm               |
|-----------------------------|--------------------------|
| Classification              | Random Forest Classifier |
| Lead Time Prediction        | Random Forest Regressor  |
| Baselines Compared          | Logistic Regression, SVM, KNN, Naive Bayes, Decision Tree, Gradient Boosting |
| Regression Benchmarks       | Linear, Ridge, Lasso, SVR, Tree-based Regressors |

✅ Best models were selected based on **Accuracy (Classification)** and **R² / RMSE (Regression)**.

---

## 📦 Dataset Details

- **Source**: [Kaggle - Procurement Strategy Dataset for Kraljic Matrix](https://www.kaggle.com/datasets/shahriarkabir/procurement-strategy-dataset-for-kraljic-matrix)
- **Size**: 1,000 records
- **File**: `realistic_kraljic_dataset.csv`
- **Features**:
  - Lead_Time_Days
  - Order_Volume_Units
  - Cost_per_Unit
  - Supply_Risk_Score
  - Profit_Impact_Score
  - Environmental_Impact
  - Single_Source_Risk
  - Kraljic_Category (Target)

---

## 📊 Exploratory Data Analysis Highlights

- ⚖️ Balanced class distribution across Kraljic categories
- 📈 Strong correlations observed:
  - `Cost_per_Unit` ↔ `Supply_Risk_Score` & `Environmental_Impact`
- 🗺️ Region-wise variability in `Lead_Time_Days`
- 🔍 Feature importance shows `Cost_per_Unit` and `Profit_Impact_Score` as key drivers

---

## 🖥️ Streamlit Dashboard

Launch the interactive dashboard to:
- Input item characteristics
- View predicted Kraljic category and estimated lead time
- Visualize feature importances

### 🔗 Preview

![SmartProcure Dashboard](./dashboard_preview.png)

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Kuvedant/SmartProcure.git
cd SmartProcure
```

```bash
pip install -r requirements.txt

```

```bash
streamlit run smartprocure_dashboard.py
```

```bash
SmartProcure/
│
├── smartprocure_dashboard.py         # Streamlit app
├── SmartProcureProject.ipynb         # Main notebook with EDA + Modeling
├── realistic_kraljic_dataset.csv     # Dataset
├── rf_classifier.pkl                 # Trained classification model
├── rf_regressor.pkl                 # Trained regression model
├── dashboard_preview.png             # Dashboard UI screenshot
├── requirements.txt
└── README.md
```
## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

MIT License

Copyright (c) 2025 SmartProcure Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

