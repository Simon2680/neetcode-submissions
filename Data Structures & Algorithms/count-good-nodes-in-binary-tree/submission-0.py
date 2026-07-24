# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        count =0
        max_so_far = float("-inf")
        def check(root, max_so_far):
            nonlocal count
            if not root:
                return
            if root.val>=max_so_far:
                max_so_far = root.val
                count +=1
            check(root.right, max_so_far)
            check(root.left, max_so_far)
        check(root, max_so_far)
        return count




        