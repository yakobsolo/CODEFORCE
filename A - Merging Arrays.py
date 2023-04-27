n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

merged = []
i, j = 0, 0
while i< len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        merged.append(arr1[i])
        i+=1
    else:
        merged.append(arr2[j])
        j+=1
if i<len(arr1):
    merged+=arr1[i:]
if j< len(arr2):
    merged+=arr2[j:]
print(*merged)
