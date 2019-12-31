from threading import Thread
import threading
import time
import os

# Définir la fonction à évaluer
def calcul_long():
    print("pid:" + str(os.getpid()))
    n = 1E7
    while n>0:
        n -= 1

def multiThreads():

    class myThread (threading.Thread):   #hériter la class threading.Thread
        def __init__(self, threadID, name):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name

        def run(self):
            print("Démarrer: " + self.name)
            calcul_long()
            print("Fin du thread: " + self.name)

    # Créer nouveaux threads
    thread1 = myThread(1, "Thread-1")
    thread2 = myThread(2, "Thread-2")
    thread3 = myThread(3, "Thread-3")
    thread4 = myThread(4, "Thread-4")
    thread5 = myThread(5, "Thread-5")

    # Lancer threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    # Attend que les threads se terminent
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    print("Exiting Main Thread")

# Main
if __name__ == "__main__":
    start = time.time()

    multiThreads()

    end = time.time()
    print("Temps d'exécution du processeur:", end - start)