def zero(op=None):
    res=0 
    if op:
        res=eval('res'+op)
    return res
def one(op=None):
    res=1 
    if op:
        res=eval('res'+op)
    return res
def two(op=None): 
    res=2
    if op:
        res=eval('res'+op)
    return res
def three(op=None):
    res=3
    if op:
        res=eval('res'+op)
    return res
def four(op=None):
    res=4 
    if op:
        res=eval('res'+op)
    return res
def five(op=None): 
    res=5 
    if op:
        res=eval('res'+op)
    return res
def six(op=None):
    res=6 
    if op:
        res=eval('res'+op)
    return res
def seven(op=None):
    res=7 
    if op:
        res=eval('res'+op)
    return res
def eight(op=None):
    res=8
    if op:
        res=eval('res'+op)
    return res
def nine(op=None):
    res=9 
    if op:
        res=eval('res'+op)
    return res

def plus(b):
    return f'+{b}'
def minus(b):
    return f'-{b}'
def times(b): 
    return f'*{b}'
def divided_by(b):
    return f'//{b}'


assert seven(times(five())) == 35



