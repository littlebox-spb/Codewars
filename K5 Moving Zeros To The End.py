def move_zeros(lst):
    if sum(lst)!=0:
        digital=[]
        nulls=[]
        for i in range(len(lst)):
            if lst[i]==0:
                nulls.append(0)
            else:
                digital.append(lst[i]) 
        lst=digital
        lst.extend(nulls)
    return lst            

assert move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
assert move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) == [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert move_zeros([0, 0]) == [0, 0]
assert move_zeros([0]) == [0]
assert move_zeros([]) == []

print("OK!")