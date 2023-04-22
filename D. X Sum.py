for _ in range(int(input())):
    n,  m = map(int, input().split())
    mtx= []
    for r in range(n):
        row = list(map(int, input().split()))
        mtx.append(row)
    tot = 0
    for i in range(n):
        for j in range(m):
            r , c = i, j
            cursum = 0

            while 0<= r< n and 0<= c<m:
                cursum += mtx[r][c]
                r -=1
                c -=1
            r , c = i, j

            while 0<= r< n and 0<= c<m:
                cursum += mtx[r][c]
                r -=1
                c +=1 
            r , c = i, j

            while 0<= r< n and 0<= c<m:
                cursum += mtx[r][c]
                r +=1
                c -=1
            r , c = i, j

            while 0<= r< n and 0<= c<m:
                cursum += mtx[r][c]
                r +=1
                c +=1 
            cursum -= mtx[i][j]*3
            
            tot = max(tot, cursum)
    print(tot) 
