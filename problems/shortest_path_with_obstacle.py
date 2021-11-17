def solution(xa, ya, xb, yb, xf, yf):
    if (xf==xa and xf==xb):
        if (yf-ya)*(yf-yb)<0:
            return abs(yb-ya)+2
        else:
            return abs(xb-xa)+abs(yb-ya)    
    elif (yf==ya and yf==yb):
        if (xf-xa)*(xf-xb)<0:
            return abs(xb-xa)+2
        else:
            return abs(xb-xa)+abs(yb-ya)
    else:
        return abs(xb-xa)+abs(yb-ya)

t = int(input())
results = []
for _ in range(t):
    null = input()
    xa, ya = list(map(int, input().split()))
    xb, yb = list(map(int, input().split()))
    xf, yf = list(map(int, input().split()))
    

    results.append(solution(xa, ya, xb, yb, xf, yf))

print(*results, sep='\n')


