import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

#Load dataset
df = pd.read_csv("dashboard/shunyi_cleaned.csv")

#Menggabungkan kolom year, month, day menjadi satu kolom datetime
df['DATE'] = pd.to_datetime(df[['year', 'month', 'day']])

start_date = df['DATE'].min().date()
end_date = df['DATE'].max().date()

# Sidebar untuk filter tanggal
with st.sidebar:
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=start_date,
        max_value=end_date,
        value=[start_date, end_date]
    )

# Filter data berdasarkan rentang tanggal yang dipilih
df_filtered = df[(df['DATE'] >= pd.to_datetime(start_date)) & (df['DATE'] <= pd.to_datetime(end_date))]

st.title("Dashboard Analisis Polusi Udara")
st.text(
    """
    Nama\t\t: Azel Fabian Azmi
    Cohort ID\t: MC314D5Y0547
    Email\t\t: azelfa65@gmail.com
    """
)

# Tren tahunan polusi udara (menggunakan data yang sudah difilter)
st.subheader("Tren Tahunan Polusi Udara di Shunyi")
polusi = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]
polusi_trends = df_filtered.groupby("year")[polusi].mean().reset_index()

plt.figure(figsize=(10, 6))
for i in polusi:
    plt.plot(polusi_trends['year'], polusi_trends[i], label=i)
plt.title("Tren Tahunan Polusi Udara di Shunyi [Filter Berdasarkan Tanggal]")
plt.xlabel("Tahun")
plt.ylabel("Konsentrasi Polutan (µg/m³)")
plt.xticks(polusi_trends['year'])
plt.legend()
st.pyplot(plt)

# Scatter plot hubungan curah hujan dengan polutan
st.subheader("Hubungan antara Curah Hujan dengan Polutan")
select_polusi = st.selectbox("Pilih Polutan:", polusi)
plt.figure(figsize=(7, 5))
sns.scatterplot(x=df_filtered["RAIN"], y=df_filtered[select_polusi], alpha=0.5)
plt.xlabel("Curah Hujan (mm)")
plt.ylabel(f"{select_polusi} (µg/m³)" if select_polusi != "CO" else "CO (mg/m³)")
st.pyplot(plt)

st.caption('Copyright (c) AzelFA 2025')
