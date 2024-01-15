def dig_pow(n, p):
    sn=str(n)
    ssum=0
    for i in sn:
        ssum+=int(i)**p
        p+=1
    return ssum//n if ssum%n==0 else -1

assert dig_pow(89, 1) == 1
assert dig_pow(92, 1) == -1
assert dig_pow(46288, 3) == 51
assert dig_pow(41, 5) == 25
assert dig_pow(114, 3) == 9
assert dig_pow(8, 3) == 64

print('OK!')