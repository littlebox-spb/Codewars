def sum_edges(n):
    l=0
    a=0
    for i in range(n):
        a+=i+1
        l+=(2*a-i,a)[i==0]
    l+=sum(range(a-n+2,a))
    return l
        


assert sum_edges(0) == 0
assert sum_edges(1) == 1
assert sum_edges(2) == 6
assert sum_edges(3) == 21
assert sum_edges(4) == 50

print("OK!")

#lambda i:(i,i*i+2)[i>1]