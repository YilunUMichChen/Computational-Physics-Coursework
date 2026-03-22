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
    
    # print(f'{x}  {N}')
    # print(sum)
    
    return sum, x, N
        
def difference(x):
    sum, x, N = taylorExpansionOfSin(x)
    diff = abs(sum - math.sin(x))
    # print(diff)
    return diff


#try x = 0.5

# for x in range(1,11):
#     taylorExpansionOfSin(x)

for x in range(1,11):
    sum, x, N = taylorExpansionOfSin(x)
    diff = difference(x)
    print(f'x = {x}, N = {N}, sum = {sum}, error = {diff}')
    

for x in range(10,101):
    sum, x, N = taylorExpansionOfSin(x)
    diff = difference(x)
    print(f'x = {x}, N = {N}, sum = {sum}, error = {diff}')
    
    
    
