'''
Created on 2015. 7. 28.

@author: Jay
'''
import time
from problems.europeanVanilla import EuropeanVanillaOption

#Processing Start
start_time = time.time()  
const = EuropeanVanillaOption()

S = 100.0
r = 0.05
sigma = 0.10
T = 1.0
K = 120
NumOftimeStep = 100
NumOfSimulation = 10000
perturbation = 0.01

price = const.calcOption(S, r, sigma, T, K, NumOftimeStep, NumOfSimulation)

greekType = 'D' 
delta = const.calcGreeks(S, r, sigma, T, K, NumOftimeStep, NumOfSimulation, perturbation, greekType)

greekType = 'V' 
vega = const.calcGreeks(S, r, sigma, T, K, NumOftimeStep, NumOfSimulation, perturbation, greekType)

greekType = 'T' 
theta = const.calcGreeks(S, r, sigma, T, K, NumOftimeStep, NumOfSimulation, perturbation, greekType)

greekType = 'R' 
rho = const.calcGreeks(S, r, sigma, T, K, NumOftimeStep, NumOfSimulation, perturbation, greekType)

print "Price: " + repr(price)
print "Delta: " + repr(delta)
print "Vega: " + repr(vega)
print "Rho: " + repr(rho)
print "Theta: " + repr(theta)


#Processing End
end_time = time.time()

print end_time - start_time