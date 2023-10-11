'''
    if __name_ == "__main__"
        It Allows You to Execute Code When the File Runs as a Script, 
        but Not When It’s Imported as a Module 

    https://realpython.com/if-name-main-python/

'''


def myCoolFunction(): 
    print('I am cool')


if __name__ == "__main__": 
    print('Testing from module...')
    myCoolFunction() 