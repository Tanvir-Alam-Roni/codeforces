output = []

def find_time(keys, s):
        time = 0
        left = 0
        right = 1
        while(right<len(s)):
            time += abs(int(keys.find(s[right]))-int(keys.find(s[left])))
            left += 1
            right += 1
        return time


n = int(input())
for _ in range(n):
    keys = input()
    s = input()
    output.append(find_time(keys, s))
print(*output, sep='\n')


