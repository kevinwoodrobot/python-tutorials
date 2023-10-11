'''
    Sets are 
        - not ordered/can't index 
        - can add or remove items 
        - no repeats 

    Sets good to see what's common or different between group of things 
'''

# create a set 
mySet = {1,2,3,1}

# print mySet and you'll see the last 1 is ignored because repeated 
# > mySet = {1,2,3}

# add an item to the set 
mySet.add(5) 

# remov item from the set 
mySet.remove(5) 

# creating even and odd sets 
evenSet = {2,4,6}
oddSet = {1,3,5}

# union of the two sets (i.e. what's unique in both)
evenSet.union(oddSet) # > {1, 2, 3, 4, 5, 6} all unique 

# intersection of two sets
evenSet.intersection(oddSet) # > {} no intersection 


debug = 1 