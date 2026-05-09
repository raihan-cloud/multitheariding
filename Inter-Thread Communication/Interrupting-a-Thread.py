import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        # Bendera untuk mengontrol status thread
        self._stop_event = threading.Event()

    def stop(self):
        # Mengirim sinyal untuk berhenti
        self._stop_event.set()

    def stopped(self):
        # Mengecek apakah sinyal berhenti sudah dikirim
        return self._stop_event.is_set()

    def run(self):
        print(f"Thread {self.name} mulai bekerja...")
        
        while not self.stopped():
            print(f"Thread {self.name} masih berjalan...")
            time.sleep(1)
            
        print(f"Thread {self.name} menerima interupsi dan berhenti dengan rapi.")

# --- Eksekusi ---

t1 = MyThread("Pekerja-1")
t1.start()

# Biarkan thread berjalan selama 3 detik
time.sleep(3)

# Menginterupsi thread
print("Main Thread: Mengirim sinyal interupsi...")
t1.stop()

# Menunggu hingga thread benar-benar berhenti
t1.join()

print("Program Utama Selesai.")