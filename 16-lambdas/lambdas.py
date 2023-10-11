# https://www.machinelearningplus.com/python/lambda-function/

'''
    lambda functions 
        - a way to write a function that is used locally and temporarily 
        - can make code more condensed 
        - aka anonymous function 
    
'''
# naming a lambda function
sum  = lambda x1,x2 : x1 + x2
mySum = sum(1,2)

# using a lambda function directly 
(lambda x1,x2: x1 + x2)(1,2)

# get the odd numbers 
myList = [1,2,3,4,5,6]
'''
    Parameters:     
        - function, can be a normal function or lambda
        - iterable, like a list, tuple, etc anything you can iterate over 
    Returns: 
        returns a filter object 

    Filter similar to other functions like map 
'''
list(filter(lambda x : x%2 == 0, myList))

debug = 1 