import math

# def taylorSineTerm(x,N):
#     return ((-1) ** N) * (x ** (2 * N + 1)) / math.factorial(2 * N + 1)

def taylorExpansionOfSin(x):
    sum = 0
    N = 0
    term = x
    # if x == 0:
    #     print(0)
    #     print(f'when x = {x}, the summation ends at N = {N}')
    #     return 0
    
    while abs(term) >= 1e-7 * abs(sum):  #must take abs(sum) rather than sum on the RHS!!!
        sum += term
        N += 1
        term = ((-1) ** N) * (x ** (2 * N + 1)) / math.factorial(2 * N + 1)
        # print(taylorSineTerm(x,N))
    print(sum)
    print(f'when x = {x}, the summation ends at N = {N}')
    return sum
        
def difference(x):
    diff = abs(taylorExpansionOfSin(x) - math.sin(x))
    print(f'the difference between the finite series and the actual value is {diff}')
    return diff


#try x = 0.5

# for x in range(1,11):
#     taylorExpansionOfSin(x)

for x in range(1,11):
    difference(x)
    

for x in range(10,101):
    difference(x)
    
    
    
