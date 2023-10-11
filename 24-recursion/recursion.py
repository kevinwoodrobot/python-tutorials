def countDown(n): 
    print(n)
    if n == 0:
        print('Done') 
        return
    countDown(n-1)

countDown(10)