# https://redirect.cs.umbc.edu/courses/331/fall10/notes/python/python3.ppt.pdf


# import public modules 
# need to pip install first 
import numpy as np 
A = np.matrix([1,2,3])
print(A)

# # import everything, need to call with module name 
import KWmodule as KWmodule
KWmodule.classFunction() # doesn't work 
KWmodule.KWmodule.classFunction() # works 
KWmodule.lonerFunction() # works 

# import everything, use name directly 
from KWmodule import *
KWmodule.KWmodule.classFunction() # doesn't work 
KWmodule.classFunction() # works 
lonerFunction() # works 

# import only class 
from KWmodule import KWmodule
KWmodule.classFunction() # works 
KWmodule.lonerFunction() # doesn't work, not imported 

# import function only 
from KWmodule import lonerFunction
lonerFunction()
