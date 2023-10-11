'''
    dictionary maps your keys (in quotes) to a value
    separated by colon symbol ":" 

    no duplicates 
'''

# example of mapping name to favorite number 
myMap = {'kevin':1, 
         'john':3, 
         'mark':5}

'''
    Function: keys 
    Parameters: none 
    Returns: keys for the dictionary 
'''
myMap.keys()


# method 1 to extract value associated with the key kevin 
myMap.get('kevin')

# method 2 to extract value associated with the key 'kevin' 
myMap['kevin'] 

# list out items in the dictionary 
myMap.items() 

# remove item in dictionary 
myMap.pop('kevin')

# change value - method 1 
myMap.update({'john':7})

# change value - method 2 
myMap['john'] = 2

# same to add new item 
myMap['ozzy'] = 8 

debug = 1 