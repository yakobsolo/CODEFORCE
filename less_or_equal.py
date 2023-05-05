n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
if k == 0:
    cur = arr[0] -1
    if cur>= 1:
        print(cur)
    else:
        print("-1")
else:
    cur = arr[k-1]
    if k<n and cur == arr[k]:
        print("-1")
    else:
        if cur >= 1:
        
            print(cur)
        else: 
            print("-1")
