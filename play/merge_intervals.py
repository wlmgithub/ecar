
#temp_tuple = [[-25, -14], [-21, -16], [-20, -15], [-10, -7], [-8, -5], [-6, -3], [2, 4], [2, 3], [3, 6], [12, 15], [13, 18], [14, 17], [22, 27], [25, 30], [26, 29]]
temp_tuple = [[26,29], [-25, -14], [-21, -16], [-20, -15], [-10, -7], [-8, -5], [-6, -3], [2, 4], [2, 3], [3, 6], [12, 15], [13, 18], [14, 17], [22, 27], [25, 30]]

print('temp_tuple: ', temp_tuple)

temp_tuple.sort(key=lambda interval: interval[0])

print('sorted temp_tuple: ', temp_tuple)

merged = [temp_tuple[0]]
for current in temp_tuple:
    previous = merged[-1]
    if current[0] <= previous[1]:
        previous[1] = max(previous[1], current[1])
    else:
        merged.append(current)


print('merged: ', merged)


#####
from operator import itemgetter

intervals = temp_tuple

def merge_intervals(intervals):

    sorted_intervals = sorted(intervals, key=itemgetter(0))

    if not sorted_intervals:  # no intervals to merge
        return

    # low and high represent the bounds of the current run of merges
    low, high = sorted_intervals[0]

    for iv in sorted_intervals[1:]:
        if iv[0] <= high:  # new interval overlaps current run
            high = max(high, iv[1])  # merge with the current run
        else:  # current run is over
            yield low, high  # yield accumulated interval
            low, high = iv  # start new run

    yield low, high  # end the final run


print('------------ calling func merge_intervals ---- ')

print('merged: ', list(merge_intervals(intervals)))
