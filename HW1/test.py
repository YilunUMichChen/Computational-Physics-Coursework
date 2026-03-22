import math

def taylorSineTerm(x,N):
    return ((-1) ** N) * (x ** (2 * N + 1)) / math.factorial(2 * N + 1)

def taylorExpansionOfSin(x):
    sum = 0
    N = 0
    if x == 0:
        print(0)
        print(f'the summation ends at N = {N}')
        return 0
    
    while abs(taylorSineTerm(x,N) * (10 ** 7)) >= abs(sum):  #must take abs(sum) rather than sum on the RHS!!!
        sum += taylorSineTerm(x,N)
        N += 1
        # print(taylorSineTerm(x,N))
    print(sum)
    print(f'the summation ends at N = {N}')
    return sum
        
def difference(x):
    diff = taylorExpansionOfSin(x) - math.sin(x)
    print(f'the difference between the finite series and the actual value is {diff}')
    return diff


#try x = 0.5

taylorExpansionOfSin(70)
print()
difference(70)