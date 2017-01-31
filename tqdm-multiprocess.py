#!/usr/bin/env python
# coding: utf-8

from tqdm import tqdm
from multiprocessing import Pool
from time import sleep
from random import random

def all_ops(delayset):
    pbar = tqdm(total=len(delayset))
    def cb(x):
        pbar.update(1)
    pool = Pool()
    for delay in delayset:
        pool.apply_async(sleep, args=(delay,), callback=cb)
    pool.close()
    pool.join()
    pbar.close()

if __name__ == '__main__':
    ds = [random() for n in range(100)]
    all_ops(ds)
