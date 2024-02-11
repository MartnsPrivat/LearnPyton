import numpy as np

#putzt das Terminalwindow
print("\033[H\033[J", end="")
#end Terminalwindow putzen

e = np.random.random((2, 4)) 
print ("A random array:\n", e)

print("Shape of array: ", e.shape) 

print ("")

c = np.zeros((3, 4)) 
print ("An array initialized with all zeros:\n", c)

print ("")

f = np.arange(0, 30, 5) 
print ("A sequential array with steps of 5:\n", f)

# what is re-shaping an array?
# Create a one-dimensional array of 12 elements
a = np.arange(12)
print("eindimensionales array mit 12 Elementen:", a)
print()

# Reshape it into a two-dimensional array of 3 rows and 4 columns
b = a.reshape((3, 4))
print ("das gleiche array re-shaped auf 3 mal 4:\n ", b)

# Reshape it into a three-dimensional array of 2 arrays, each with 2 rows and 3 columns
c = a.reshape((2, 2, 3))
print("Reshaped it into a three-dimensional array of 2 arrays, each with 2 rows and 3 columns \n", c)

# Reshape it into a two-dimensional array of 4 rows, letting numpy infer the number of columns
d = a.reshape((-1, 4))
print("Reshaped it into a two-dimensional array of 4 rows, letting numpy infer the number of columnsd:\n",d)