def solution(s):
    a = s.count('A')
    b = s.count('B')
    c = s.count('C')
    if(b == a+c):
        return 'YES'
    else:
        return 'NO'

result = []

t = int(input())
for _ in range(t):
    s = input()
    result.append(solution(s))
print(*result, sep='\n')
