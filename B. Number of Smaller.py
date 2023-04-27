n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

ans = []
i , j = 0, 0
while j < m:
    while i<n and arr2[j]>arr1[i]:
        i +=1
    ans.append(i)
    j +=1
print(*ans)
