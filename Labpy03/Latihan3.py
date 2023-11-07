# Modal awal
modal_awal = 100000000  # 100 juta

# Inisialisasi total keuntungan
total_keuntungan = 0

# Bulan 1 dan 2
total_keuntungan += 0  # Tidak ada laba pada bulan 1
total_keuntungan += 0  # Tidak ada laba pada bulan 2

# Bulan 3
total_keuntungan += modal_awal * 0.01  # Laba 1% dari modal awal

# Bulan 4
total_keuntungan += 0  # Tidak ada peningkatan laba

# Bulan 5
total_keuntungan += modal_awal * 0.05  # Laba 5% dari modal awal

# Bulan 6 dan 7
total_keuntungan += 0  # Tidak ada peningkatan laba pada bulan 6 dan 7

# Bulan 8
total_keuntungan += modal_awal * 0.03  # Laba 3% dari modal awal

# Total keuntungan selama 8 bulan
print("Total Keuntungan selama 8 bulan adalah: Rp", total_keuntungan)