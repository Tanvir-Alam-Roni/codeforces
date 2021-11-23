def solution(n, arr):
    items = list(set(arr))
    i = 0
    count = [0]*2
    while(i<n):
        if arr[i]==items[0]:
            count[0] += 1
        elif arr[i]==items[1]:
            count[1] += 1
        i += 1
    if count[0]==1:
        spy = items[0]
    else:
        spy = items[1]

    return arr.index(spy)+1


result = []
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result.append(solution(n, arr))
print(*result, sep='\n')

