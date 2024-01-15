def delete_nth(order,max_e):
    rep={}
    if len(order)<=1:
        return order
    for i in order:
        if i in rep:
            rep[i]+=1
        else:
            rep.setdefault(i,1)
    for i in order:
        if rep[i]>max_e:
            rep[i]=max_e
    result=[]
    for i in order:
        if rep[i]>0:
            result.append(i)
            rep[i]-=1
    return result

# Чужой код
#
# def delete_nth(order,max_e):
#     ans = []
#     for o in order:
#         if ans.count(o) < max_e: ans.append(o)
#     return ans


assert delete_nth([20, 37, 20, 21], 1) == [20, 37, 21]
assert delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3) == [1, 1, 3, 3, 7, 2, 2, 2]
assert delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 3) == [1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5]
assert delete_nth([1, 1, 1, 1, 1], 5) == [1, 1, 1, 1, 1]
assert delete_nth([], 5) == []

print("OK!")