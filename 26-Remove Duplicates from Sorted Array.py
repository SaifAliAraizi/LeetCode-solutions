class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        k = 1  # Start from the second element
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # If the current element is unique
                nums[k] = nums[i]  # Place it at the k-th index
                k += 1  # Move forward
        
        return k

solution = Solution()
arr = [0,0,1,1,1,2,2,3,3,4]
k = solution.removeDuplicates(arr)
print("k =", k, ", nums =", arr[:k])
