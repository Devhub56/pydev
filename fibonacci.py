
memo = {}

def fibs(n):
    if n in memo:
        return memo[n]
    if n <= 2:
        f = 1 
    else :
        f = fibs (n-1)+ fibs (n-2)
    memo[n] = f
    return f
    
print (fibs(10))