import math

def solution(l, a):
    count = 0
    i = 0
  
# 4 2 10 1
# 1 3
# 6 1
# 1 4 2
# 1 2 3 4 3
# 4 31 25 50 30 20 34 46 42 16 15 16
 
    while(i<l-1):
        if((max(a[i], a[i+1])/min(a[i], a[i+1])) > 2):
            if(a[i] > a[i+1]):
                count += math.ceil(math.log(0.5*a[i]/a[i+1])/math.log(2))
            else:
                count += math.ceil(math.log(0.5*a[i+1]/a[i])/math.log(2))
        i += 1
    return count

result = []
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result.append(solution(n, arr))

print(*result, sep='\n')