def searchSquareNum(n):
    numList = []
    
    try:
        n = int(n)
    except:
        print('Please input an integer')
    
    k = 1
    m = 1
    
    while True:
        k = m ** 2
        if k >= n:
            break
        numList.append(k)
        # print(k)
        m += 1
    
    print(f'the square numbers up to {n} are {numList}')
    
    return numList
    
            
            
searchSquareNum(1000)