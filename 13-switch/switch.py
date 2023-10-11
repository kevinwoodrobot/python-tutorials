num = 3

if num == 1: 
    print('first place baby')
elif num == 2: 
    print('man so close')
elif num == 3: 
    print('dang, barely made it')
else:
    print('Invalid case')

# starting with version 3.10, we can create a switch statement with cases 
match num: 
    case 1: 
        print('first place baby')
    case 2: 
        print('man so close')
    case 3: 
        print('dang barely made it')
    case _: 
        print('Invalid case')