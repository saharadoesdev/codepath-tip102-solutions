class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p, q):
    # Traverse both trees
    # Check current nodes
    if p is None and q is None:
        return True
    
    # Added after testing
    if p is None or q is None:
        return False
    
    if p.val == q.val:
        return is_same_tree(p.left,q.left) and is_same_tree(p.right,q.right)
    else:
        return False
    

# Full solution put into LeetCode:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        def helper(p, q):
            if p is None and q is None:
                return True

            if p is None or q is None:
                return False
                
            if p.val == q.val:
                return helper(p.left,q.left) and helper(p.right,q.right)
            else:
                return False
        return helper(p, q)