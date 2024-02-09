
class Solution:
    def maxIndexDiff(self,a, n): 
        left_min = [0]*n
        right_max = [0]*n
        left_min[0] = a[0]
        for i in range(1,n):
            left_min[i] = min(left_min[i-1],a[i])

        right_max[-1] = a[-1]
        for i in range(n-2,-1,-1):
            right_max[i] = max(right_max[i+1],a[i])

        i=0
        j=0
        max_index= -1
        while i<n and j<n:
            if left_min[i]<=right_max[j]:
                max_index = max(max_index,j-i)
                j+=1
            else:
                i+=1
        return max_index
a = [34, 8, 10, 3, 2, 80, 30, 33, 1]
Sol = Solution()
print(Sol.maxIndexDiff(a,len(a)))
