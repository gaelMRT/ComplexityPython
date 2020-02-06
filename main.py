import time
import math

result = 0
"""

print("Calcul de performance 2\'000\'000\'000 opérations ")
number = 2000000000

tBefore = time.time()
for x in range(1, number):
    result += 1/x
tAfter = time.time()

dtime = tAfter - tBefore
print("%d;%f;%f;%f;%f\n" % (number,result, dtime,tBefore,tAfter))
"""
"""
print("Performance mémoire")
arr = list()
length = 1000000
tBefore = time.time()
for x in range(length):
    arr.append(x)
print("Swap begining | first = %d , last = %d" % (arr[0],arr[math.floor(len(arr)-1)]))
for x in range( math.floor(len(arr)/2)):
    tmp = arr[x]
    arr[x] = arr[math.floor(len(arr)-x-1)]
    arr[math.floor(len(arr)-x-1)] = tmp
print("Swap finished | first = %d , last = %d" % (arr[0],arr[math.floor(len(arr)-1)]))
tAfter = time.time()

dtime = tAfter - tBefore
print("%d;%f;%f;%f\n" % (len(arr),dtime,tBefore,tAfter))
"""

number = 1000000
print("Performance accès disque - %d" % number)

tBefore = time.time()
fileName = "performancea.txt"
for x in range(number):
    f = open(fileName,"a+")
    f.write("Operation %d" % x)
    f.close()
tAfter = time.time()

dtime = tAfter - tBefore
print("%d;%f;%f;%f\n" % (number,dtime,tBefore,tAfter))
   