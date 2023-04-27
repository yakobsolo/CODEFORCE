#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        for i in range(n):
            if i ==0:
                continue
            if arr[i-1] > arr[i]:
                return False
        return True
