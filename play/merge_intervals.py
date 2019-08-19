
#temp_tuple = [[-25, -14], [-21, -16], [-20, -15], [-10, -7], [-8, -5], [-6, -3], [2, 4], [2, 3], [3, 6], [12, 15], [13, 18], [14, 17], [22, 27], [25, 30], [26, 29]]
temp_tuple = [[26,29], [-25, -14], [-21, -16], [-20, -15], [-10, -7], [-8, -5], [-6, -3], [2, 4], [2, 3], [3, 6], [12, 15], [13, 18], [14, 17], [22, 27], [25, 30]]

print(temp_tuple)

temp_tuple.sort(key=lambda interval: interval[0])

print(temp_tuple)

merged = [temp_tuple[0]]
for current in temp_tuple:
    previous = merged[-1]
    if current[0] <= previous[1]:
        previous[1] = max(previous[1], current[1])
    else:
        merged.append(current)


print(merged)
