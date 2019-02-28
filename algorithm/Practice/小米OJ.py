#兔子跳格子
def go(a_list, current, N, res):
    if current >= N:
        return True
    if not a_list[current]:
        return False
    if res:
        return True
    for i in range(1,a_list[current]+1):
        res = (res or go(a_list, i, N, res))


def solution(line):
# 缩进请使用 4 个空格，遵循 PEP8 规范
# please write your code here

# return 'your_answer'
    a = [int(i) for i in  line.split()]
    a_0 = a.pop(0)
    # print(a)
    N = len(a)
    if not a_0:
        return "true" if N==0 else "false"
    # res = go(a,0,N-1,False)
    # i = 0
    if a_0 == 1 and a[0]==0:
        return "false"
    my_dp = [[a_0-1 for j in range(N)] for i in range(N)]
    # current_max = a[0]
    i = 1
    while i<N:
        my_dp[i][0] = a[i]
        i += 1

    for i in range(1,N):
        for j in range(1,N):
            my_dp[i][j] = max(my_dp[i-1][j],my_dp[i-1][j]+my_dp[i][0])
    flag = True
    # print(my_dp[0][0])
    # print(my_dp)
    for i in range(1,N):
        if my_dp[i][i] < i:
            flag = False
            break

    return "true" if flag else "false"




if __name__ == '__main__':
    print(solution(input()))