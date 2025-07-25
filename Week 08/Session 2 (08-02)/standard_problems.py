from collections import deque

# Tree Node class
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
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




def count_odd_splits(root):
    # if root is None:
    #     return 0
    
    # if root.left is None and root.right is None:
    #     return 1 if root.val % 2 == 1 else 0
    
    # return count_odd_splits(root.left) + count_odd_splits(root.right)
    if not root:
        return 0

    num = 1 if root.val % 2 == 1 else 0

    left_count = count_odd_splits(root.left)
    right_count = count_odd_splits(root.right)

    return num + left_count + right_count




    # count = 0
    # def helper(root, count):
    #     if root:
    #         if root.val % 2 == 1:
    #             count += 1
    #         count += helper(root.left, count)
    #         count += helper(root.right, count)
    #         return count
    #     else: 
    #         return count

    # return helper(root, count)


values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

print(count_odd_splits(monstera))
print(count_odd_splits(None))



def find_flower(inventory, name):
    if not inventory:
        return False    
    if inventory.val == name:
        return True
    if name < inventory.val: 
        return find_flower(inventory.left,name)
    if name > inventory.val:
        return find_flower(inventory.right, name)


values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower"))      



## PROBLEM 3 was discussion-based, not coding!



def add_plant(collection, name):
    if not collection:
        return TreeNode(name)
    if name < collection.val:
        collection.left = add_plant(collection.left, name)
    else:
        collection.right = add_plant(collection.right, name)
    return collection
        

values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(add_plant(collection, "Aloe"))