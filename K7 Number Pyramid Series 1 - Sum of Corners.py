# n=3

# if n<=1:
#     print(n)
# else:
     
# corner3=sum([i for i in range(n+1)])

# corner3=int(n+n*(n-1)/2)

# print(n*n+2)
            
# def sum_corners(n):
#     return n*n+2 if n>1 else n            


sum_corners=lambda n:(n,n*n+2)[n>1]
##################################

assert sum_corners(3)== 11
assert sum_corners(1)== 1
assert sum_corners(0)== 0
print("OK!")