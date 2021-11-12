def solution(x, y, z):
    if x>y and x>z:
        return str(0)
    if y>z:
        return str(y-x+1)
    else:
        return str(z-x+1)

def print_now(result):
    first = 0
    last = 3
    while(last<=len(result)):
        print(' '.join(result[first:last]))
        first += 3
        last += 3

result = []
t = int(input())
for _ in range(t):
    a, b, c = list(map(int, input().split()))
    result.append(solution(a, b, c))
    result.append(solution(b, c, a))
    result.append(solution(c, a, b))
print_now(result)

