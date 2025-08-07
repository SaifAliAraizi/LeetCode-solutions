class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
    
solution = Solution()
arr = [3,1,2,2,3,0,4,2]
val = 2
k = solution.removeElement(arr, val)
# print(k, ", nums =", arr[:k])

# Build output: valid elements + underscores
output = arr[:k] + ['_'] * (len(arr) - k)
print(f"{k} , nums = {output}")