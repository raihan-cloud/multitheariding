import threading
import time

# Fungsi yang akan dijalankan di dalam thread
def cetak_pesan(nama, jeda):
    print(f"Memulai thread: {nama}")
    time.sleep(jeda)
    print(f"Thread {nama} selesai setelah {jeda} detik")

# Membuat thread
t1 = threading.Thread(target=cetak_pesan, args=("Thread-1", 2))
t2 = threading.Thread(target=cetak_pesan, args=("Thread-2", 4))

# Menjalankan thread
t1.start()
t2.start()

# Menunggu semua thread selesai
t1.join()
t2.join()

print("Semua tugas selesai, keluar dari program utama.")