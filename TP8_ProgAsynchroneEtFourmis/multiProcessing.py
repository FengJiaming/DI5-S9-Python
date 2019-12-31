import timeit
from multiprocessing import Process
import os

# Définir la fonction à calculer
def calcul_long(name):
    print("pid:" + str(os.getpid()) + " exécute")
    n = 1E7
    while n>0:
        n -= 1

if __name__ == '__main__':
    start = timeit.default_timer()
    processes = [Process(target=calcul_long, args=('process'+str(i),)) for i in range(10)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    end = timeit.default_timer()
    print("Temps d'exécution du processeur:", end - start)