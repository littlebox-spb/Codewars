def sum_edges(n):
    i=1 
    l=1
    while i<n:
        l+=i
        i+=1
    return l        
        


assert sum_edges(0) == 0
assert sum_edges(1) == 1
assert sum_edges(2) == 6
assert sum_edges(3) == 21
assert sum_edges(4) == 50