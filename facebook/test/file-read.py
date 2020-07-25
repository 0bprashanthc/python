import multiprocessing as mp
import sys
import os

def chunkify(fname, size=5000):
    fsize = os.path.getsize(fname)
    with open(fname) as f:
        fend = f.tell()
        while True:
            fstart = fend
            f.seek(size,1)
            f.readline()
            fend = f.tell()
            yield fstart, fend-fstart
            if fend > fsize:
                return

def process(fname, fstart, size):
    with open(fname) as f:
        f.seek(fstart)
        lines = f.readlines()
        for line in lines:
            process(line)

pool = mp.Pool(mp.cpu_count())
jobs = list()
fname = sys.argv[1]
for fstart,size in chunkify(fname):
    jobs.append(pool.apply_async(process,(fname,fstart,size)))
for job in jobs:
    job.get()
pool.close()
