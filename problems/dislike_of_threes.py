bucket = []
results = []

i = 1

while(i<1667):
    if(i%3!=0 and str(i)[-1] != '3'):
        bucket.append(i)
    i += 1

t = int(input())

for _ in range(t):
    k = int(input())
    results.append(bucket[k-1])
print(*results, sep='\n')