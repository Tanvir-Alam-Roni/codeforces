def solution(n, task_list):
    task = []
    start_flag = 0
    end_flag = 0
    i = 0

    while(i<n):
        current_task = task_list[i]

        if(start_flag==1 and current_task!=running_task):
            start_flag=0

        if(start_flag==0):
            start_flag=1
            running_task = task_list[i]
            if current_task in task:
                return 'NO' 
            else:
                task.append(current_task)
        i += 1

    return 'YES'

result = []
t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(str, input()))
    result.append(solution(n, s))
print(*result, sep='\n')


                          