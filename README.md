# Content Monetization Modeler

## What I Built
I built an **end-to-end Content Monetization Modeler** that predicts **YouTube ad revenue** using video performance and contextual data.  
The project covers the complete data science workflow — from raw data analysis to model deployment using **Streamlit**.

The final output is a **production-ready regression model** that allows users to input video metrics and get an estimated ad revenue in real time.

---

## Domain
Social Media Analytics

---

## Work Done in This Project

### Data Understanding & Exploration
- Loaded and explored a large-scale dataset (~122K rows)
- Analyzed distributions, trends, and correlations across engagement and revenue
- Identified missing values, duplicates, and potential outliers

### Data Cleaning
- Removed duplicate records 
- Handled missing values using statistical imputation
- Ensured data consistency and correct data types

### Exploratory Data Analysis (EDA)
- Performed univariate and multivariate analysis
- Visualized feature distributions and revenue patterns
- Used correlation heatmaps to identify key revenue drivers
- Inspected skewness and kurtosis for numerical stability

### Feature Engineering
- Created business-driven features such as:
  - **Engagement Rate** = (likes + comments) / views
  - **Average Watch Time per View**
- Improved predictive strength using meaningful derived metrics

### Model Development
- Trained and evaluated **multiple regression models**:
  - Linear Regression
  - Decision Tree Regressor
  - Random Forest Regressor
  - Gradient Boosting Regressor
  - XGBoost Regressor
- Compared models using standard regression metrics
- Selected **Linear Regression** for its strong performance and interpretability

### Model Evaluation
- Evaluated models using:
  - R² Score
  - RMSE
  - MAE
- Achieved high predictive accuracy (R² ≈ 0.95)

### Model Deployment
- Built a **Streamlit web application** for interactive usage
- Enabled real-time ad revenue prediction from user inputs
- Integrated feature engineering logic into the app
- Saved and loaded the trained model using `joblib`

---

## Dataset Overview
- Dataset: YouTube Monetization Modeler
- Format: CSV
- Size: ~122,000 rows
- Type: Synthetic (for learning purposes)
- Target Variable: `ad_revenue_usd`

Each row represents daily performance metrics of a video, including:
- Views, likes, comments
- Watch time and video length
- Subscriber count
- Category, device, and country context

---

## Results Achieved
- Built a reliable regression model to predict ad revenue
- Identified key factors influencing monetization:
  - Views and watch time are the strongest drivers
  - Engagement rate improves revenue predictability
- Delivered a clean, interactive Streamlit application
- Created a reusable modeling pipeline suitable for real-world deployment

---

## Skills Gained From This Project
- Regression Modeling
- Predictive Analytics
- Feature Engineering
- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Regression Metrics (R², RMSE, MAE)
- Model Comparison & Selection
- Data Visualization
- Python
- Pandas & NumPy
- Scikit-learn
- Categorical Encoding
- Outlier Detection
- Missing Value Handling
- Streamlit Application Development
- Model Deployment using Joblib

---

## Tech Stack
Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Streamlit

---

## How to Run
```bash
pip install -r requirements.txt
streamlit run content.py

