from concurrent.futures import ThreadPoolExecutor
import time

# Fungsi yang akan dikerjakan oleh thread
def tugas_berat(n):
    print(f"Mengerjakan tugas {n}...")
    time.sleep(2)
    return f"Hasil tugas {n} selesai"

# --- Menggunakan ThreadPoolExecutor ---

# Kita tentukan max_workers=3, artinya hanya ada 3 thread yang bekerja simultan
with ThreadPoolExecutor(max_workers=3) as executor:
    # Mengirim tugas ke pool menggunakan map
    tugas_list = [1, 2, 3, 4, 5]
    hasil = executor.map(tugas_berat, tugas_list)

# Mengambil hasil setelah semua selesai
print("\nSemua hasil:")
for r in hasil:
    print(r)

print("\nProgram Utama Selesai.")