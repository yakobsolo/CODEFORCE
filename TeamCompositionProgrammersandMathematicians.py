n = int(input())
for _ in range(n):
    p, m = map(int, input().split())
    l =0 
    h = (p+m)//4
    maxx = 0
    
    while l<= h:
        mid = (l+h)//2
        if mid > min(p,m):
            h = mid-1
        else:
            l = mid +1
            maxx = max(maxx, mid)
    print(maxx)
