import threading
import time

class MyThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter

   def run(self):
      print(f"Starting {self.name}")
      # Simulasi beban kerja
      time.sleep(self.counter)
      print(f"Exiting {self.name}")

# 1. Membuat thread baru
thread1 = MyThread(1, "Thread-1", 2) # Butuh 2 detik
thread2 = MyThread(2, "Thread-2", 4) # Butuh 4 detik

# 2. Menjalankan thread
thread1.start()
thread2.start()

# 3. Bergabung (Joining)
# Main thread akan berhenti di sini dan menunggu thread1 selesai
thread1.join()
print("Main Thread: Thread-1 sudah selesai!")

# Main thread kemudian menunggu thread2 selesai
thread2.join()
print("Main Thread: Thread-2 sudah selesai!")

print("Exiting Main Thread. Semua tugas beres.")