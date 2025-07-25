# Week 01, Session 1 (01-01) - Advanced Problems

# -----------------------------------------------------------------------------
# Problem 1: Hunny Hunt
# -----------------------------------------------------------------------------
'''
Problem:
Write a function `linear_search()` to help Winnie the Pooh locate his lost items.
The function accepts a list `items` and a `target` value as parameters. The function
should return the first index of `target` in `items`, and `-1` if `target` is not
in the `lst`. Do not use any built-in functions.

Example Usage:
items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
linear_search(items, target)

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
linear_search(items, target)

Example Output:
3
-1

Note: The problem description states that the function has `items` as a parameter,
while the given function header uses `lst`. I will be using `items` as per the
description and example usage.
'''
def linear_search(items, target):
    """
    Description.
    
    Args:
        variable (type): Description.
    """
    for i in range (0, len(items)):
        if items[i] == target:
            return i
    return -1

# Complexity Analysis:
# Time Complexity: O(n) - The function iterates the elements of items, up to n possible times.
# Space Complexity: O(1) - The function uses a constant amount of memory, regardless of n. No new data structures are created.


# -----------------------------------------------------------------------------
# Problem 2: Bouncy, Flouncy, Trouncy, Pouncy
# -----------------------------------------------------------------------------
'''
Problem:
Tigger has developed a new programming language Tiger with only four operations
and one variable `tigger`.
- `bouncy` and `flouncy` both increment the value of the variable `tigger` by `1`.
- `trouncy` and `pouncy` both decrement the value of the variable `tigger` by `1`.
Initially, the value of `tigger` is 1 because he's the only tigger around! Given
a list of strings `operations` containing a list of operations, return the final
value of `tigger` after performing all the operations.

Example Usage:
operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)

Example Output:
2
4
'''
def final_value_after_operations(operations):
    """
    Description.
    
    Args:
        variable (type): Description.
    """
    tigger = 1
    for op in operations:
        if op == "bouncy" or op == "flouncy":
            tigger += 1
        else:
            tigger -= 1
    return tigger


# Complexity Analysis:
# Time Complexity: O(?) - Description.
# Space Complexity: O(?) - Description.


# -----------------------------------------------------------------------------
# Problem 3: T-I-Double Guh-Er II
# -----------------------------------------------------------------------------
'''
Problem:
T-I-Double Guh-Er: That spells Tigger! Write a function `tiggerfy()` that accepts
a string `word` and returns a new string that removes any substrings `t`, `i`, `gg`,
and `er` from `word`. The function should be case insensitive.

Example Usage:
word = "Trigger"
tiggerfy(word)

word = "eggplant"
tiggerfy(word)

word = "Choir"
tiggerfy(word)

Example Output:
"r"
"eplan"
"Chor"
'''
def tiggerfy(word):
    """
    Description.
    
    Args:
        variable (type): Description.
    """
    letters_to_remove = ["t", "i", "gg", "er"]
    result = ""

    i = 0
    while i < len(word):
        if word[i:i+2].lower() in letters_to_remove:
            i = i + 2  # "gg" or "er", skip the next iteration
        elif word[i].lower() in letters_to_remove:
            i += 1
        else:
            result += word[i]
            i += 1

    return result
        

# Complexity Analysis:
# Time Complexity: O(?) - Description.
# Space Complexity: O(?) - Description.


# -----------------------------------------------------------------------------
# Problem 4: Non-decreasing Array
# -----------------------------------------------------------------------------
'''
Problem:
Write a function...

Example Usage:
()

Example Output:
...
'''
def function(var):
    """
    Description.
    
    Args:
        variable (type): Description.
    """
    pass

# Complexity Analysis:
# Time Complexity: O(?) - Description.
# Space Complexity: O(?) - Description.


# -----------------------------------------------------------------------------
# Problem #: Template
# -----------------------------------------------------------------------------
'''
Problem:
Write a function...

Example Usage:
()

Example Output:
...
'''
def function(var):
    """
    Description.
    
    Args:
        variable (type): Description.
    """
    pass

# Complexity Analysis:
# Time Complexity: O(?) - Description.
# Space Complexity: O(?) - Description.


# -----------------------------------------------------------------------------
# Main execution block for testing
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    # Tests for Problem 1
    print("\n--- Problem 1: template(items, target) ---")
    items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
    target = 'hunny'
    print(linear_search(items, target))

    items = ['bed', 'blue jacket', 'red shirt', 'hunny']
    target = 'red balloon'
    print(linear_search(items, target))

    # Tests for Problem 2
    print("\n--- Problem 2: final_value_after_operations(operations) ---")
    operations = ["trouncy", "flouncy", "flouncy"]
    print(final_value_after_operations(operations))

    operations = ["bouncy", "bouncy", "flouncy"]
    print(final_value_after_operations(operations))

    # Tests for Problem 3
    print("\n--- Problem 3: tiggerfy(word) ---")
    word = "Trigger"
    print(tiggerfy(word))

    word = "eggplant"
    print(tiggerfy(word))

    word = "Choir"
    print(tiggerfy(word))

    # Tests for Problem 4
    print("\n--- Problem #: template(var, x) ---")

    # Tests for Problem 5
    print("\n--- Problem #: template(var, x) ---")

    # Tests for Problem 6
    print("\n--- Problem #: template(var, x) ---")

    # Tests for Problem 7
    print("\n--- Problem #: template(var, x) ---")

    # Tests for Problem 8
    print("\n--- Problem #: template(var, x) ---")

    # TEMPLATE Tests for Problem #
    print("\n--- Problem #: template(var, x) ---")