# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Title
# ---------------------------
st.title("Vehicle Insurance Predictions")
st.write("Visualize the predictions made by the XGBoost model.")

# ---------------------------
# Load prediction CSV
# ---------------------------
submission = pd.read_csv("submission.csv")

# ---------------------------
# Sidebar filters
# ---------------------------
st.sidebar.header("Filter Predictions")
prob_threshold = st.sidebar.slider("Probability threshold", 0.0, 1.0, 0.5, 0.01)
class_filter = st.sidebar.selectbox("Predicted class", ["All", 0, 1])

filtered_df = submission[submission['Response_Prob'] >= prob_threshold]
if class_filter != "All":
    filtered_df = filtered_df[filtered_df['Response'] == int(class_filter)]

# ---------------------------
# Show filtered table
# ---------------------------
st.subheader("Filtered Predictions")
st.dataframe(filtered_df)

# ---------------------------
# Bar chart of predicted classes
# ---------------------------
st.subheader("Prediction Distribution")
class_counts = filtered_df['Response'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(class_counts.index.astype(str), class_counts.values, color=['skyblue','salmon'])
ax.set_xlabel("Predicted Class")
ax.set_ylabel("Count")
ax.set_title("Distribution of Predicted Classes")
st.pyplot(fig)

# ---------------------------
# Optional: Show top 10 highest probabilities
# ---------------------------
st.subheader("Top 10 highest probability predictions")
st.dataframe(filtered_df.sort_values('Response_Prob', ascending=False).head(10))
