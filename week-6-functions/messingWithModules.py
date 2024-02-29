# Messing with modules
# Some programs need to be imported so the program will run
# Author: Fatima Oliveira

import math #https://docs.python.org/3/library/math.html#module-math
# from math import cos ----work same as above 

var = math.cos(3.14) # will need to put math in front if I only import math above
# var = cos(3.14) --- this if I use: from math import cos
# if import math as m, then m will be enough to define any function inside math
# ex: var = m.cos(3.14)
print(var)
