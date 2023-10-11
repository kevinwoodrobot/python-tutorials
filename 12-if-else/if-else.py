
'''
    if (bool): 
        do something 
    elif (bool): 
        do something
    else: 
        do something 

    logical conditions 
        >  greater than 
        >= greather than or equal to 
        <  less than 
        <= less than or equal to 
        == equal to 
        != not equal to 

'''

myBool = True
# don't do this 
if myBool == True: 
    print('Bad way')

# just do this
if myBool: 
    print('Good way')



maxCalories = 2000 
minCalories = 1500
myCalories = 3000 

if myCalories > maxCalories: 
    print('You ate too much Turkey!')


'''
    combining conditions with 
        and, or 
'''


if myCalories > minCalories and myCalories < maxCalories: 
    print('Good Job!')
elif myCalories < minCalories and myCalories >= 0: 
    print('Eat More!')
elif myCalories > maxCalories: 
    print('Go run!')
else: 
    print('Invalid calories')


debug = 1 

    