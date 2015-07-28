'''
Created on 2015. 7. 28.

@author: Jay
'''
import math
import random

class HullWhite():
    
    meanReversion = 0
    volatility = []
    HWVol = 0    
        
    dt = 0
    periodTenor = 0
       
    simNum = 0
    periodNum = 0
    timeNum = 0
    
    rnds = []
    
    def __init__(self, meanReversion, HWVol, 
                 simNum, Maturity, CouponFrequency, ACT, MonitorFrequency):
        
        self.meanReversion = meanReversion
        self.HWVol = HWVol        
        
        self.simNum = simNum
        self.periodNum = int(Maturity * CouponFrequency)
        self.dt = MonitorFrequency / ACT
        self.periodTenor = CouponFrequency * 30.0 / ACT
        self.timeNum = int(self.periodNum / self.dt)
        
        self.getRnds()
        
    def getRnds(self):
        for simIndex in range(0, self.simNum):
            rnd = []
            for periodIndex in range(0, self.periodNum):
                timernd = []
                for timeIndex in range(0, self.timeNum):
                    timernd.append(random.gauss(0,1))                
                rnd.append(timernd)            
            self.rnds.append(rnd)            
            
    
    def genHWX(self, rnd, initial):
        
        path = []
        path.append(initial)
        
        for index in range(1, self.timeNum) :
            
            drift = math.exp(-self.meanReversion * self.dt)
            vol = math.sqrt((1- math.exp(-2* self.meanReversion * self.dt)) / (2 * self.meanReversion))
            
            diffusion = self.HWVol 
            value = drift * path[index - 1] + diffusion * vol * rnd[index - 1]
            
            path.append(value)
        
        return path
        
    def generatePaths(self):
        for simIndex in range(0, self.simNum) :
            startTenor = 0.0
            initial = 0.0      
            hwX = []
            
            for periodIndex in range(0, self.periodNum):
                            
                hwX.append(self.genHWX(self.rnds[simIndex][periodIndex], initial))
                
                lastIndex = len(hwX[periodIndex])
                initial = hwX[periodIndex][lastIndex - 1]
                print hwX[periodIndex]
                print initial                
                   
            
            
    
        
    