#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:01:05 2023

@author: carlosdm
"""
from multiprocessing import Process
from multiprocessing import BoundedSemaphore
from multiprocessing import Value
N= 8


semaphore = BoundedSemaphore(1)

def task(common, tid, semaphore): 
    for i in range(10):
        print(f'{tid}−{i}: Non−critical Section')
        print(f'{tid}−{i}: End of non−critical Section') 
        semaphore.acquire()
        print(f'{tid}−{i}: Giving up') 
        print(f'{tid}−{i}: Critical section')
        v = common.value + 1 
        print(f'{tid}−{i}: Inside critical section') 
        common.value = v
        print(f'{tid}−{i}: End of critical section') 
        semaphore.release()
def main(): 
    lp = []
    common = Value('i', 0) 
    for tid in range(N):
        lp.append(Process(target=task, args=(common, tid, semaphore))) 
    print (f"Valor inicial del contador {common.value}")
    for p in lp:
        p.start()
    for p in lp: 
        p.join()
    print (f"Valor final del contador {common.value}") 
    print ("fin")

if __name__ == "__main__": 
    main()