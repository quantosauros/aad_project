'''
Created on 2015. 7. 28.

@author: Jay
'''
from krwirs.hullwhite import HullWhite

#input parameters
Maturity = 10.0
#Num of payment per year
CouponFrequency = 4.0
MonitorFrequency = 30.0
ACT = 365.0
simNum = 10

meanReversion = 0.01
HWVol = 0.001

hw = HullWhite(meanReversion, HWVol, 
               simNum, Maturity, CouponFrequency, ACT, MonitorFrequency)

hw.generatePaths()

