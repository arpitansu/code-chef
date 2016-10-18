for _ in xrange(input()):
    totalCars = input()# number of cars
    speeds = map(int,raw_input().split())# speeds for ex input = 1 2 3 4
    speedBestPos=speeds[0] # keeping speed of pos 1
    counter=0# you know what is this
    for i in xrange(totalCars):# some chutiyapa find out on your own
        if speeds[i] <= speedBestPos:
            speedBestPos=speeds[i]
            counter+=1
    print (counter)