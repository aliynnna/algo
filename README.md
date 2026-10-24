# Simulasi Depth-First Search (DFS): Mencari Kunci Rumah

Repository ini dibuat untuk memenuhi tugas mata kuliah Kecerdasan Buatan (AI). Proyek ini berisi implementasi sederhana dari algoritma pencarian **Depth-First Search (DFS)** menggunakan bahasa pemrograman Python.

## 📌 Deskripsi Proyek
Kode ini mensimulasikan cara kerja algoritma DFS menggunakan analogi kehidupan sehari-hari, yaitu **mencari kunci motor yang hilang di dalam rumah**. 

Alih-alih mencari di seluruh permukaan ruangan secara bersamaan, algoritma DFS bekerja dengan cara menelusuri satu rute sedalam mungkin sampai mentok (misalnya: Masuk ke Pintu Utama -> Buka Ruang Tamu -> Buka Laci TV). Jika rute tersebut buntu (kunci tidak ditemukan), pencarian akan mundur dan mencoba rute atau cabang lainnya.

## 🔍 Cara Kerja Kode
1. **Peta Rumah (Graf):** Rumah dimodelkan dalam bentuk *Dictionary* di Python. Setiap ruangan terhubung dengan tempat atau objek yang lebih spesifik di dalamnya.
2. **Tumpukan (Stack):** DFS menggunakan prinsip tumpukan *Last-In-First-Out (LIFO)*. Tempat terakhir yang dilihat adalah tempat pertama yang akan dibongkar selanjutnya.
3. **Pencarian:** Program menelusuri ruangan demi ruangan secara mendalam hingga target (`'Kunci Motor'`) ditemukan, dan mencegah pencarian berulang di tempat yang sama.

## 🚀 Cara Menjalankan Program
Pastikan Python sudah terinstal di komputer.
1. Unduh atau *clone* repository ini.
2. Buka terminal atau *command prompt*.
3. Arahkan ke folder tempat file disimpan, lalu jalankan perintah berikut:
   ```bash
   python CONTOH_SEARCHALGORYTHM.py
