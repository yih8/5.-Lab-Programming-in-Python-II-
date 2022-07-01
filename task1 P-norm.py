import math






def p_norm(p,v):
    n=len(v)
    a=0
    
    for i in range (0,n):
        a=a+v[i]**p  
        i+=1
    b= math.log10(a) /p
    c=10**b 
    return c 


print(p_norm(100,[3,4,5,6,7,8]))
print(p_norm(2,[3,4]))