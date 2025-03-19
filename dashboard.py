import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.preprocessing import MinMaxScaler

sns.set(style='dark')

#Load dataset
df = pd.read_csv("dashboard/shunyi_cleaned.csv")

#Dataset Normalisasi
scaler = MinMaxScaler()
polusi = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]
normalisasi = df
normalisasi[polusi] = scaler.fit_transform(df[polusi])
polusi_trends = normalisasi.groupby("year")[polusi].mean().reset_index()


st.title("Dashboard Analisis Polusi Udara")
st.text(
    """
    Nama\t\t: Azel Fabian Azmi
    Cohort ID\t: MC314D5Y0547
    Email\t\t: azelfa65@gmail.com
    """
)

#Tren tahunan polusi udara
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

#Scatter plot hubungan curah hujan dengan polutan
st.subheader("Hubungan antara Curah Hujan dengan Polutan")
select_polusi = st.selectbox("Pilih Polutan:", polusi)
plt.figure(figsize=(7, 5))
sns.scatterplot(x=df["RAIN"], y=df[select_polusi], alpha=0.5)
plt.xlabel("Curah Hujan (mm)")
plt.ylabel(f"{select_polusi} (µg/m³)" if select_polusi != "CO" else "CO (mg/m³)")
st.pyplot(plt)

st.caption('Copyright (c) AzelFA 2025')
