"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def Prime(n):  
    for i in range(2,n//2+1):  
        if(n%i==0):  
            return(0)  
    return(1)  




def primes(n):
    
    if n < 0:
        raise ValueError("Sorry, no numbers below zero")
        
    N=n
    i=2 
    lst=[] 
    while(1):  
        if(Prime(i)):  
            lst.append(i) 
            if(len(lst)==N): 
                break 
        i+=1 
    print("First "+str(N)+" Prime numbers are:",end="") 
    print(*lst) 



    return lst




