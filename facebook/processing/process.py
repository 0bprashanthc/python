import multiprocessing as mp
import time
import random

def myfunc(x):
    print(mp.current_process())
    time.sleep(5)
    print(random.random())

if __name__ == "__main__":
    pool = mp.Pool(mp.cpu_count())
    result = pool.map(myfunc,[x for x in range(4)])
