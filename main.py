import numpy as np

def genstate( N, index ) : 
  spins = N*[0]
  # Your code goes here
  
  return spins
  
nspins = 3
for i in range(2**nspins) :
  print( genstate(nspins,i) )
