'''
Created on 2015. 7. 28.

@author: Jay
'''
import math
import time
import random
from scipy.stats.vonmises_cython import numpy
class AAD_Adjoint_EuropeanVanilla():
    
    @staticmethod
    def genStockPath(S, r, sigma, dt, rnd):
        return S + r * S * dt + sigma * S * math.sqrt(dt)* rnd
    
    @staticmethod
    def calcPayoff(S, r, T, K, callput):
        if callput == 'C' :
            return math.exp(-r*T) * max(0, S - K)
        elif callput == 'P':
            return math.exp(-r*T) * max(0, K - S)
        
    @staticmethod
    def calcOption(S, r, sigma, T, K, NumOftimeStep, NumOfSimulation, callput, rnds = []):
        dt = T / NumOftimeStep
        payoffs = []
        delta = []
        vega = []
        rho = []
        theta = []    
            
        for simIndex in range(0, NumOfSimulation):
            #For price calculation
            rnd = []
            stockPath = []    
            stockPath.append(S)
                   
            for stepIndex in range(0, NumOftimeStep):
                if len(rnds) is not 0 :
                    rnd.append(rnds[simIndex][stepIndex])
                else :
                    rnd.append(random.gauss(0, 1))
                    
                stockPath.append(AAD_Adjoint_EuropeanVanilla.genStockPath(stockPath[stepIndex], r, sigma, dt, rnd[stepIndex]))
                #print rnd[stepIndex], stockPath[stepIndex], S_dot_delta[stepIndex]
            
            #print len(rnd), len(stockPath), len(S_dot_delta)    
            
            payoffs.append(AAD_Adjoint_EuropeanVanilla.calcPayoff(stockPath[NumOftimeStep], r, T, K, callput))
            #print payoffs[simIndex]
    
            #For greeks calculation
            flag = 0
            if callput == 'C' :
                flag = 1 if stockPath[NumOftimeStep] > K else 0
            elif callput == 'P' :
                flag = -1 if stockPath[NumOftimeStep] < K else 0
            
            S_bar = math.exp(-r * T) * flag
            r_bar = -math.exp(-r * T) * T  * flag * (stockPath[NumOftimeStep] - K)
            sigma_bar = 0
            T_bar = math.exp(-r * T) * flag * (stockPath[NumOftimeStep] - K) * r
            K_bar = - math.exp(-r * T) * flag
            
            for stepIndex in range(NumOftimeStep - 1, 0, -1):
                #print stepIndex
                r_bar = r_bar + stockPath[stepIndex] * dt * S_bar
                sigma_bar = sigma_bar + stockPath[stepIndex] * math.sqrt(dt) * rnd[stepIndex] * S_bar
                T_bar = T_bar - (r * stockPath[stepIndex] + 0.5 * sigma * stockPath[stepIndex] * rnd[stepIndex] / math.sqrt(dt)) * S_bar / NumOftimeStep            
                S_bar = (1 + r * dt + sigma * math.sqrt(dt) * rnd[stepIndex]) * S_bar
            
            delta.append(S_bar)
            vega.append(sigma_bar)
            rho.append(r_bar)
            theta.append(T_bar)
            
        price = numpy.average(payoffs)
        print "Price: " + repr(price)
        print "Delta: " + repr(numpy.average(delta))
        print "Vega: " + repr(numpy.average(vega))
        print "Rho: " + repr(numpy.average(rho))
        print "Theta: " + repr(numpy.average(theta))
    
#===============================================================================
#     
# #Processing Start
# start_time = time.time()
# 
# S = 100.0
# r = 0.05
# sigma = 0.10
# T = 1.0
# K = 120
# 
# NumOftimeStep = 100
# NumOfSimulation = 10000
# 
# 
# AAD_Adjoint_EuropeanVanilla.calcOption(S, r, sigma, T, K, NumOftimeStep, NumOfSimulation)
# 
# #Processing End
# end_time = time.time()
# 
# print end_time - start_time
#===============================================================================
