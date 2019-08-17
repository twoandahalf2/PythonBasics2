nums = list(map(float, input().split(' ')))
counts = {}
for word in nums:
    if word in counts:
        counts[word] +=1
    else:
        counts[word] = 1



for item in sorted(counts.keys()):
    print(f'{item} -> {counts[item]} times')
