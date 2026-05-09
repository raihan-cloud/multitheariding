import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name, duration):
        threading.Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        print(f"--> {self.name} mencoba mendapatkan waktu CPU.")
        # Saat sleep dipanggil, Thread Scheduler akan memindahkan fokus ke thread lain
        time.sleep(self.duration)
        print(f"<-- {self.name} selesai dieksekusi setelah {self.duration} detik.")

# Membuat beberapa thread dengan durasi kerja berbeda
t1 = MyThread("Thread-Cepat", 1)
t2 = MyThread("Thread-Lama", 3)
t3 = MyThread("Thread-Sedang", 2)

# Memulai thread
# Urutan start() tidak menjamin urutan eksekusi yang pasti oleh OS
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("Main Thread: Semua thread telah dijadwalkan dan selesai.")