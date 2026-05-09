import threading
import time

# Kita punya dua kunci
lockA = threading.Lock()
lockB = threading.Lock()

def thread_satu():
    print("Thread-1: Mencoba mengambil Lock A...")
    with lockA:
        print("Thread-1: Berhasil mengambil Lock A.")
        time.sleep(1) # Memberi waktu agar Thread-2 mengambil Lock B
        
        print("Thread-1: Mencoba mengambil Lock B...")
        with lockB:
            print("Thread-1: Berhasil mengambil Lock B.")

def thread_dua():
    print("Thread-2: Mencoba mengambil Lock B...")
    with lockB:
        print("Thread-2: Berhasil mengambil Lock B.")
        time.sleep(1) # Memberi waktu agar Thread-1 mengambil Lock A
        
        print("Thread-2: Mencoba mengambil Lock A...")
        with lockA:
            print("Thread-2: Berhasil mengambil Lock A.")

# Menjalankan thread
t1 = threading.Thread(target=thread_satu)
t2 = threading.Thread(target=thread_dua)

t1.start()
t2.start()

t1.join()
t2.join()

print("Program selesai (Ini tidak akan pernah tercetak jika terjadi deadlock)")