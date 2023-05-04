from collections import Counter
n, m = map(int, input().split())
mtx = []
for i in range(n):
    mtx.append(input())

mtx2 = []
for i in range(m):
    col = []
    for r in range(n):
        col.append(mtx[r][i])
    mtx2.append(col)
ans = ""
for i in range(n):
    row = Counter(mtx[i])
    for j in range(m):
        col = Counter(mtx2[j])
        if row[mtx[i][j]] == 1 and col[mtx[i][j]] == 1 :
            ans += str(mtx[i][j])
print(ans)
