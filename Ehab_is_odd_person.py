n = int(input())
arr = list(map(int, input().split()))
parity = arr[0]%2
for a in arr:
    if a%2 != parity:
        arr.sort()
        print(*arr)
        break
    
else:
    print(*arr)
    
