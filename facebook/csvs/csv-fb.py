import sys
import csv
import math

G = 9.8
r1,r2 = open(sys.argv[1]),open(sys.argv[2])
csv1,csv2 = csv.DictReader(r1), csv.DictReader(r2)
bipedals = dict()

for line in csv2:
    if line['STANCE']=='bipedal':
        bipedals[line['NAME']] = [float(line['STRIDE_LENGTH'])]

for line in csv1:
    if line['NAME'] in bipedals:
        bipedals[line['NAME']].append(float(line['LEG_LENGTH']))

for name,params in bipedals.items():
    if len(params) > 1:
        #speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g) 
        speed = ((params[0]/params[1])-1)*math.sqrt(params[1]*G)
        if speed in bipedals:
            bipedals[speed].append(name)
        else:
            bipedals[speed] = [name]
        del bipedals[name]
    else:
        del bipedals[name]

for speed in sorted(list(bipedals.keys()),reverse=True):
    print(bipedals[speed])
