def boringFunction(): 
    '''
        can type comments here and see it show up when you 
        hover you mouse over the name of your function 
    '''
    print('I am useless')

'''
    Function: gainSomeMuscle
    Parameters: 
        - currentWeight, float in lbs 
        - pureMuscle, float in lbs 
    Returns: 
        - newWeight, float in lbs 
'''
def gainSomeMuscle(currentWeight,pureMuscle):
    newWeight = currentWeight + pureMuscle
    print('Your new weight is',newWeight)

'''
    define function specifying type (caled typing, version 3.5 and above )
'''
def gainSomeMuscleFancy(currentWeight:float,pureMuscle:float) -> float: 
    newWeight = currentWeight + pureMuscle
    print('Your new weight is',newWeight)

'''
    Arbitrary arguments with input *argName 
    Ex: def functionName(*argName)
    arg - variable length arguments

    input will be a tuple (item1, item2, etc..)
'''
def magicRecipe(*favoriteFoods): 
    '''
        prints out foods in magic recipe 
    '''
    for x in favoriteFoods:
        print(x)

'''
    **kwargs, two stars 
    keyworded variable length arguments with keys and values 
    basically a dictionary 
    colorNames = {first:'blue',
                  second: 'red', 
                  etc}
'''
def colorMixer(**colorNames):
    if 'first' in colorNames.keys(): 
        print('first color is',colorNames['first'])

    if 'second' in colorNames.keys(): 
        print('second color is', colorNames['second'])

    if 'third' in colorNames.keys(): 
        print('third color is', colorNames['third'])


boringFunction() 
gainSomeMuscle(160,5)
gainSomeMuscleFancy(160,5)
magicRecipe('galbijim','eggs','bbq')
colorMixer(first='blue',second='red',third='white')