import streamlit as st
import requests
import json as json
import datetime

st.header("Transportation Mode Predictor App for Malang-Jabodetabek Route")

Fisik_1= st.number_input(
    label="Usia anda (dalam tahun)", 
    min_value=18, 
    max_value=100, 
    value=18)

Fisik_2_list= ['Pria', 'Wanita']
Fisik_3_list= ['Ya', 'Tidak']
Fisik_4_list= ['Ya', 'Tidak']
Fisik_5_list= ['Ya', 'Tidak']
Mental_1_list= ['Pelajar/Mahasiswa', 'Aparatur Sipil Negara (ASN)', 'Wiraswasta/Pengusaha', 'Pegawai Swasta', 'Pensiunan', 'Tidak Bekerja']
Mental_2_list= ['SD/Sederajat', 'SMP/Sederajat', 'SMA/Sederajat', 'Diploma', 'Sarjana (S1)', 'Magister (S2)', 'Doktor (S3)']
Finansial_1_list= ['<Rp2,000,000', 'Rp2,000,000 - Rp4,999,999', 'Rp5,000,000 - Rp9,999,999', '>Rp10,000,000']
Finansial_2_list= ['<Rp500,000', 'Rp500,000 - Rp1,000,000', '>Rp1,000,000']
Karakteristik_1_list= ['Bisnis', 'Pendidikan', 'Wisata', 'Rumah']
jadwal_keberangkatan_list= ['Pagi hari', 'Siang hari', 'Sore hari', 'Malam hari', 'Dini hari']
Frekuensi_list= ['Kurang dari 1 kali per bulan','1 kali per bulan','2-3 kali per bulan','1 kali per pekan','2-3 kali per pekan','1 kali per pekan','Setiap hari']
Kelompok_list= ['Sendiri', 'Bersama 1 orang lain', 'Bersama 2 orang lain', 'Bersama 3 orang lain atau lebih']

Fisik_2_encoded= st.selectbox(label="Jenis Kelamin", options=Fisik_2_list, key="Fisik_2")
Fisik_3_encoded= st.selectbox(label="Apakah Anda Memiliki SIM?", options=Fisik_3_list, key="Fisik_3")
Fisik_4_encoded= st.selectbox(label="Apakah Anda Memiliki Kendaraan Pribadi?", options=Fisik_4_list, key="Fisik_4")
Fisik_5_encoded= st.selectbox(label="Apakah Anda sanggup mengemudi pada rute ini?", options=Fisik_5_list, key="Fisik_5")
Mental_1_encoded= st.selectbox(label="Pekerjaan", options=Mental_1_list, key="Mental_1")
Mental_2_encoded= st.selectbox(label="Pendidikan Terakhir", options=Mental_2_list, key="Mental_2")
Finansial_1_encoded= st.selectbox(label="Pendapatan per Bulan", options=Finansial_1_list, key="Finansial_1")
Finansial_2_encoded= st.selectbox(label="Biaya yang dapat dikeluarkan pada tiket transportasi", options=Finansial_2_list, key="Finansial_2")
Karakteristik_1_encoded= st.selectbox(label="Tujuan Perjalanan", options=Karakteristik_1_list, key="Karakteristik_1")

durasi_time = st.time_input("Durasi Perjalanan Maksimal (jam:menit)", value=datetime.time(0, 0))
durasi_perjalanan = durasi_time.hour + durasi_time.minute / 60

tarif_transportasi= st.number_input(
    label="Tarif Transportasi Maksimal (dalam ribu rupiah)", 
    min_value=0, 
    max_value=5000000, 
    value=0, 
    step=50000)

fasilitas_options = [
    "Kursi", "Toilet", "Colokan Charger", "Bagasi",
    "Reclining Seat", "Sandaran Kaki", "Hiburan", "Makanan/Minuman"
]
fasilitas_selected = st.multiselect(
    "Fasilitas Operator Transportasi (pilih yang diinginkan)",
    options=fasilitas_options
)
fasilitas_operator = len(fasilitas_selected)

jadwal_keberangkatan_encoded= st.selectbox(label="Jadwal Keberangkatan", options=jadwal_keberangkatan_list, key="jadwal_keberangkatan")

kedatangan_time = st.time_input("Jadwal Kedatangan (jam:menit)", value=datetime.time(0, 0))
jadwal_kedatangan = kedatangan_time.hour + kedatangan_time.minute / 60

Frekuensi_encoded= st.selectbox(label="Frekuensi Perjalanan", options=Frekuensi_list, key="Frekuensi")
Kelompok_encoded= st.selectbox(label="Kelompok Perjalanan", options=Kelompok_list, key="Kelompok")

recommendation= st.button(label="Recommend Transportation Mode")

if recommendation:
    # Create a DataFrame for the input features
    input_data = ({
        'Fisik_1': Fisik_1,  # Assuming Fisik_1 is a constant feature with value 1
        'Fisik_2_encoded': Fisik_2_encoded,
        'Fisik_3_encoded': Fisik_3_encoded,
        'Fisik_4_encoded': Fisik_4_encoded,
        'Fisik_5_encoded': Fisik_5_encoded,
        'Mental_1_encoded': Mental_1_encoded,
        'Mental_2_encoded': Mental_2_encoded,
        'Finansial_1_encoded': Finansial_1_encoded,
        'Finansial_2_encoded': Finansial_2_encoded,
        'Karakteristik_1_encoded': Karakteristik_1_encoded,
        'durasi_perjalanan': durasi_perjalanan,
        'tarif_transportasi': tarif_transportasi,
        'fasilitas_operator': fasilitas_operator,
        'jadwal_keberangkatan_encoded': jadwal_keberangkatan_encoded,
        'jadwal_kedatangan': jadwal_kedatangan,
        'Frekuensi_encoded': Frekuensi_encoded,
        'Kelompok_encoded': Kelompok_encoded
    })

    url= st.secrets["API_URL"]

    result = requests.post(url, json=input_data)
    predict = result.json()["Karakteristik_2_encoded"]
    st.write(f"Recommended Transportation Mode:")
    st.write(f"#### {predict}")