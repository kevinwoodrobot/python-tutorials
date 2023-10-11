'''
    enums good for different cases 
'''
from enum import Enum 

class Size(Enum): 
    SMALL = 1 
    MEDIUM = 2 
    LARGE = 3 

def printSize(Enum:Size): 
    match Enum:
        case Size.SMALL: 
            print('Small')
        case Size.MEDIUM: 
            print('Medium')
        case Size.LARGE: 
            print('Large')
        case _: 
            print('Wrong size!')


printSize(Size.MEDIUM)

debug = 1 