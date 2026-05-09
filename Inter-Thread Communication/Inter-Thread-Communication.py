import threading
import time

# Membuat objek Event
event = threading.Event()

def tugas_menunggu():
    print(f"{threading.current_thread().name} sedang menunggu sinyal...")
    # Thread ini akan berhenti di sini sampai event.set() dipanggil
    event.wait() 
    print(f"{threading.current_thread().name} mendapat sinyal! Mulai bekerja...")

def tugas_pemberi_sinyal():
    print(f"{threading.current_thread().name} sedang menyiapkan sesuatu...")
    time.sleep(3) # Simulasi persiapan selama 3 detik
    print(f"{threading.current_thread().name} mengirim sinyal!")
    event.set() # Mengubah status event menjadi 'True'

# Membuat thread
t1 = threading.Thread(target=tugas_menunggu, name="Pekerja")
t2 = threading.Thread(target=tugas_pemberi_sinyal, name="Manager")

# Menjalankan thread
t1.start()
t2.start()

t1.join()
t2.join()

print("Program selesai.")