
memo = {} # creating a dictionary to store our fibs helps us re-use some of the values from our earlier iterations 

def fibs(n):
    if n in memo:
        return memo[n] 
    if n <= 2:
        f = 1 
    else :
        f = fibs (n-1)+ fibs (n-2)
    memo[n] = f
    return f

#test case    
print (fibs(10))
