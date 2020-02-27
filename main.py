#!/bin/python3
import time
import math

FILE_RESULT_PERF = "resultPerf.csv"
FILE_RESULT_MEMO = "resultMemo.csv"
FILE_RESULT_DISK = "resultDisk.csv"


def CalculPerformance(number,file):
    print("Calcul de performance "+str(number)+" opérations ")
    result = 0
    tBefore = time.time()
    for x in range(1, number):
        result += 1/x
    tAfter = time.time()

    dtime = tAfter - tBefore
    print("iteration %d;resultat %f;temps (sec) %f\n" % (number,result, dtime))
    file.write("%d;%f\n" % (number,dtime))

def CalculMemoire(length,file):
    print("Performance mémoire")
    arr = list()
    tBefore = time.time()
    for x in range(length):
        arr.append(x)
    print("Swap begining | first = %d , last = %d" % (arr[0],arr[-1]))
    for x in range( math.floor(length/2)):
        tmp = arr[x]
        id2 = (-x-1)
        arr[x] = arr[id2]
        arr[id2] = tmp
    print("Swap finished | first = %d , last = %d" % (arr[0],arr[-1]))
    tAfter = time.time()

    dtime = tAfter - tBefore
    print("iteration %d;temps(sec) %f\n" % (length,dtime))
    file.write("%d;%f\n" % (length,dtime))

def CalculDisque(number,file):
    print("Performance accès disque - %d" % number)

    tBefore = time.time()
    fileName = "performancea.txt"
    for x in range(number):
        f = open(fileName,"w+")
        f.write("Operation %d" % x)
        f.close()
    tAfter = time.time()

    dtime = tAfter - tBefore
    print("iteration %d;temps(sec) %f\n" % (number,dtime))
    file.write("%d;%f\n" % (number,dtime))

    

fPerf = open(FILE_RESULT_PERF,'w+')
fPerf.write("Interations;Temps(sec)\n")
i = 20
while(i <= 2000000000):
    CalculPerformance(i,fPerf)
    i*= 10
fPerf.close()


fMemo = open(FILE_RESULT_MEMO,'w+')
fMemo.write("Interations;Temps(sec)\n")
i = 10
while(i <= 1000000):
    CalculMemoire(i,fMemo)
    i*= 10
fMemo.close()

fDisk = open(FILE_RESULT_DISK,'w+')
fDisk.write("Interations;Temps(sec)\n")
i = 10
while(i <= 100000):
    CalculDisque(i,fDisk)
    i*= 10
fDisk.close()
