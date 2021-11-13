def solution(n):
    c1 = 0
    c2 = 0
    if(n%3==1):
        c1 += 1
    if(n%3==2):
        c2 += 1
    
    c1 += n//3
    c2 += n//3
    return ' '.join(list(map(str, [c1, c2])))

result = []
t = int(input())
for _ in range(t):
    n = int(input())
    result.append(solution(n))
print(*result, sep='\n')




