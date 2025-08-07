class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Helper function to check if all strings have the given prefix
        def is_common_prefix(length):
            str0, count = strs[0][:length], len(strs)
            return all(strs[i][:length] == str0 for i in range(1, count))
            
        # Binary search for the smallest length at which not all strings match
        min_length = min(len(s) for s in strs)
        low, high = 1, min_length

        while low <= high:
            mid = (low + high) // 2
            if is_common_prefix(mid):
                low = mid + 1
            else:
                high = mid -1

        return strs[0][:(low + high) // 2]
            

solution = Solution()
res = ["flower","flow","flight"]
print(solution.longestCommonPrefix(res)) # "fl"  # Output: "fl"



            