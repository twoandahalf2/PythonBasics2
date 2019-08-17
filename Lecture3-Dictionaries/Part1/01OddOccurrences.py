line = input().lower()
words = line.split(' ')

counts = {}
for word in words:
    if word in counts:
        counts[word] +=1
    else:
        counts[word] = 1

results = []

for key,value in counts.items():
    if value % 2 != 0:
        results.append(key)

print(', '.join(results))