# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return
        val = max(nums)
        id1 = nums.index(val)
        node = TreeNode(val)
        node.left = self.constructMaximumBinaryTree(nums[0:id1])
        node.right = self.constructMaximumBinaryTree(nums[id1 + 1:])
        return node
        
