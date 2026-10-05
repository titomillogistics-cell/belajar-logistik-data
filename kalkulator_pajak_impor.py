# =================================================================
# KALKULATOR BEA MASUK & PAJAK IMPOR (LOGISTIK VERSION)
# Dibuat untuk otomasi hitungan awal barang masuk di Gudang MM2100
# =================================================================

def hitung_pajak_impor(cif_value, tarif_bea_masuk_persen):
    # 1. Hitung Nilai Bea Masuk (BM)
    bea_masuk = cif_value * (tarif_bea_masuk_persen / 100)
    
    # 2. Hitung Nilai Impor (Nilai CIF + Bea Masuk) sebagai dasar PPN
    nilai_impor = cif_value + bea_masuk
    
    # 3. Hitung PPN (Pajak Pertambahan Nilai) standar saat ini sebesar 11%
    ppn = nilai_impor * 0.11
    
    # 4. Total tagihan pajak yang harus dibayar ke Bea Cukai
    total_pajak = bea_masuk + ppn
    
    # Menampilkan hasil simulasi hitungan
    print(f"--- SIMULASI PERHITUNGAN PAJAK IMPOR ---")
    print(f"Nilai Barang (CIF) : Rp {cif_value:,.2f}")
    print(f"Biaya Bea Masuk    : Rp {bea_masuk:,.2f}")
    print(f"Biaya PPN (11%)    : Rp {ppn:,.2f}")
    print(f"========================================")
    print(f"TOTAL WAJIB BAYAR  : Rp {total_pajak:,.2f}")

# CONTOH KASUS: Barang masuk dengan nilai CIF Rp 50.000.000 dan Bea Masuk 7.5%
hitung_pajak_impor(cif_value=50000000, tarif_bea_masuk_persen=7.5)
