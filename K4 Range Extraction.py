def solution(args):
    args.sort()
    flag=False
    count=0
    result=str(args[0])
    for i in range(1,len(args)):
        if args[i-1]+1==args[i]:
            flag=True
            count+=1
        else:
            if flag:
                if count>1:
                    result+='-'+str(args[i-1])
                    count=0
                else:
                    result+=','+str(args[i-1])
                flag=False
                count=0
            result+=','+str(args[i])
        if flag and args[i] == args[-1]:
            if count>1:
                result+='-'+str(args[i])
            else:
                result+=','+str(args[i])
    return result
    
    
# print('-83,-82,-79--74,-71,-68--66,-64,-63,-60,-59,-57,-56,-54,-53,-51,-48,-47')
# print(solution([-83, -82, -79, -78, -77, -76, -75, -74, -71, -68, -67, -66, -64, -63, -60, -59, -57, -56, -54, -53, -51, -48, -47]))

    
assert solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]) == '-6,-3-1,3-5,7-11,14,15,17-20'
assert solution([-3,-2,-1,2,10,15,16,18,19,20]) == '-3--1,2,10,15,16,18-20'
assert solution([-60, -58, -56, -54, -53, -50, -47, -46, -43, -40, -38, -35, -33, -30, -29, -27, -26, -25, -24, -21, -18, -17, -14, -11]) == '-60,-58,-56,-54,-53,-50,-47,-46,-43,-40,-38,-35,-33,-30,-29,-27--24,-21,-18,-17,-14,-11'
assert solution([-83, -82, -79, -78, -77, -76, -75, -74, -71, -68, -67, -66, -64, -63, -60, -59, -57, -56, -54, -53, -51, -48, -47]) == '-83,-82,-79--74,-71,-68--66,-64,-63,-60,-59,-57,-56,-54,-53,-51,-48,-47'

print("OK!")

'''
Чужое решение
def solution(args):
    out = []
    beg = end = args[0]
    
    for n in args[1:] + [""]:        
        if n != end + 1:
            if end == beg:
                out.append( str(beg) )
            elif end == beg + 1:
                out.extend( [str(beg), str(end)] )
            else:
                out.append( str(beg) + "-" + str(end) )
            beg = n
        end = n
    
    return ",".join(out)
'''