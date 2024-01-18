def sum_edges(n):
    i=1 
    l=(1,0)[n==0]
    while n>1 and i<=n:
        l+=(i,i*i+2)[i>1]-1
        i+=1
    return l
        


assert sum_edges(0) == 0
assert sum_edges(1) == 1
assert sum_edges(2) == 6
assert sum_edges(3) == 21
assert sum_edges(4) == 50



#lambda i:(i,i*i+2)[i>1]