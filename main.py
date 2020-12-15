import numpy as np

def genstate( N, index ) : 
  spins = N*[0]
  # Your code goes here
  for i in range(N) :  
      spins[i] = np.floor( index / 2**(N-1-i) )
      index = index - spins[i]*(2**(N-1-i))
      if spins[i]==0 : spins[i] = -1
  return spins
  
nspins = 3
for i in range(2**nspins) :
  print( genstate(nspins,i) )
