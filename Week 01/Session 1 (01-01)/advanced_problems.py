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
Given an array `nums` with `n` integers, write a function `non_decreasing()` that
checks if `nums` could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if `nums[i] <= nums[i + 1]` holds for every
`i` (0-based) such that (`0 <= i <= n - 2`).

Example Usage:
nums = [4, 2, 3]
non_decreasing(nums)

nums = [4, 2, 1]
non_decreasing(nums)

Example Output:
True
False
'''
def non_decreasing(nums):
    """
    Description.
    
    Args:
        variable (type): Description.
    """
    # Check for if array is non-decreasing
    # If problem element found, modify it (set changedYet to True)
    # Continue checking elements
    # More examples: 3 4 2 3 (False), 1 4 2 3 (True)

    changedYet = False
    for i in range(len(nums) - 1):
        if not nums[i] <= nums[i + 1]:  # If problem found
            if not changedYet:  # Element could be modified to fix
                changedYet = True
                # Try fixing
                if i > 0 and nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = nums[i]
            else:   # If an element has already been modified, can't be nondecreasing with one modification
                return False
    return True

# Complexity Analysis:
# Time Complexity: O(n) - Checks each element in the array once.
# Space Complexity: O(1) - Uses the same amount of space regardless of input size; no new data structures.


# -----------------------------------------------------------------------------
# Problem 5: Missing Clues
# -----------------------------------------------------------------------------
'''
Problem:
Christopher Robin set up a scavenger hunt for Pooh, but it's a blustery day and
several hidden clues have blown away. Write a function `find_missing_clues()` to
help Christopher Robin figure out which clues he needs to remake. The function
accepts two integers `lower` and `upper` and a unique integer array `clues`. All
elements in `clues` are within the inclusive range `[lower, upper]`.

A clue `x` is considered missing if `x` is in the range `[lower, upper]` and
`x` is not in `clues`.

Return the shortest sorted list of ranges that exactly covers all the missing
numbers. That is, no element of `clues` is included in any of the ranges, and
each missing number is covered by one of the ranges.

Example Usage:
clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
find_missing_clues(clues, lower, upper)

clues = [-1]
lower = -1
upper = -1
find_missing_clues(clues, lower, upper)

Example Output:
[[2, 2], [4, 49], [51, 74], [76, 99]]
[]
'''
def find_missing_clues(clues, lower, upper):
    """
    Description.
    
    Args:
        variable (type): Description.
    """
    missing_clues = []
    x = lower
    i = 1    # i tracks current position in clues
    while x <= upper and i < len(clues) - 1:
        if x not in clues:
            new_list = [x]
            new_list.append(clues[i + 1] - 1)
            missing_clues.append(new_list)
            x = clues[i + 1]
            i += 1
        x += 1
    # If reached end of clues, but still more missing:
    if x <= upper:
        if x not in clues:
            new_list = [x]
            new_list.append(upper)
            missing_clues.append(new_list)

    return missing_clues

# Complexity Analysis:
# Time Complexity: O(?) - Description.
# Space Complexity: O(?) - Description.


# -----------------------------------------------------------------------------
# Problem 6: Vegetable Harvest
# -----------------------------------------------------------------------------
'''
Problem:
Rabbit is collecting carrots from his garden to make a feast for Pooh and friends.
Write a function `harvest()` that accepts a 2D `n x m` matrix `vegetable_patch`
and returns the number of of carrots that are ready to harvest in the vegetable
patch. A carrot is ready to harvest if `vegetable_patch[i][j]` has value 'c'.

Assume `n = len(vegetable_patch)` and `m = len(vegetable_patch[0])`.
`0 <= i < n` and `0 <= j < m`.

Example Usage:
vegetable_patch = [
	['x', 'c', 'x'],
	['x', 'x', 'x'],
	['x', 'c', 'c'],
	['c', 'c', 'c']
]
harvest(vegetable_patch)

Example Output:
6
'''
def harvest(vegetable_patch):
    """
    Description.
    
    Args:
        variable (type): Description.
    """
    carrots_ready = 0
    for row in vegetable_patch:
        for col in row:
            if col == 'c':
                carrots_ready += 1
    return carrots_ready

# Complexity Analysis:
# Time Complexity: O(n) - Checks each element in the matrix exactly once.
# Space Complexity: O(1) - Uses the same amount of space regardless of input size; no new data structures created.


# -----------------------------------------------------------------------------
# Problem 7: Eeyore's House
# -----------------------------------------------------------------------------
'''
Problem:
Eeyore has collected two piles of sticks to rebuild his house and needs to choose
pairs of sticks whose lengths are the right proportion. Write a function `good_pairs()`
that accepts two integer arrays `pile1` and `pile2` where each integer represents
the length of a stick. The function also accepts a positive integer `k`. The function
should return the number of good pairs.

A pair `(i, j)` is called good if `pile1[i]` is divisible by `pile2[j] * k`.
Assume `0 <= i <= len(pile1) - 1` and `0 <= j <= len(pile2) - 1`.

Example Usage:
pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
good_pairs(pile1, pile2, k)

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
good_pairs(pile1, pile2, k)

Example Output:
5
2
'''
def good_pairs(pile1, pile2, k):
    """
    Description.
    
    Args:
        variable (type): Description.
    """
    # Count how many times each possible divisor pile2[j] * k appears
    counts = {}
    for stick in pile2:
        divisor = stick * k
        if divisor in counts:
            counts[divisor] += 1
        else:
            counts[divisor] = 1

    good_count = 0
    for stick in pile1:
        for divisor in counts:
            if stick % divisor == 0:    # If valid divisor
                good_count += counts[divisor]

    return good_count

# Complexity Analysis:
# Time Complexity: O(m * d) - m = len(pile1) d = number of unique divisors (d <= len(pile2)).
# Space Complexity: O(d) - d = number of unique divisors (d <= len(pile2)), stored in a dictionary.


# -----------------------------------------------------------------------------
# Problem 8: Local Maximums
# -----------------------------------------------------------------------------
'''
Problem:
Write a function `local_maximums()` that accepts an `n x n` integer matrix `grid`
and returns an integer matrix `local_maxes` of size `(n - 2) x (n - 2)` such that:

`local_maxes[i][j]` is equal to the largest value of the `3 x 3` matrix in `grid`
centered around row `i + 1` and column `j + 1`.

In other words, we want to find the largest value in every contiguous `3 x 3` matrix in `grid`.

Example Usage:
grid = [
	[9, 9, 8, 1],
	[5, 6, 2, 6],
	[8, 2, 6, 4],
	[6, 2, 2, 2]
]
local_maximums(grid)

grid = [
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 2, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1]
]
local_maximums(grid)

Example Output:
[[9, 9], [8, 6]]
[[2, 2, 2], [2, 2, 2], [2, 2, 2]]
'''
def local_maximums(grid):
    """
    Description.
    
    Args:
        variable (type): Description.
    """
    # Create empty result matrix based on original size
    n = len(grid[0]) - 2
    result_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # Find local max
            local_max = grid[i][j]
            # Check 3x3 centered at i+1,j+1
            for i2 in range(i, i + 3):
                for j2 in range(j, j + 3):
                    val = grid[i2][j2]
                    if val > local_max:
                        local_max = val
            result_matrix[i][j] = local_max

    return result_matrix

# Complexity Analysis:
# Time Complexity: O(n^2) - n x n input matrix, checking every element.
# Space Complexity: O((n-2)^2) - The size of the result matrix.


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
    print("\n--- Problem 4: non_decreasing(nums) ---")
    nums = [4, 2, 3]
    print(non_decreasing(nums))

    nums = [4, 2, 1]
    print(non_decreasing(nums))

    # Tests for Problem 5
    print("\n--- Problem 5: find_missing_clues(clues, lower, upper) ---")
    clues = [0, 1, 3, 50, 75]
    lower = 0
    upper = 99
    print(find_missing_clues(clues, lower, upper))

    clues = [-1]
    lower = -1
    upper = -1
    print(find_missing_clues(clues, lower, upper))

    # Tests for Problem 6
    print("\n--- Problem 6: harvest(vegetable_patch) ---")
    vegetable_patch = [
        ['x', 'c', 'x'],
        ['x', 'x', 'x'],
        ['x', 'c', 'c'],
        ['c', 'c', 'c']
    ]
    print(harvest(vegetable_patch))

    # Tests for Problem 7
    print("\n--- Problem 7: good_pairs(pile1, pile2, k) ---")
    pile1 = [1, 3, 4]
    pile2 = [1, 3, 4]
    k = 1
    print(good_pairs(pile1, pile2, k))

    pile1 = [1, 2, 4, 12]
    pile2 = [2, 4]
    k = 3
    print(good_pairs(pile1, pile2, k))

    # Tests for Problem 8
    print("\n--- Problem #: local_maximums(grid) ---")
    grid = [
        [9, 9, 8, 1],
        [5, 6, 2, 6],
        [8, 2, 6, 4],
        [6, 2, 2, 2]
    ]
    print(local_maximums(grid))

    grid = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 2, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    print(local_maximums(grid))