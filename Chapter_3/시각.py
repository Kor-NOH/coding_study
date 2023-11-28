t = int(input())
cnt = 0

for i in range(t + 1):
    for j in range(60):
        for k in range(60):
            # i,j,k 를 문자열로 만들어서 하나로 묶은다음 3이 있는지 탐색
            if '3' in str(i) + str(j) + str(k):

                cnt += 1

print(cnt)