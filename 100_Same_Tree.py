# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False
        
        return (p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

root = TreeNode(1)
nodeA = TreeNode(2)
nodeB = TreeNode(3)

root.left = nodeA
root.right = nodeB

root1 = TreeNode(1)
nodeC = TreeNode(2)
nodeD = TreeNode(3)

root1.left = nodeC
root1.right = nodeD

solution = Solution()

print(solution.isSameTree(root, root1))
"""
100. Same Tree
Easy

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""