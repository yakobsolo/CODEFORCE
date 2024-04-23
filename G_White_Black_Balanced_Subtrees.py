
import sys
from collections import defaultdict



for _ in range(int(input())):
    ans = 0
    n = int(input())
    arr = list(map(int, input().split()))
    colors = input()
    graph = defaultdict(list)
    parent = [[0, 0] for _ in range(n+1)]
    stack = []

    for i in range(n-1):
        graph[arr[i]].append(i+2)
        
    
    
    stack.append((1, 0, 0))
    visted = set()
    while stack:

        node, status , p = stack.pop()
        visted.add(node)
        if status:

            if colors[node-1] == "W":
                parent[node][0]+=1
            else:
                parent[node][1] +=1
            
            
            
            parent[p][0]+=parent[node][0]
            parent[p][1] += parent[node][1]
            continue
        

        stack.append((node, 1, p))
        for adj in graph[node]:
            if adj not in visted:
                stack.append((adj, 0, node))
            

    count = 0  
    
    for b, w in parent[1:]:
        if b == w:
            count+=1
    print(count)

        
    