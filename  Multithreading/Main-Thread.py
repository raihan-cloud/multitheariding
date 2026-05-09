import threading
import time

def tugas_anak():
    # Mengambil informasi thread yang sedang berjalan
    curr = threading.current_thread()
    print(f"Thread Anak: Nama={curr.name}, ID={threading.get_ident()}")
    time.sleep(2)
    print("Thread Anak selesai.")

# 1. Mendapatkan informasi Main Thread
main = threading.main_thread()
print(f"Main Thread: Nama={main.name}, ID={threading.get_ident()}")

# 2. Membuat thread anak
t1 = threading.Thread(target=tugas_anak, name="Si-Anak-Kecil")

# 3. Mengecek apakah thread saat ini adalah Main Thread
if threading.current_thread() is threading.main_thread():
    print("Status: Saat ini kita berada di Main Thread.")

t1.start()
t1.join()

print("Program Utama Selesai.")