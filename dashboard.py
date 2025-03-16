import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.preprocessing import MinMaxScaler


from babel.numbers import format_currency
sns.set(style='dark')

#Load dataset
df = pd.read_csv("/dashboard/shunyi_cleaned.csv")

#Dataset Normalisasi
scaler = MinMaxScaler()
polusi = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]
normalisasi = df
normalisasi[polusi] = scaler.fit_transform(df[polusi])
polusi_trends = normalisasi.groupby("year")[polusi].mean().reset_index()

# Judul Dashboard
st.title("Dashboard Analisis Polusi Udara")
st.text(
    """
    Nama\t\t: Azel Fabian Azmi
    Cohort ID\t: MC314D5Y0547
    Email\t\t: azelfa65@gmail.com
    """
)

# Tren tahunan polusi udara
st.subheader("Tren Tahunan Polusi Udara di Shunyi (2013-2017)")
polusi_trends = df.groupby("year")[polusi].mean().reset_index()
plt.figure(figsize=(10, 6))
for i in polusi:
    plt.plot(polusi_trends['year'], polusi_trends[i], label=i)
plt.title("Tren Tahunan Polusi Udara di Shunyi (2013-2017) [Normalisasi Min-Max]")
plt.xlabel("Tahun")
plt.ylabel("Skala Normalisasi (0-1)")
plt.xticks(polusi_trends['year'])
plt.legend()
st.pyplot(plt)

# Scatter plot hubungan curah hujan dengan polutan
st.subheader("Hubungan antara Curah Hujan dan Polutan")
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6 = st.columns(2)

with col1:
    st.subheader("PM2.5")
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x=df["RAIN"], y=df["PM2.5"], alpha=0.5)
    plt.xlabel("Curah Hujan (mm)")
    plt.ylabel("PM2.5 (µg/m³)")
    st.pyplot(plt)

with col2:
    st.subheader("PM10")
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x=df["RAIN"], y=df["PM10"], alpha=0.5)
    plt.xlabel("Curah Hujan (mm)")
    plt.ylabel("PM10 (µg/m³)")
    st.pyplot(plt)

with col3:
    st.subheader("SO2")
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x=df["RAIN"], y=df["SO2"], alpha=0.5)
    plt.xlabel("Curah Hujan (mm)")
    plt.ylabel("SO2 (µg/m³)")
    st.pyplot(plt)

with col4:
    st.subheader("NO2")
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x=df["RAIN"], y=df["NO2"], alpha=0.5)
    plt.xlabel("Curah Hujan (mm)")
    plt.ylabel("NO2 (µg/m³)")
    st.pyplot(plt)

with col5:
    st.subheader("CO")
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x=df["RAIN"], y=df["CO"], alpha=0.5)
    plt.xlabel("Curah Hujan (mm)")
    plt.ylabel("CO (mg/m³)")
    st.pyplot(plt)

with col6:
    st.subheader("O3")
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x=df["RAIN"], y=df["O3"], alpha=0.5)
    plt.xlabel("Curah Hujan (mm)")
    plt.ylabel("O3 (µg/m³)")
    st.pyplot(plt)
st.caption('Copyright (c) AzelFA 2025')
