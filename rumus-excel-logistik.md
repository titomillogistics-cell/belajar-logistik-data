# Dokumentasi Rumus Excel & Otomasi Logistik

File ini berisi kumpulan rumus Excel (Formula) andalan yang saya gunakan untuk mempercepat pengolahan data manifest, pengecekan data warehouse, dan operasional Exim sehari-hari.

## 1. Rumus Rekonsiliasi Data Manifest (XLOOKUP / VLOOKUP)
Digunakan untuk mencocokkan data nomor kontainer dari sistem internal dengan manifest dari pelayaran secara otomatis.

* **Formula:**
  ```excel
  =XLOOKUP(A2, 'Data_Pelayaran'!A:A, 'Data_Pelayaran'!B:B, "Data Tidak Ditemukan")
  ```
* **Fungsi:** Mencari nomor BL di kolom A2 pada sheet pelayaran, lalu menarik data status kontainernya di kolom B. Jika tidak ada, otomatis memunculkan teks peringatan agar tidak ada data yang terlewat.

## 2. Pengecekan Masa Free Time Kontainer (IF & TODAY)
Digunakan untuk memantau sisa hari *free time* kontainer di pelabuhan/depo guna menghindari biaya *demurrage* (denda).

* **Formula:**
  ```excel
  =IF((B2-TODAY())<=2, "WARNING: Segera Tarik!", "Aman")
  ```
* **Fungsi:** Jika tanggal akhir *free time* (di kolom B2) dikurangi tanggal hari ini hasilnya kurang dari atau sama dengan 2 hari, Excel akan otomatis memberikan status "WARNING".

## 3. Klasifikasi Berat Barang untuk Trucking (IF Bertingkat)
Digunakan untuk menentukan jenis armada truk yang dibutuhkan berdasarkan total berat barang (Gross Weight) secara otomatis.

* **Formula:**
  ```excel
  =IF(C2>5000, "Wingbox / Fuso", IF(C2>2000, "CDD (Double)", "CDE (Engkel)"))
  ```
* **Fungsi:** Membaca berat di kolom C2. Jika di atas 5 ton pakai Wingbox, di atas 2 ton pakai CDD, di bawah itu cukup CDE.
