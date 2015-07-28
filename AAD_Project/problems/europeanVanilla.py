'''
Created on 2015. 7. 28.

@author: Jay
'''
import math
import random
from scipy.stats.vonmises_cython import numpy
import time

class EuropeanVanillaOption():

    rnds = []
    rndFlag = False
    
    def __init__(self, rnds):
        '''
        Constructor
        '''
        self.rnds = rnds
        if len(rnds) is not 0 :
            self.rndFlag = True
        
        
    def genStockPath(self, S, r, sigma, dt, rnd):
        return S + r * S * dt + sigma * S * math.sqrt(dt)* rnd

    def calcPayoff(self, S, r, T, K, callput):
        if callput == 'C' :
            return math.exp(-r*T) * max(0, S - K)
        elif callput == 'P':
            return math.exp(-r*T) * max(0, K - S)
            
    def calcOption(self, S, r, sigma, T, K, NumOftimeStep, NumOfSimulation, callput):
        dt = T / NumOftimeStep
        payoffs = []
        
        for simIndex in range(0, NumOfSimulation):
            #For price calculation
            rnd = []
            stockPaths = []    
            stockPaths.append(S)
            
            for stepIndex in range(0, NumOftimeStep):
                if self.rndFlag is True :
                    rnd.append(self.rnds[simIndex][stepIndex])
                else :
                    rnd.append(random.gauss(0, 1))
                     
                stockPaths.append(self.genStockPath(stockPaths[stepIndex], r, sigma, dt, rnd[stepIndex]))
                #print rnd[stepIndex], stockPaths[stepIndex], S_dot_delta[stepIndex]
            
            #print len(rnd), len(stockPaths), len(S_dot_delta)    
            #def calcPayoffSen(S, r, T, K, S_dot_delta, K_dot, r_dot, T_dot):
            payoffs.append(self.calcPayoff(stockPaths[NumOftimeStep], r, T, K, callput))
            #print payoffs[simIndex]
            if self.rndFlag is False :
                self.rnds.append(rnd)
                
        price = numpy.average(payoffs)
        
        if self.rndFlag is False : self.rndFlag = True
             
        return price
        
    def calcGreeks(self, S, r, sigma, T, K, NumOftimeStep, NumOfSimulation, perturbation, greekType, callput):
        upPrice = 0
        downPrice = 0
        exposure = 0
        
        if greekType == 'D' :
            #delta
            exposure = S
            upValue =  exposure * (1 + perturbation)
            downValue = exposure * (1 - perturbation)
            upPrice = self.calcOption(upValue, r, sigma, T, K, NumOftimeStep, NumOfSimulation, callput)
            downPrice = self.calcOption(downValue, r, sigma, T, K, NumOftimeStep, NumOfSimulation, callput)
        elif greekType == 'V':    
            #delta
            exposure = sigma
            upValue =  exposure * (1 + perturbation)
            downValue = exposure * (1 - perturbation)
            upPrice = self.calcOption(S, r, upValue, T, K, NumOftimeStep, NumOfSimulation, callput)
            downPrice = self.calcOption(S, r, downValue, T, K, NumOftimeStep, NumOfSimulation, callput)
        elif greekType == 'R':
            #delta
            exposure = r
            upValue =  exposure * (1 + perturbation)
            downValue = exposure * (1 - perturbation)
            upPrice = self.calcOption(S, upValue, sigma, T, K, NumOftimeStep, NumOfSimulation, callput)
            downPrice = self.calcOption(S, downValue, sigma, T, K, NumOftimeStep, NumOfSimulation, callput)
        elif greekType == 'T':
            #delta
            exposure = T
            upValue =  exposure * (1 + perturbation)
            downValue = exposure * (1 - perturbation)
            upPrice = - self.calcOption(S, r, sigma, upValue, K, NumOftimeStep, NumOfSimulation, callput)
            downPrice = - self.calcOption(S, r, sigma, downValue, K, NumOftimeStep, NumOfSimulation, callput)
        
        return (upPrice - downPrice) / (2 * perturbation * exposure)
