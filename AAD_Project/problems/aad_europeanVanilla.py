'''
Created on 2015. 7. 28.

@author: Jay
'''
import time
from problems.europeanVanilla import EuropeanVanillaOption
from problems.aad_adjoint_europeanVanilla import AAD_Adjoint_EuropeanVanilla
from problems.aad_forward_europeanVanilla import AAD_Tangent_EuropeanVanilla
import random

#input parameters
#1

#===============================================================================
# S = 100.0
# r = 0.05
# sigma = 0.10
# T = 5.0
# K = 120
# NumOftimeStep = int(T * 54)
# NumOfSimulation = 10000
# perturbation = 0.01
# rnds = []
# callput = 'C'
#===============================================================================

#2

#===============================================================================
# S = 100.0
# r = 0.05
# sigma = 0.10
# T = 5.0
# K = 120
# NumOftimeStep = int(T * 54)
# NumOfSimulation = 10000
# perturbation = 0.01
# rnds = []
# callput = 'P'
#===============================================================================

#3

#===============================================================================
# S = 100.0
# r = 0.05
# sigma = 0.10
# T = 5.0
# K = 80
# NumOftimeStep = int(T * 54)
# NumOfSimulation = 10000
# perturbation = 0.01
# rnds = []
# callput = 'C'
#===============================================================================

#4

#===============================================================================
# S = 100.0
# r = 0.05
# sigma = 0.10
# T = 5.0
# K = 80
# NumOftimeStep = int(T * 54)
# NumOfSimulation = 10000
# perturbation = 0.01
# rnds = []
# callput = 'P'
#===============================================================================

#5

#===============================================================================
# S = 100.0
# r = 0.05
# sigma = 0.10
# T = 5.0
# K = 100
# NumOftimeStep = int(T * 54)
# NumOfSimulation = 10000
# perturbation = 0.01
# rnds = []
# callput = 'C'
#===============================================================================

#6

#===============================================================================
# S = 100.0
# r = 0.05
# sigma = 0.10
# T = 5.0
# K = 100
# NumOftimeStep = int(T * 54)
# NumOfSimulation = 10000
# perturbation = 0.01
# rnds = []
# callput = 'P'
#===============================================================================

#7

#===============================================================================
# S = 100.0
# r = 0.05
# sigma = 0.30
# T = 5.0
# K = 120
# NumOftimeStep = int(T * 54)
# NumOfSimulation = 10000
# perturbation = 0.01
# rnds = []
# callput = 'C'
#===============================================================================

#8

#===============================================================================
# S = 100.0
# r = 0.05
# sigma = 0.30
# T = 5.0
# K = 120
# NumOftimeStep = int(T * 54)
# NumOfSimulation = 10000
# perturbation = 0.01
# rnds = []
# callput = 'P'
#===============================================================================

#9

#===============================================================================
# S = 100.0
# r = 0.05
# sigma = 0.30
# T = 5.0
# K = 80
# NumOftimeStep = int(T * 54)
# NumOfSimulation = 10000
# perturbation = 0.01
# rnds = []
# callput = 'C'
#===============================================================================

#10

#===============================================================================
# S = 100.0
# r = 0.05
# sigma = 0.30
# T = 5.0
# K = 80
# NumOftimeStep = int(T * 54)
# NumOfSimulation = 10000
# perturbation = 0.01
# rnds = []
# callput = 'P'
#===============================================================================

#11

#===============================================================================
# S = 100.0
# r = 0.05
# sigma = 0.30
# T = 3.0
# K = 120
# NumOftimeStep = int(T * 54)
# NumOfSimulation = 10000
# perturbation = 0.01
# rnds = []
# callput = 'C'
#===============================================================================

#12

#===============================================================================
# S = 100.0
# r = 0.05
# sigma = 0.30
# T = 3.0
# K = 120
# NumOftimeStep = int(T * 54)
# NumOfSimulation = 10000
# perturbation = 0.01
# rnds = []
# callput = 'P'
#===============================================================================

#13

#===============================================================================
# S = 100.0
# r = 0.05
# sigma = 0.30
# T = 3.0
# K = 80
# NumOftimeStep = int(T * 54)
# NumOfSimulation = 10000
# perturbation = 0.01
# rnds = []
# callput = 'C'
#===============================================================================

#14

#===============================================================================
# S = 100.0
# r = 0.05
# sigma = 0.30
# T = 3.0
# K = 80
# NumOftimeStep = int(T * 54)
# NumOfSimulation = 10000
# perturbation = 0.01
# rnds = []
# callput = 'P'
#===============================================================================

#15

#===============================================================================
# S = 100.0
# r = 0.05
# sigma = 0.30
# T = 3.0
# K = 100
# NumOftimeStep = int(T * 54)
# NumOfSimulation = 10000
# perturbation = 0.01
# rnds = []
# callput = 'C'
#===============================================================================

#16

S = 100.0
r = 0.05
sigma = 0.30
T = 3.0
K = 100
NumOftimeStep = int(T * 54)
NumOfSimulation = 10000
perturbation = 0.01
rnds = []
callput = 'P'


print "S: " + repr(S)
print "r: " + repr(r)
print "sigma: " + repr(sigma)
print "T: " + repr(T)
print "K: " + repr(K)
print "CallPut: " + callput
print "#OfTimeSteps: " + repr(NumOftimeStep)
print "#OfSimulation: " + repr(NumOfSimulation)
print "Perturbation: " + repr(perturbation)
print "========================================================"

for simIndex in range(0, NumOfSimulation):
    rnd = []
    for stepIndex in range(0, NumOftimeStep):
        rnd.append(random.gauss(0, 1))
    
    rnds.append(rnd)

#finite difference
start_time = time.time()
const = EuropeanVanillaOption(rnds)
price = const.calcOption(S, r, sigma, T, K, NumOftimeStep, NumOfSimulation, callput)

greekType = 'D' 
delta = const.calcGreeks(S, r, sigma, T, K, NumOftimeStep, NumOfSimulation, perturbation, greekType, callput)

greekType = 'V' 
vega = const.calcGreeks(S, r, sigma, T, K, NumOftimeStep, NumOfSimulation, perturbation, greekType, callput)

greekType = 'T' 
theta = const.calcGreeks(S, r, sigma, T, K, NumOftimeStep, NumOfSimulation, perturbation, greekType, callput)

greekType = 'R' 
rho = const.calcGreeks(S, r, sigma, T, K, NumOftimeStep, NumOfSimulation, perturbation, greekType, callput)

print "Price: " + repr(price)
print "Delta: " + repr(delta)
print "Vega: " + repr(vega)
print "Rho: " + repr(rho)
print "Theta: " + repr(theta)

end_time = time.time()
print "Finite Difference Method: " + repr(end_time - start_time)
print "========================================================"

#AAD - tangent(forward) method
start_time = time.time()

AAD_Tangent_EuropeanVanilla.calcOption(S, r, sigma, T, K, NumOftimeStep, NumOfSimulation, callput, rnds)

end_time = time.time()

print "AAD Tangent Method: " + repr(end_time - start_time)
print "========================================================"

#AAD - adjoint(backward) method
start_time = time.time()

AAD_Adjoint_EuropeanVanilla.calcOption(S, r, sigma, T, K, NumOftimeStep, NumOfSimulation,callput, rnds)

end_time = time.time()

print "AAD Adjoint Method: " + repr(end_time - start_time)
print "========================================================"


