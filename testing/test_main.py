import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_microstates_generator(self) : 
        for k in range(1,6) :
            for i in range(2**k) :
                num, spins = i, k*[0]
                refspins = genstate( k, i )
                for j in range(k) :
                   spins[k - 1 - j] = np.floor( num / 2**(k-1-j) )
                   num = num - spins[k - 1 - j]*2**(k-1-j)
                   if spins[k-1-j]==0 : spins[k - 1 - j] = -1
                   self.assertTrue( refspins[k-1-j]==spins[k-1-j] or refspins[j]==spins[k-1-j], "The code that you have written does not generate microstates correctly" )
