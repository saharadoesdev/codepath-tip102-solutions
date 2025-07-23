from collections import deque 

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

root = TreeNode("Trunk")
root.left = TreeNode("Macintosh")
root.left.left = TreeNode("Fuji")
root.left.right = TreeNode("Opal")
root.right = TreeNode("GrannySmith")
root.right.left = TreeNode("Crab")
root.right.right = TreeNode("Gala")


def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)
    
    
# Using print_tree() included at the top of this page
print_tree(root)



def calculate_yield(root):
  if root.val == "+":
      return root.left.val + root.right.val
  elif root.val == "-":
      return root.left.val - root.right.val
  elif root.val == "*":
      return root.left.val * root.right.val    
  else:
      return root.left.val / root.right.val

"""
    +
  /   \
 7     5
"""
apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))

print(calculate_yield(apple_tree))



def right_vine(root):
    # vine = []
    # while root:
    #     vine.append(root.val)
    #     root = root.right
    #return vine
    vine = []
    def recursive_helper(vine, root):
        if root == None:
            return vine
        elif root.val is not None or root.right is not None:
            vine.append(root.val)
            return recursive_helper(vine, root.right)
        else:
            return vine
    return recursive_helper(vine, root)
    
  


"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))



def count_leaves(root):
    
    count_left = 0
    count_right = 0
    
    while root:
        
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1
        
        if root.left is not None:
            count_left = count_leaves(root.left)
        
        if root.right is not None:
            count_right = count_leaves(root.right)

        return count_left + count_right


    # # Edge Case
    # if root is None:
    #     return 0
    # # Base Case: We found a leaf node, return 1 recursively
    # if root.left is None and root.right is None:
    #     return 1

    # # Sum left of root's leaves and right of root's leaves
    # return count_leaves(root.left) + count_leaves(root.right)


"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

oak1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


print(count_leaves(oak1))
print(count_leaves(oak2))


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def survey_tree(root):
    tree = []
    def postorder(root):
        if root is None:
            return tree
        postorder(root.left)
        postorder(root.right)
        tree.append(root.val)
        
    postorder(root)
    return tree


"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

print(survey_tree(magnolia))


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def harvest_berries(root, threshold):
    
    total = 0
    def postorder(root):
        if root is None:
            return 0
        postorder(root.left)
        postorder(root.right)
        

        
    return postorder(root)


"""
       4
     /   \
   10     6
  /  \     \
 5    8    20
"""
bush = TreeNode(4, TreeNode(10, TreeNode(5), TreeNode(8)), TreeNode(6, None, TreeNode(20)))

print(harvest_berries(bush, 6))
print(harvest_berries(bush, 30))