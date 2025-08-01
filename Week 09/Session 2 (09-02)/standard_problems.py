from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

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

# from collections import deque 

# Tree Node class
# class TreeNode:
#   def __init__(self, value, key=None, left=None, right=None):
#       self.key = key
#       self.val = value
#       self.left = left
#       self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

"""
Problem 1: Balanced Baked Goods Display
U: balanced tree --> difference in subtrees heights never exceeds 1
example: 3 - 2 = 1
checking each subtree as we go down the tree
edge case
    -- if the tree is empty (base check)??
P: check the height of each of subtree and compare their height counts to 1 (using recursion)
traverse down, and each time, we can add 1 to count the height
"""

def is_balanced(display):
    # base case
    if not display:
        return 0

    left_height = 1 + is_balanced(display.left)

    right_height = 1 + is_balanced(display.right)

    if (left_height - right_height) < 2:
        return True
    else:
        return False


    
    # if node.left and not node.right:
    #     if node.left.left or node.left.right:
    #         return False
    #     else:
    #         return True


baked_goods = ["🎂", "🥮", "🍩", "🥖", "🧁"]
display1 = build_tree(baked_goods)
baked_goods = ["🥖", "🧁", "🧁", "🍪", None, None, "🍪", "🥐", None, None, "🥐"]
display2 = build_tree(baked_goods)

print(is_balanced(display1)) 
print(is_balanced(display2))  
