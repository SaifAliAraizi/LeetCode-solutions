# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True
        
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2 or t1.val != t2.val:
                return False
            
            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        
        return isMirror(root.left, root.right)

root = TreeNode(1)
nodeA = TreeNode(2)
nodeB = TreeNode(2)
nodeC = TreeNode(3)
nodeD = TreeNode(4)

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeD
nodeB.right = nodeC

solution = Solution()

print(solution.isSymmetric(root))
        
"""
101. Symmetric Tree
Easy

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). 

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
"""