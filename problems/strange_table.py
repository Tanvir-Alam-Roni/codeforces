def find_index(row, col, x):
    if(x%row==0):
        i = row-1
        j = x // (row+1)
    else:
        i = x%(row) - 1
        j = x // row
    return i, j

def solution(row, col, x):
    i, j = find_index(row, col, x)
    return col*i+j+1

result = []
t = int(input())
for _ in range(t):
    n, m, x = list(map(int, input().split()))
    result.append(solution(n, m, x))
print(*result, sep='\n')



# def solution(row, col, cell):
#     for i in range(row):
#         for j in range(col):
#             print(col*i+j+1, end=' ')
#         print('\n')

#     print('Another way\n')

#     for i in range(row):
#         for j in range(col):
#             print(i*1+j*row+1, end=' ')
#         print('\n')

# a, b, c = [3, 5, 12]
# print(solution(a, b, c))
# 6
# 1 1 1
# 1 2 1
# 1 2 2
# 1 3 1
# 1 3 2
# 1 3 3

    

