import threading
import time

class MyThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      # Memberi nama thread melalui atribut .name
      self.name = name
      self.counter = counter

   def run(self):
      # threading.current_thread().name digunakan untuk mengambil nama thread yang sedang aktif
      print(f"Starting {threading.current_thread().name}")
      print_time(self.name, self.counter, 5)
      print(f"Exiting {threading.current_thread().name}")

def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print(f"{threadName}: {time.ctime(time.time())}")
      counter -= 1

# --- Membuat Thread dengan Nama Kustom ---

# Cara 1: Lewat parameter 'name' (paling umum)
thread1 = MyThread(1, "Proses-Input", 1)
thread2 = MyThread(2, "Proses-Output", 2)

# Mengubah nama thread yang sudah dibuat (opsional)
thread1.name = "Worker-Data-1"

# Menjalankan thread
thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Exiting Main Thread")