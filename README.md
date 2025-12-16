# Content Monetization Modeler

## Project Overview
As video creators and media companies increasingly rely on platforms like YouTube for income, accurately predicting ad revenue is critical for business planning and content strategy.  
This project builds a **regression-based predictive model** to estimate YouTube ad revenue for individual videos using performance and contextual features, and demonstrates the results through a **Streamlit web application**.

The solution covers the complete data science lifecycle — from data cleaning and exploratory analysis to model evaluation and deployment.

---

## Domain
**Social Media Analytics**

---

## Problem Statement
Build a **Linear Regression–based predictive system** to estimate YouTube ad revenue (`ad_revenue_usd`) for videos using historical performance and contextual data, and deploy the model in a simple, interactive Streamlit application.

---

## Business Use Cases
- **Content Strategy Optimization**  
  Helps creators identify content characteristics that generate higher revenue.
- **Revenue Forecasting**  
  Enables media companies to estimate income from upcoming uploads.
- **Creator Support Tools**  
  Can be integrated into analytics platforms for YouTubers.
- **Ad Campaign Planning**  
  Allows advertisers to forecast ROI based on performance metrics.

---

## Dataset Information
- **Name:** YouTube Monetization Modeler  
- **Format:** CSV  
- **Size:** ~122,000 rows  
- **Source:** Synthetic dataset created for learning purposes  
- **Target Variable:** `ad_revenue_usd`

### Dataset Description
Each row represents performance metrics for a specific video on a specific day.

Key columns include:
- `video_id` – Unique video identifier  
- `date` – Upload or report date  
- `views`, `likes`, `comments` – Engagement metrics  
- `watch_time_minutes`, `video_length_minutes` – Content engagement  
- `subscribers` – Channel subscriber count  
- `category`, `device`, `country` – Contextual features  
- `ad_revenue_usd` – Revenue generated (target)

---

## Preprocessing Requirements
- Handle ~5% missing values in key columns
- Remove ~2% duplicated records
- Encode categorical variables (`category`, `device`, `country`)
- Normalize or scale numerical features where required
- Detect and treat outliers

---

## Project Approach

### 1. Data Understanding
- Load and inspect dataset
- Validate schema and data types

### 2. Exploratory Data Analysis (EDA)
- Identify trends and distributions
- Analyze correlations with revenue
- Detect anomalies and outliers
- Visualize engagement vs revenue patterns

### 3. Data Preprocessing
- Missing value handling
- Duplicate removal
- Categorical encoding
- Feature scaling

### 4. Feature Engineering
- Create derived features such as:
  - Engagement rate = (likes + comments) / views
- Improve predictive signal quality

### 5. Model Building
- Train and compare **5 different regression models**
- Predict `ad_revenue_usd`
- Identify the most effective model

### 6. Model Evaluation
- Evaluate using:
  - R² Score
  - Root Mean Squared Error (RMSE)
  - Mean Absolute Error (MAE)

### 7. Streamlit App Development
- Interactive revenue prediction
- Input-based forecasting
- Basic visual analytics and insights

### 8. Interpretation & Insights
- Identify key drivers of ad revenue
- Translate model outputs into business insights

---

## Results
- A trained and evaluated regression model for ad revenue prediction
- A cleaned and well-processed dataset
- Actionable insights on factors influencing YouTube ad revenue
- A functional Streamlit application for interactive testing

---

## Evaluation Metrics
- R² Score
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- Code quality and documentation
- Depth of EDA and insights
- Streamlit app usability and functionality

---

## Technical Tags
Linear Regression, EDA, Feature Engineering, Pandas, Scikit-learn, Outlier Detection, Missing Value Handling, Machine Learning, Data Visualization, Streamlit, Model Evaluation

---

## Project Deliverables
- Jupyter Notebook or Python scripts containing:
  - Full EDA
  - Data preprocessing
  - Model building
  - Evaluation and insights
- Streamlit application showcasing:
  - Revenue prediction from user inputs
  - Visual analytics
- README with project overview and execution steps

---

## Skills Gained
- Regression Models
- Predictive Modeling
- Feature Engineering
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Regression Metrics (R², RMSE, MAE)
- Data Visualization
- Streamlit
- Python
- Pandas
- Scikit-learn
- Categorical Encoding
- Outlier Detection
- Missing Value Handling

---

## Project Guidelines
- Follow clean coding practices
- Use Git/GitHub for version control
- Avoid hardcoded file paths
- Include markdown explanations and comments
- Add basic error handling
- Ensure Streamlit app runs end-to-end without errors

---

## How to Run
```bash
pip install -r requirements.txt
streamlit run app/app.py
