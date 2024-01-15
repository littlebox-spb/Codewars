def is_valid_walk(walk):
    if len(walk)!=10:
        return False
    pointX=0
    pointY=0
    for i in walk:
        if i in ('e', 'w'):
            pointX+= 1 if i=='w' else -1
        else:
            pointY+= 1 if i=='n' else -1
    return not(pointX) and not(pointY)


'''
Чужое решение
def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
'''










assert is_valid_walk(['n','s','n','s','n','s','n','s','n','s']) == True
assert is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']) == False
assert is_valid_walk(['w']) == False
assert is_valid_walk(['n','n','n','s','n','s','n','s','n','s']) == False
assert is_valid_walk(['e', 'w', 'e', 'e', 'w', 's', 'w', 'w', 'e', 'w']) == False

print("OK!")