for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    count = 0
    for i in range(1, n):
        if arr[i]  - arr[i-1] <= 1:
            count+=1
    if n-count == 1:
        print("YES")
    else:
        print("NO")

