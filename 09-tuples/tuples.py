# tuples ordered, unchangeable, repeatable
myTuple = (1,2,3,1)

# access tuple (same way as list)
myTuple[0]
myTuple[0:2]

# can't modify, so this would give an error 
myTuple[0] = 2 

'''
    Function: count 
    Parameters: value inside the tuple (any data type) 
    Returns: number of occurrences 
'''
myTuple.count(1)

'''
    Function: index 
    Parameters: value inside the tuple (any data type)
    Returns: first index of occurrence 
'''
myTuple.index(2)
debug = 1 