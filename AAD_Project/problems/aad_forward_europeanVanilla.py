'''
Created on 2015. 7. 27.

@author: Jay
'''
import math
import random
from scipy.stats.vonmises_cython import numpy
import time

class AAD_Tangent_EuropeanVanilla():

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
    def calcSenOfStockPath(S, r, sigma, dt, rnd, NumOfStep, S_dot, r_dot, sigma_dot, T_dot):
        return (1 + r*dt + sigma * math.sqrt(dt) * rnd) * S_dot + \
            S * dt * r_dot + \
            S * math.sqrt(dt) * rnd * sigma_dot - \
            (r * S + 0.5 * sigma * S * rnd / math.sqrt(dt)) * T_dot / NumOfStep
    
    @staticmethod
    def calcPayoffSen(S, r, T, K, S_dot, K_dot, r_dot, T_dot, callput):
        flag = 0
        if callput == 'C' :
            flag = 1 if S > K else 0
        elif callput == 'P':
            flag = -1 if S < K else 0
                    
        return math.exp(-r * T) * (S_dot - K_dot + (S - K) * (- T * r_dot + r * T_dot)) * flag
    
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
            stockPaths = []    
            stockPaths.append(S)
            
            #For greeks calculation
            S_dot_delta = []
            S_dot_vega = []
            S_dot_rho = []
            S_dot_theta = []
            S_dot_delta.append(1)
            S_dot_vega.append(0)
            S_dot_rho.append(0)
            S_dot_theta.append(0)        
            
            for stepIndex in range(0, NumOftimeStep):
                if len(rnds) is not 0 :
                    rnd.append(rnds[simIndex][stepIndex])
                else :
                    rnd.append(random.gauss(0, 1))
                    
                stockPaths.append(AAD_Tangent_EuropeanVanilla.genStockPath(stockPaths[stepIndex], r, sigma, dt, rnd[stepIndex]))
                
                S_dot_delta.append(AAD_Tangent_EuropeanVanilla.calcSenOfStockPath(stockPaths[stepIndex], r, sigma, dt, rnd[stepIndex], NumOftimeStep, S_dot_delta[stepIndex], 0, 0, 0))
                S_dot_vega.append(AAD_Tangent_EuropeanVanilla.calcSenOfStockPath(stockPaths[stepIndex], r, sigma, dt, rnd[stepIndex], NumOftimeStep,S_dot_vega[stepIndex], 0, 1, 0))
                S_dot_rho.append(AAD_Tangent_EuropeanVanilla.calcSenOfStockPath(stockPaths[stepIndex], r, sigma, dt, rnd[stepIndex], NumOftimeStep,S_dot_rho[stepIndex], 1, 0, 0))
                S_dot_theta.append(AAD_Tangent_EuropeanVanilla.calcSenOfStockPath(stockPaths[stepIndex], r, sigma, dt, rnd[stepIndex], NumOftimeStep,S_dot_theta[stepIndex], 0, 0, 1))
                
                #print rnd[stepIndex], stockPaths[stepIndex], S_dot_delta[stepIndex]
            
            #print len(rnd), len(stockPaths), len(S_dot_delta)    
            #def calcPayoffSen(S, r, T, K, S_dot_delta, K_dot, r_dot, T_dot):
            payoffs.append(AAD_Tangent_EuropeanVanilla.calcPayoff(stockPaths[NumOftimeStep], r, T, K, callput))
            
            delta.append(AAD_Tangent_EuropeanVanilla.calcPayoffSen(stockPaths[NumOftimeStep], r, T, K, S_dot_delta[NumOftimeStep], 0, 0, 0, callput))
            vega.append(AAD_Tangent_EuropeanVanilla.calcPayoffSen(stockPaths[NumOftimeStep], r, T, K, S_dot_vega[NumOftimeStep], 0, 0, 0, callput))
            rho.append(AAD_Tangent_EuropeanVanilla.calcPayoffSen(stockPaths[NumOftimeStep], r, T, K, S_dot_rho[NumOftimeStep], 0, 1, 0, callput))
            theta.append(AAD_Tangent_EuropeanVanilla.calcPayoffSen(stockPaths[NumOftimeStep], r, T, K, S_dot_theta[NumOftimeStep], 0, 0, 1, callput))
            #print payoffs[simIndex]
        
        price = numpy.average(payoffs)
        print "Price: " + repr(price)
        print "Delta: " + repr(numpy.average(delta))
        print "Vega: " + repr(numpy.average(vega))
        print "Rho: " + repr(numpy.average(rho))
        print "Theta: " + repr(numpy.average(theta))



#===============================================================================
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
# calcOption(S, r, sigma, T, K, NumOftimeStep, NumOfSimulation)
# 
# #Processing End
# end_time = time.time()
# 
# print end_time - start_time
#===============================================================================

