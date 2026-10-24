# Ini adalah 'Peta' rumah kita.
# Di sebelah kiri adalah ruangan, di sebelah kanan (dalam kurung siku) adalah isinya.
rumah = {
    'Pintu Masuk': ['Ruang Tamu', 'Dapur'],
    'Ruang Tamu': ['Bawah Sofa', 'Laci TV'],
    'Dapur': ['Meja Makan', 'Kulkas'],
    'Bawah Sofa': [],
    'Laci TV': ['Kunci Motor'],  # Nah, kuncinya terselip di dalam Laci TV!
    'Meja Makan': [],
    'Kulkas': [],
    'Kunci Motor': []
}

def cari_barang_dfs(peta, posisi_awal, barang_dicari):
    # Dalam DFS, kita menggunakan sistem "Tumpukan" (seperti tumpukan piring).
    # Tempat yang TERAKHIR kali kita lihat, itu yang akan kita bongkar duluan.
    tumpukan = [[posisi_awal]]
    sudah_diperiksa = set()

    while tumpukan:
        # pop() tanpa angka nol di dalam kurung berarti mengambil data paling akhir (paling atas dari tumpukan).
        # Ini rahasia utama algoritma DFS!
        jalur = tumpukan.pop()
        tempat_sekarang = jalur[-1]

        # 1. Cek: Apakah ini barang yang kita cari?
        if tempat_sekarang == barang_dicari:
            return jalur

        # 2. Jika bukan, dan tempat ini belum pernah kita periksa...
        if tempat_sekarang not in sudah_diperiksa:
            # Tandai tempat ini supaya kita tidak mencari dua kali di tempat yang sama
            sudah_diperiksa.add(tempat_sekarang)
            
            # Cek ada apa saja di dalam tempat ini, lalu masukkan ke daftar pencarian selanjutnya
            isi_tempat_ini = peta[tempat_sekarang]
            for tempat_selanjutnya in isi_tempat_ini:
                jalur_baru = list(jalur)
                jalur_baru.append(tempat_selanjutnya)
                tumpukan.append(jalur_baru)

    # 3. Jika semua tempat sudah dibongkar dan tidak ketemu
    return "Barang tidak ada di rumah"

# Mari kita suruh komputernya mencari!
hasil_pencarian = cari_barang_dfs(rumah, 'Pintu Masuk', 'Kunci Motor')
print("Langkah-langkah menemukan kunci:", hasil_pencarian)