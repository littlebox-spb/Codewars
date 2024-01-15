class Stack:
    st=[]    
    def __init__(self):
        self.st=[]
    def push(self,dir):
        self.st.append(dir)
    def pop(self):
        if len(self.st)==0:
            return ""
        else:
            return self.st.pop()
        

def dir_reduc(arr):
    stack=Stack()
    for d in arr:
        t=stack.pop()
        if not t:
            stack.push(d)
        else: 
            if not ((t=='NORTH' and d=='SOUTH') or (t=='SOUTH' and d=='NORTH') or (t=='WEST' and d=='EAST') or (t=='EAST' and d=='WEST')):
                stack.push(t)
                stack.push(d)
    return stack.st


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
assert(dir_reduc(a)==['WEST'])
a=["NORTH", "WEST", "SOUTH", "EAST"]
assert(dir_reduc(a)==["NORTH", "WEST", "SOUTH", "EAST"])
a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"] # ['WEST']
assert(dir_reduc(a)==['WEST'])
a = ["NORTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH", "SOUTH", "NORTH","WEST", "EAST"] # ['NORTH', 'NORTH']
assert(dir_reduc(a)==['NORTH', 'NORTH'])
a = [] # []
assert(dir_reduc(a)==[]) 
a=["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH"] # []
assert(dir_reduc(a)==[])
a = ["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH","NORTH"] # ["NORTH"]
assert(dir_reduc(a)==["NORTH"])
a = ["EAST", "EAST", "WEST", "NORTH", "WEST", "EAST", "EAST", "SOUTH", "NORTH", "WEST"] # ["EAST", "NORTH"]
assert(dir_reduc(a)==["EAST", "NORTH"])
a = ["NORTH", "EAST", "NORTH", "EAST", "WEST", "WEST", "EAST", "EAST", "WEST", "SOUTH"] # ["NORTH", "EAST"])
assert(dir_reduc(a)==["NORTH", "EAST"])
a = ["NORTH", "WEST", "SOUTH", "EAST"] # ["NORTH", "WEST", "SOUTH", "EAST"])
assert(dir_reduc(a)==["NORTH", "WEST", "SOUTH", "EAST"])
a = ['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH', 'NORTH']
assert(dir_reduc(a)==['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH'])       

print('OK!') 

'''
Чужое решение
opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dirReduc(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan
'''