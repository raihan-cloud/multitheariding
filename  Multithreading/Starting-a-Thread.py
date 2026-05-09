import threading
import time

# Mendefinisikan class thread
class MyThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter

   def run(self):
      print ("Starting " + self.name)
      # Memanggil fungsi pembantu untuk mencetak waktu
      print_time(self.name, self.counter, 5)
      print ("Exiting " + self.name)

# Fungsi pembantu untuk simulasi beban kerja
def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

# --- TAHAP STARTING THREAD ---

# 1. Create new threads (Membuat)
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

# 2. Start new Threads (Menjalankan)
# Ini akan memicu metode run() di dalam thread baru
thread1.start()
thread2.start()

# 3. Join threads (Sinkronisasi akhir)
# Tanpa join, program utama akan langsung mencetak "Exiting Main Thread" 
# meskipun thread-1 dan thread-2 masih berjalan.
thread1.join()
thread2.join()

print ("Exiting Main Thread")