import threading
import time

# Fungsi yang akan dijalankan oleh thread
def print_nama_dan_waktu(nama_thread, jeda):
    count = 0
    while count < 5:
        time.sleep(jeda)
        count += 1
        print(f"{nama_thread}: {time.ctime(time.time())}")

# Membuat thread dengan target fungsi di atas
try:
    t1 = threading.Thread(target=print_nama_dan_waktu, args=("Thread-1", 2, ))
    t2 = threading.Thread(target=print_nama_dan_waktu, args=("Thread-2", 4, ))

    # Menjalankan thread
    t1.start()
    t2.start()
except:
    print("Error: tidak dapat menjalankan thread")

# Menunggu thread selesai (opsional tapi disarankan)
t1.join()
t2.join()
print("\nSelesai menjalankan fungsi biasa.")