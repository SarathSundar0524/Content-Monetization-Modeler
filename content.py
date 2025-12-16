import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="YouTube Content Monetization Modeler",
                   layout="wide")

@st.cache_resource
def load_model():
    model_path = r"C:\Users\USER\OneDrive\Desktop\contentmodel\bestfit.joblib"
    return joblib.load(model_path)


model = load_model()

st.title("📺 Content Monetization Modeler")
st.write("Estimate YouTube ad revenue for a given video based on its performance metrics.")

st.sidebar.header("Video Inputs")

# --- Collect user inputs ---
views = st.sidebar.number_input("Views", min_value=0, value=10000, step=1000)
likes = st.sidebar.number_input("Likes", min_value=0, value=500, step=10)
comments = st.sidebar.number_input("Comments", min_value=0, value=50, step=5)
watch_time_minutes = st.sidebar.number_input("Watch Time (minutes)", min_value=0.0, value=20000.0, step=100.0)
video_length_minutes = st.sidebar.number_input("Video Length (minutes)", min_value=0.0, value=10.0, step=1.0)
subscribers = st.sidebar.number_input("Subscribers", min_value=0, value=100000, step=1000)

category = st.sidebar.selectbox("Category", [
    "Entertainment", "Education", "Gaming", "Music", "News", "Sports", "Other"
])

device = st.sidebar.selectbox("Device", [
    "mobile", "desktop", "tablet", "tv", "other"
])

country = st.sidebar.text_input("Country (ISO code)", value="US")

# --- Build input dataframe ---
input_dict = {
    "views": views,
    "likes": likes,
    "comments": comments,
    "watch_time_minutes": watch_time_minutes,
    "video_length_minutes": video_length_minutes,
    "subscribers": subscribers,
    "category": category,
    "device": device,
    "country": country,
}

# Feature engineering (must MATCH training)
engagement = likes + comments
engagement_rate = engagement / views if views > 0 else 0
avg_watch_time_per_view = watch_time_minutes / views if views > 0 else 0

input_dict["engagement"] = engagement
input_dict["engagement_rate"] = engagement_rate
input_dict["avg_watch_time_per_view"] = avg_watch_time_per_view

input_df = pd.DataFrame([input_dict])

st.subheader("Input Summary")
st.dataframe(input_df)

if st.button("Predict Revenue"):
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Ad Revenue: **${prediction:,.2f}**")

    st.caption("Note: This is a synthetic model built for learning, not real financial advice.")

# --- Simple insight section (optional) ---
st.subheader("Model Insights")
st.write("""
- Higher **views** and **watch time** generally increase revenue.
- A higher **engagement rate** (likes + comments relative to views) is correlated with better monetization.
- Some **categories**, **countries**, and **devices** may historically yield higher CPMs.
""")
