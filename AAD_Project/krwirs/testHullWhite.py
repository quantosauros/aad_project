'''
Created on 2015. 7. 28.

@author: Jay
'''
import random

#input parameters
Maturity = 10.0
#Num of payment per year
CouponFrequency = 4.0
MonitorFrequency = 30.0
ACT = 365.0
simNum = 10

#intermediate variables
periodNum = Maturity * CouponFrequency
dt = MonitorFrequency / ACT
periodTenor = CouponFrequency * 30.0 / ACT
rnds = []
timeNum = periodTenor / dt

print periodNum, dt, periodTenor, timeNum

for simIndex in range(0, simNum):
    startTenor = 0
    initial = 0
    
    hwX = []
    
    for periodIndex in range(0, int(periodNum)) :
        rnd = []
        for timeIndex in range(0, int(timeNum)) :                        
            rnd.append(random.gauss(0, 1))        
        
    rnds.append(rnd) 
        
        