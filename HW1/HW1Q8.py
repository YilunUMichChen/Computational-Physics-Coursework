import math

def singleContribution(i, j, k):
    '''Define a function to calculate the contribution of a single atom 
    to the Madelung constant'''
    if i == 0 and j == 0 and k == 0:
        return 0
    
    absContribution = math.sqrt(i**2 + j**2 + k**2) #calculate the absolute value of the contribution
    
    if (i + j + k) % 2 == 0: #if the sum of i, j, k is even, the contribution is positive
        return 1 / absContribution
    else:                    #if the sum of i, j, k is odd, the contribution is negative
        return -1 / absContribution
    

def getMadelung(L):
    ''''Define a function to calculate the Madelung constant
    for a range of L'''
    sum = 0
    for i in range(-L, L+1):
        for j in range(-L, L+1):
            for k in range(-L, L+1):
                sum += singleContribution(i, j, k)  #sum the contribution of each atom
    return sum

L = 200 #set the range of L
print(getMadelung(L))
#the result is -1.7446850421707383 when L = 200
#using C++ can get the result faster than python