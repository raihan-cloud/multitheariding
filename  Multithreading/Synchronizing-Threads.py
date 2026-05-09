import threading
import time

class MyThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter

   def run(self):
      print ("Starting " + self.name)
      # 1. Dapatkan kunci untuk mensinkronisasi thread
      threadLock.acquire()
      
      # Hanya satu thread yang bisa menjalankan fungsi ini di satu waktu
      print_time(self.name, self.counter, 3)
      
      # 2. Lepaskan kunci untuk thread berikutnya
      threadLock.release()
      print ("Exiting " + self.name)

def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

# Membuat objek Lock
threadLock = threading.Lock()
threads = []

# Membuat thread baru
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

# Menjalankan thread
thread1.start()
thread2.start()

# Menambahkan thread ke daftar threads
threads.append(thread1)
threads.append(thread2)

# Menunggu semua thread selesai
for t in threads:
   t.join()

print ("Exiting Main Thread")