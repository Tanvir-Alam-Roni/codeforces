def solution(n, arr):
    l = n
    min_arr = min(arr)
    max_arr = max(arr)
    idx_min = arr.index(min_arr)
    idx_max = arr.index(max_arr)
    print(f'index is {idx_min} and {idx_max}')
    count = 0
    if idx_max < idx_min:
        if n-idx_max-1 > idx_max+1:
            count += idx_max+1
            l -= idx_max+1
            idx_min -= idx_max+1
        else:
            count += n-idx_max-1
            l -= n-idx_max-1
            idx_min -= idx_max+1
        if l-idx_min-1 > idx_min+1:
            count += idx_min+1
        else:
            count += l-idx_min-1
    else:
        if n-idx_min-1 > idx_min+1:
            count += idx_min+1
            l -= idx_min+1
            idx_max -= idx_min+1
        else:
            count += n-idx_min-1
            l -= n-idx_min-1
            idx_max -= idx_min+1
        if l-idx_max-1 > idx_max+1:
            count += idx_max+1
        else:
            count += l-idx_max-1
    return count

result = []
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result.append(solution(n, arr))

print(*result, sep='\n')

