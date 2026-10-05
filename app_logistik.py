import streamlit as st
import pandas as pd

# =================================================================
# APLIKASI UTAMA: DIGITAL HUB LOGISTIK & EXIM MM2100
# Dibuat untuk dashboard interaktif manajemen operasional
# =================================================================

st.set_page_config(page_title="Exim Digital Hub", page_icon="📦", layout="wide")

st.title("📦 Exim & Warehouse Digital Hub - MM2100")
st.write("Aplikasi internal pintar untuk mempermudah operasional logistik harian.")

# MEMBUAT NAVBAR / PILIHAN MENU DI SEBELAH KIRI
menu = st.sidebar.radio("Pilih Alat Kerja:", ["Kalkulator Pajak Impor", "Tracker Free Time Kontainer", "Data Manifest Gudang"])

# --- MENU 1: KALKULATOR INTERAKTIF ---
if menu == "Kalkulator Pajak Impor":
    st.subheader("🧮 Kalkulator Simulasi Bea Masuk & PPN")
    
    # Input interaktif berbentuk slider dan kotak angka
    cif_value = st.number_input("Masukkan Nilai Barang (CIF) dalam Rupiah:", min_value=0, value=50000000, step=1000000)
    tarif_bm = st.slider("Tarif Bea Masuk (%):", min_value=0.0, max_value=30.0, value=7.5, step=0.5)
    
    # Logika hitungan
    bea_masuk = cif_value * (tarif_bm / 100)
    nilai_impor = cif_value + bea_masuk
    ppn = nilai_impor * 0.11
    total_bayar = bea_masuk + ppn
    
    # Tampilan hasil yang estetik di web
    col1, col2, col3 = st.columns(3)
    col1.metric("Biaya Bea Masuk", f"Rp {bea_masuk:,.0f}")
    col2.metric("PPN (11%)", f"Rp {ppn:,.0f}")
    col3.metric("TOTAL WAJIB BAYAR", f"Rp {total_bayar:,.0f}")

# --- MENU 2: TRACKER FREE TIME ---
elif menu == "Tracker Free Time Kontainer":
    st.subheader("⏳ Peringatan Demurrage & Free Time")
    st.write("Simulasi sistem deteksi otomatis sisa hari kontainer di depo pelabuhan.")
    
    sisa_hari = st.number_input("Masukkan sisa hari free time kontainer:", min_value=0, max_value=14, value=3)
    
    if sisa_hari <= 2:
        st.error(f"🚨 STATUS WARNING: Sisa {sisa_hari} hari! Segera lakukan penarikan/stripping kontainer!")
    else:
        st.success(f"✅ STATUS AMAN: Sisa {sisa_hari} hari berjalan.")

# --- MENU 3: DATA MANIFEST GUDANG ---
elif menu == "Data Manifest Gudang":
    st.subheader("📊 Manifest Data Viewer")
    st.write("Contoh simulasi penarikan database manifes kontainer secara rapi:")
    
    # Membuat tiruan data database logistik sederhana
    data_logistik = {
        'No Container': ['TGBU1234567', 'MSKU9876543', 'NYKU4567890'],
        'Ukuran': ["20ft", "40ft", "40ft HC"],
        'Status Customs': ['SPPB / Jalur Hijau', 'Hold / Jalur Merah', 'Proses Dokumen'],
        'Lokasi Gudang': ['Blok A-1', 'Zona Karantina', 'Blok B-3']
    }
    df = pd.DataFrame(data_logistik)
    st.dataframe(df, use_container_width=True)
