========================
File: app.py
========================
import streamlit as st
import pandas as pd
import plotly.express as px

# Load data from Google Sheet CSV
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQBfePx1CHyOOXGc_MpgKlkdmjZaMX6T3fjFW8559_ju4x_dm6iptZ7AiFsbHYQRPAqxrmcO-4kTitL/pub?output=csv"
df = pd.read_csv(url)

# Sidebar navigation
st.sidebar.title("📊 Dashboard Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Trends", "KPIs", "Infographics", "Raw Data"])

# ---------------- Overview Page ----------------
if page == "Overview":
    st.title("📈 Dashboard Overview")
    st.write("Welcome to your interactive dashboard powered by Google Sheets data.")
    st.metric("Total Rows", len(df))
    st.write("Quick preview of your dataset:")
    st.dataframe(df.head())

# ---------------- Trends Page ----------------
elif page == "Trends":
    st.title("📉 Trends")
    if "Date" in df.columns:
        selected_y = st.selectbox("Choose a column to plot:", [col for col in df.columns if col != "Date"])
        fig = px.line(df, x="Date", y=selected_y,
                      title=f"Trend of {selected_y} Over Time",
                      template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No 'Date' column found in your dataset.")

# ---------------- KPIs Page ----------------
elif page == "KPIs":
    st.title("⭐ Key Performance Indicators")
    for col in df.select_dtypes(include=['int64','float64']).columns:
        st.subheader(f"KPI for {col}")
        st.metric("Average", round(df[col].mean(), 2))
        st.metric("Max", df[col].max())
        st.metric("Min", df[col].min())

# ---------------- Infographics Page ----------------
elif page == "Infographics":
    st.title("🎨 Infographics")
    selected_col = st.selectbox("Choose a column:", df.columns)
    fig = px.histogram(df, x=selected_col, color=selected_col,
                       title=f"Distribution of {selected_col}",
                       template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

    # Extra visuals
    if df[selected_col].nunique() < 20:
        fig2 = px.pie(df, names=selected_col, title=f"Pie Chart of {selected_col}")
        st.plotly_chart(fig2, use_container_width=True)

# ---------------- Raw Data Page ----------------
elif page == "Raw Data":
    st.title("📑 Raw Data")
    st.dataframe(df)
    st.download_button("Download CSV", df.to_csv(index=False), "data.csv")

========================
File: requirements.txt
========================
streamlit
pandas
plotly

========================
File: README.md
========================
# My Dashboard

This is a Streamlit dashboard that loads data directly from a Google Sheet CSV.

## How to run locally
1. Install dependencies:
