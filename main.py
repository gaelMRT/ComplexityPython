import time

number = 1
connard = 0

for i in range(0,100):
    connard = 0
    tBefore = time.time()
    for x in range(1, number):
        connard += 1/x
    tAfter = time.time()
    dtime = tAfter - tBefore
    print("%d;%d;%f;%f" % (i,number,connard, dtime))
    number = number * 10




   