def sum_of_intervals(intervals):
    length=0
    intervals=sorted(intervals)
    j=0
    i=1
    while i<len(intervals):
        if intervals[j][1]>intervals[i][0] and intervals[j][1]<intervals[i][1]:
            intervals.append((intervals[j][0],intervals[i][1]))
            intervals.pop(i)
            intervals.pop(j)
            intervals=sorted(intervals)
        elif intervals[j][0]<=intervals[i][0] and intervals[j][1]>=intervals[i][1]:
            intervals.pop(i)
        else:
            j+=1
            i+=1
    for i in set(intervals):
        length+=i[1]-i[0]
    return length


assert sum_of_intervals([(1, 5)]) == 4
assert sum_of_intervals([(1, 5), (6, 10)]) == 8
assert sum_of_intervals([(1, 5), (1, 5)]) == 4
assert sum_of_intervals([(1, 4), (7, 10), (3, 5)]) == 7
assert sum_of_intervals([(-1_000_000_000, 1_000_000_000)]) == 2_000_000_000
assert sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)]) == 100_000_030
assert sum_of_intervals([(1, 6), (10, 20), (5, 11)]) == 19
assert sum_of_intervals([(10, 20), (1, 6), (5, 11)]) == 19
assert sum_of_intervals([(-65, -28),( 425, 450 ),( 181, 360 ),( -460, -415 ),( 398, 474 ),( -75, 211 ),( -425, 234 ),(34, 495 ),(91, 461 )]) == 955

print("OK!")