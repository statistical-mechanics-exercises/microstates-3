# Generating microstates

In the previous exercise we showed that the following expression maps each of the possible microstates for a set of N Ising spins to an integer in the range from 0 up to ![](https://render.githubusercontent.com/render/math?math=2^N-1):

![](https://render.githubusercontent.com/render/math?math=b=\sum_{j=1}^N2^{j-1}z(s_j)\qquad\textrm{where}\qquad\z(0)=-1\qquad\textrm{and}\qquad\z(1)=1)

As this mapping between the microscopic configurations and the integers is both injective and surjective it stands to reason that we can invert this relation.  In other words, if we are given an integer between 0 and ![](https://render.githubusercontent.com/render/math?math=2^N-1) we can generate the corresponding set of spin coordinates.  I would like you to add lines to the program in the box on the left here in order to do this conversion.  You will notice that I have written a function called genstate for you that takes the number of spins, N, and the index of the configuration as input.  This function then returns a list called spins that should contain the microscopic coordinates for each of the spins.

To  help you understand how to write the program consider what the sum in the expression above is if N=3.  In that case:

![](https://render.githubusercontent.com/render/math?math=b=a_0%2B+2a_1%2B+4a_2)

Furthermore, ![](https://render.githubusercontent.com/render/math?math=a_0), ![](https://render.githubusercontent.com/render/math?math=a_1) and ![](https://render.githubusercontent.com/render/math?math=a_2) must be equal to 0 or 1 and b has to be less than or equal to 7.  Notice that if take the floor of  b/4 using the command:

````
a2 = np.floor( b / 4 )
````

 we get ![](https://render.githubusercontent.com/render/math?math=a_2).  We can then get ![](https://render.githubusercontent.com/render/math?math=a_1) by doing:

````
a1 = np.floor( (b - 4*a2) / 2 )
````

and ![](https://render.githubusercontent.com/render/math?math=a_0) by doing:

````
a0 = b - 4*a2 - 2*a1
````

Your task is to generalise the insight outlined above and to make the above algorithm work for arbitrary values of N.
