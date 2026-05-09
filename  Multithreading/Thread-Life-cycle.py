import threading
import time

# Kita membuat class yang mewarisi (inheritance) dari threading.Thread
class MyThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    # Metode run() adalah inti dari status RUNNING
    def run(self):
        print(f"--- Memulai Thread: {self.name} (Status: RUNNING) ---")
        
        # Simulasi pekerjaan dengan looping
        self.print_time(self.name, self.counter, 3)
        
        print(f"--- Selesai Thread: {self.name} (Status: DEAD) ---")

    def print_time(self, thread_name, delay, counter):
        while counter:
            # Status: BLOCKED / WAITING saat time.sleep dipanggil
            time.sleep(delay)
            print(f"{thread_name}: {time.ctime(time.time())}")
            counter -= 1

# --- Alur Eksekusi ---

# 1. NEW: Membuat objek thread
thread1 = MyThread(1, "Thread-Satu", 1)
thread2 = MyThread(2, "Thread-Dua", 2)

# 2. RUNNABLE: Memanggil start() untuk mendaftarkan ke sistem
thread1.start()
thread2.start()

# Menggunakan join() agar thread utama menunggu thread anak selesai
# Ini menjaga thread utama tetap "Waiting" sampai thread anak "Dead"
thread1.join()
thread2.join()

print("\nSemua thread telah selesai. Keluar dari program utama.")