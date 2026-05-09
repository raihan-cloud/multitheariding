import threading
import time

def pelayan_latar_belakang():
    print(f"Memulai: {threading.current_thread().name}")
    # Simulasi tugas yang sangat lama (mungkin selamanya)
    while True:
        time.sleep(1)
        print(f"{threading.current_thread().name} sedang bekerja di latar belakang...")

# 1. Membuat Thread Daemon
t = threading.Thread(target=pelayan_latar_belakang, name="Daemon-Worker")
t.daemon = True  # Menetapkan status sebagai daemon

# 2. Menjalankan Thread
t.start()

# 3. Main Thread bekerja sebentar lalu selesai
time.sleep(3)
print("Main Thread sudah selesai melakukan tugasnya.")

# Karena 't' adalah daemon, saat Main Thread sampai di sini, 
# program akan langsung berhenti dan 't' akan dimatikan paksa.