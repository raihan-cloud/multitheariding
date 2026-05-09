import queue
import threading
import time

exitFlag = 0

class MyThread (threading.Thread):
   def __init__(self, threadID, name, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.q = q
   
   def run(self):
      print ("Starting " + self.name)
      self.process_data()
      print ("Exiting " + self.name)

   def process_data(self):
      while not exitFlag:
         queueLock.acquire()
         if not workQueue.empty():
            data = self.q.get()
            queueLock.release()
            print ("%s processing %s" % (self.name, data))
         else:
            queueLock.release()
         time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["Satu", "Dua", "Tiga", "Empat", "Lima"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# 1. Membuat thread baru
for tName in threadList:
   thread = MyThread(threadID, tName, workQueue)
   thread.start()
   threads.append(thread)
   threadID += 1

# 2. Mengisi antrean (Queue)
queueLock.acquire()
for word in nameList:
   workQueue.put(word)
queueLock.release()

# 3. Menunggu antrean kosong
while not workQueue.empty():
   pass

# 4. Memberitahu thread untuk berhenti
exitFlag = 1

# 5. Menunggu semua thread selesai
for t in threads:
   t.join()

print ("Exiting Main Thread")