import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# 1. Judul Aplikasi Web
st.set_page_config(page_title="AI Prediksi Bola", page_icon="⚽", layout="centered")
st.title("⚽ Sistem Prediksi Pertandingan Sepakbola")
st.write("Aplikasi web interaktif untuk memprediksi hasil laga berdasarkan statistik tim.")

# 2. Simulasi Data Statistik Tim (Nanti bisa diganti dengan data asli/API)
st.sidebar.header("⚙️ Pengaturan Statistik Tim")

st.sidebar.subheader("Tim Tuan Rumah (home)")
home_team = st.sidebar.text_input("Nama Tim Home", "Arsenal")
home_attack = st.sidebar.slider("Kekuatan Menyerang Home (Rata-rata Gol)", 0.5, 4.0, 2.1)

st.sidebar.subheader("Tim Tamu (Away)")
away_team = st.sidebar.text_input("Nama Tim Away", "Chealsea")
away_attack = st.sidebar.slider("Kekuatan Menyerang Away (Rata-rata Gol)", 0.5, 4.0, 1.2)

# 3. Logika Prediksi Sederhana (Simulasi Probabilitas)
# Kita membuat variasi angka acak berbasis kekuatan menyerang untuk menentukan peluang
total_power = home_attack + away_attack
prob_home = round((home_attack / total_power) * 100 - 10, 1)
prob_away = round((away_attack / total_power) * 100 - 10, 1)
prob_draw = round(100 - prob_home - prob_away, 1)

# 4. Tampilan Utama Dashboard
st.subheader(f"⚔️ Analisis Laga : {home_team} vs {away_team}")

if st.button("🔄 Hitung Prediksi Sekarang", type="primary"):
    # Tampilkan hasil persentase peluang
    col1, col2, col3 = st.columns(3)
    col1.metric(label=f"Menang ({home_team})", value=f"{prob_home}%")
    col2.metric(label="Seri (Draw)", value=f"{prob_draw}%")
    col3.metric(label=f"Menang ({away_team})", value=f"{prob_away}%")

    # 5. Membuat Grafik Visualisasi yang keren dengan PLotly
    labels = [home_team, 'Seri', away_team]
    values = [prob_home, prob_draw, prob_away]
    colors = ['#2ca02c', '#7f7f7f', '#d62728']

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4, marker=dict(colors=colors))])
    fig.update_layout(title_text="Grafik Probabilitas Hasil Pertandingan")
    st.plotly_chart(fig)

    # Kesimpulan Prediksi
    prediksi_pemenang = home_team if prob_home > prob_away else away_team
    st.success(f"💡 **Kesimpulan Analisis:** {home_team} diunggulkan menang karena statistik produktivitas gol kandang yang lebih tinggi.")
else:
    st.info("Silahkan ubah performa tim di menu samping (sidebar) lalu klik tombol di atas untuk melihat prediksi.")