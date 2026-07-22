# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # rh = 0
    # lh = 0
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        Balanced = True
        def dfs(root):
            nonlocal Balanced
            if not root:
                return 0
            rh,lh=dfs(root.right), dfs(root.left)
            if abs(rh-lh)>1:
                Balanced = False
            return 1 + max(rh,lh)
        dfs(root)
        return Balanced
    
    #     def dfs(root):
    #         if not root: return [True, 0]
    #         right, left = dfs(root.right), dfs(root.left)
    #         balanced = (abs(right[1]-left[1])<= 1) and (right[0] and left[0])
    #         return [balanced, 1+max(right[1], left[1])]
    #     return dfs(root)[0]

    
    






        
        
        
        