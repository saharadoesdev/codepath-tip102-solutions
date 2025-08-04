# Week 01, Session 1 (01-01) - Standard Problems

# -----------------------------------------------------------------------------
# Problem 1: Hundred Acre Wood
# -----------------------------------------------------------------------------
'''
Problem:
Write a function `welcome()` that prints the string "Welcome to The Hundred Acre Wood!".

Example Usage:
welcome()

Example Output:
Welcome to The Hundred Acre Wood!
'''
def welcome():
    """Prints a welcome message to the console."""
    print("Welcome to The Hundred Acre Wood!")

# Complexity Analysis:
# Time Complexity: O(1) - The operation takes a constant amount of time, regardless of input.
# Space Complexity: O(1) - The memory used does not scale with any input.


# -----------------------------------------------------------------------------
# Problem 2: Greeting
# -----------------------------------------------------------------------------
'''
Problem:
Write a function `greeting()` that accepts a single parameter, a string `name`, and prints
the string "Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin."

Example Usage:
greetings("Michael")
greetings("Winnie the Pooh")

Example Output:
Welcome to The Hundred Acre Wood Michael! My name is Christopher Robin.
Welcome to The Hundred Acre Wood Winnie the Pooh! My name is Christopher Robin.

Note:
The problem description asks for a function named `greeting`, but the
example usage shows `greetings`. I will be using `greeting` as per
the main prompt.
'''
def greeting(name):
    """
    Greets a person and welcomes them to the Hundred Acre Wood.
    
    Args:
        name (str): The name of the person to greet.
    """
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")

# Complexity Analysis:
# Time Complexity: O(1) - The operation takes a constant amount of time, regardless of input.
# Space Complexity: O(1) - The memory used does not scale with any input.


# -----------------------------------------------------------------------------
# Problem 3: Catchphrase
# -----------------------------------------------------------------------------
'''
Problem:
Write a function `print_catchphrase()` that accepts a string `character` as a parameter
and prints the catchphrase of the given character as outlined in the table below.

| Character           | Catchphrase                  |
|---------------------|------------------------------|
| "Pooh"              | "Oh bother!"                 |
| "Tigger"            | "TTFN: Ta-ta for now!"       |
| "Eeyore"            | "Thanks for noticing me."    |
| "Christopher Robin" | "Silly old bear."            |

If the given `character` does not match one of the characters included above,
print "Sorry! I don't know <character>'s catchphrase!"

Example Usage:
character = "Pooh"
print_catchphrase(character)

character = "Piglet"
print_catchphrase(character)

Example Output:
"Oh bother!"
"Sorry! I don't know Piglet's catchphrase!"
'''
def print_catchphrase(character):
    """
    Prints the catchphrase for a given character.

    If the character is not found, a "not found" message is printed instead.
    
    Args:
        character (str): The character whose catchphrase should be printed.
    """
    if (character == "Pooh"):
        print("Oh bother!")
    elif (character == "Tigger"):
        print("TTFN: Ta-ta for now!")
    elif (character == "Eeyore"):
        print("Thanks for noticing me.")
    elif (character == "Christopher Robin"):
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")

# Complexity Analysis:
# Time Complexity: O(n)?
# Space Complexity: O(1) - The memory used does not scale with any input.


# -----------------------------------------------------------------------------
# Problem 4: Return Item
# -----------------------------------------------------------------------------
'''
Problem:
Implement a function `get_item()` that accepts a 0-indexed list `items` and a
non-negative integer `x` and returns the element at index `x` in `items`. If `x`
is not a valid index of `items`, return `None`.

Example Usage:
items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
get_item(items, x)

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
get_item(items, x)

Example Output:
"roo"
None

Note: This example outputs has quotation marks around `roo`, while my solution does not.
'''
def get_item(items, x):
    """
    Description.
    
    Args:
        variable (type): Description.
    """
    return items[x] if x < len(items) else None

# Complexity Analysis:
# Time Complexity: O(?) - Description.
# Space Complexity: O(?) - Description.



# -----------------------------------------------------------------------------
# Problem 5: Total Honey
# -----------------------------------------------------------------------------
'''
Problem:
Winnie the Pooh wants to know how much honey he has. Write a function `sum_honey()`
that accepts a list of integers `hunny_jars` and returns the sum of all elements in
the list. Do not use the built-in function `sum()`.

Example Usage:
hunny_jars = [2, 3, 4, 5]
sum_honey(hunny_jars)

hunny_jars = []
sum_honey(hunny_jars)

Example Output:
14
0
'''
def sum_honey(hunny_jars):
    """
    Description.
    
    Args:
        variable (type): Description.
    """
    sum = 0
    for num in hunny_jars:
        sum += num
    return sum

# Complexity Analysis:
# Time Complexity: O(?) - Description.
# Space Complexity: O(?) - Description.


# -----------------------------------------------------------------------------
# Problem 6: Double Trouble
# -----------------------------------------------------------------------------
'''
Problem:
Help Winnie the Pooh double his honey! Write a function `doubled()` that accepts
a list of integers `hunny_jars` as a parameter and multiplies each element in
the list by two. Return the doubled list.

Example Usage:
hunny_jars = [1, 2, 3]
doubled(hunny_jars)

Example Output:
[2, 4, 6]
'''
def doubled(hunny_jars):
    """
    Description.
    
    Args:
        variable (type): Description.
    """
    for i in range(len(hunny_jars)):
        hunny_jars[i] *= 2
    return hunny_jars

# Complexity Analysis:
# Time Complexity: O(?) - Description.
# Space Complexity: O(?) - Description.


# -----------------------------------------------------------------------------
# Problem 7: Poohsticks
# -----------------------------------------------------------------------------
'''
Problem:
Winnie the Pooh and his friends are playing a game called Poohsticks where they
drop sticks in a stream and race them. They time how long it takes each player's
stick to float under Poohsticks Bridge to score each round.

Write a function `count_less_than()` to help Pooh and his friends determine how
many players should move on to the next round of Poohsticks. `count_less_than()`
should accept a list of integers `race_times` and an integer `threshold` and return
the number of race times less than `threshold`.

Example Usage:
race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
count_less_than(race_times, threshold)

race_times = []
threshold = 4
count_less_than(race_times, threshold)

Example Output:
3
0
'''
def count_less_than(race_times, threshold):
    """
    Description.
    
    Args:
        variable (type): Description.
    """
    count = 0
    for time in race_times:
        if time < threshold:
            count += 1
    return count

# Complexity Analysis:
# Time Complexity: O(?) - Description.
# Space Complexity: O(?) - Description.


# -----------------------------------------------------------------------------
# Problem 8: Pooh's To Do's
# -----------------------------------------------------------------------------
'''
Problem:
Write a function `print_todo_list()` that accepts a list of strings named `tasks`.
The function should then number and print each task on a new line using the format:

Pooh's To Dos:
1. Task 1
2. Task 2
...

Example Usage:
task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)

Example Output:
Pooh's To Dos:
1. Count all the bees in the hive
2. Chase all the clouds from the sky
3. Think
4. Stoutness Exercises

Pooh's To Dos:

Note: The problem statement says "tasks" is the list's name, while the example
usage has "task". My solution uses "task" to match the example usage
'''
def print_todo_list(task):
    """
    Description.
    
    Args:
        variable (type): Description.
    """
    print("Pooh's To Dos:")
    for i in range(len(task)):
        print(f"{i + 1}. {task[i]}")

# Complexity Analysis:
# Time Complexity: O(?) - Description.
# Space Complexity: O(?) - Description.


# -----------------------------------------------------------------------------
# Problem #: Template
# -----------------------------------------------------------------------------
'''
Problem:
Rabbit is very particular about his belongings and wants to own an even number of
each thing he owns. Write a function `can_pair()` that accepts a list of integers
`item_quantities`. Return `True` if each number in `item_quantities` is even.
Return `False` otherwise.

Example Usage:
item_quantities = [2, 4, 6, 8]
can_pair(item_quantities)

item_quantities = [1, 2, 3, 4]
can_pair(item_quantities)

item_quantities = []
can_pair(item_quantities)

Example Output:
True
False
True
'''
def can_pair(item_quantities):
    """
    Description.
    
    Args:
        variable (type): Description.
    """
    for quantity in item_quantities:
        if quantity % 2 != 0:
            return False
    return True

# Complexity Analysis:
# Time Complexity: O(?) - Description.
# Space Complexity: O(?) - Description.


# -----------------------------------------------------------------------------
# Problem 10: Split Haycorns
# -----------------------------------------------------------------------------
'''
Problem:
Piglet's has collected a big pile of his favorite food, haycorns, and wants to
split them evenly amongst his friends. Write a function `split_haycorns()` to
help Piglet determine the number of ways he can split his haycorns into even
groups. `split_haycorns()` accepts a positive integer `quantity` as a parameter
and returns a list of all divisors of quantity.

Example Usage:
quantity = 6
split_haycorns(quantity)

quantity = 1
split_haycorns(quantity)

Example Output:
[1, 2, 3, 6]
[1]
'''
def split_haycorns(quantity):
    """
    Description.
    
    Args:
        variable (type): Description.
    """
    divisors = set()
    for i in range(1, int(quantity ** 0.5) + 1):
        if quantity % i == 0:
            divisors.add(i)
            divisors.add(quantity // i)

    return sorted(divisors)

# Complexity Analysis:
# Time Complexity: O(?) - Description.
# Space Complexity: O(?) - Description.


# -----------------------------------------------------------------------------
# Problem 11: T-I-Double Guh-ER
# -----------------------------------------------------------------------------
'''
Problem:
Signs in the Hundred Acre Wood have been losing letters as Tigger bounces around
stealing any letters he needs to spell out his name. Write a function `tiggerfy()`
that accepts a string `s`, and returns a new string with the letters `t`, `i`,
`g`, `e`, and `r` removed from it.

Example Usage:
s = "suspicerous"
tiggerfy(s)

s = "Trigger"
tiggerfy(s)

s = "Hunny"
tiggerfy(s)

Example Output:
"suspcous"
""
"Hunny"
'''
def tiggerfy(s):
    """
    Description.
    
    Args:
        variable (type): Description.
    """
    letters_to_remove = "tiger"
    result = ""
    for letter in s:
        if letter.lower() not in letters_to_remove:
            result += letter
    return result

    # Alternative simple one-liner solution:
    # return ''.join([letter for letter in s if letter.lower() not in "tiger"])

# Complexity Analysis:
# Time Complexity: O(?) - Description.
# Space Complexity: O(?) - Description.


# -----------------------------------------------------------------------------
# Problem 12: Thistle Hunt
# -----------------------------------------------------------------------------
'''
Problem:
Pooh, Piglet, and Roo are looking for thistles to gift their friend Eeyore. Write
a function `locate_thistles()` that takes in a list of strings `items` and returns
a list of the indices of any elements with value `"thistle"`. The indices in the
resulting list should be ordered from least to greatest.

Example Usage:
items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
locate_thistles(items)

items = ["book", "bouncy ball", "leaf", "red balloon"]
locate_thistles(items)

Example Output:
[0, 3]
[]
'''
def locate_thistles(items):
    """
    Description.
    
    Args:
        variable (type): Description.
    """
    indices = []
    for i in range (0, len(items)):
        if items[i] == "thistle":
            indices.append(i)
    return indices

# Complexity Analysis:
# Time Complexity: O(?) - Description.
# Space Complexity: O(?) - Description.


# -----------------------------------------------------------------------------
# Main execution block for testing
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    # Tests for Problem 1
    print("--- Problem 1: welcome() ---")
    welcome()

    # Tests for Problem 2
    print("\n--- Problem 2: greeting(name) ---")
    greeting("Michael")
    greeting("Winnie the Pooh")

    # Tests for Problem 3
    print("\n--- Problem 3: print_catchphrase(character) ---")
    character = "Pooh"
    print_catchphrase(character)
    character = "Piglet"
    print_catchphrase(character)

    # Tests for Problem 4
    print("\n--- Problem 4: get_item(items, x) ---")
    items = ["piglet", "pooh", "roo", "rabbit"]
    x = 2
    print(get_item(items, x))

    items = ["piglet", "pooh", "roo", "rabbit"]
    x = 5
    print(get_item(items, x))

    # Tests for Problem 5
    print("\n--- Problem 5: sum_honey(hunny_jars) ---")
    hunny_jars = [2, 3, 4, 5]
    print(sum_honey(hunny_jars))

    hunny_jars = []
    print(sum_honey(hunny_jars))

    # Tests for Problem 6
    print("\n--- Problem 6: doubled(hunny_jars) ---")
    hunny_jars = [1, 2, 3]
    print(doubled(hunny_jars))

    # Tests for Problem 7
    print("\n--- Problem 7: count_less_than(race_times, threshold) ---")
    race_times = [1, 2, 3, 4, 5, 6]
    threshold = 4
    print(count_less_than(race_times, threshold))

    race_times = []
    threshold = 4
    print(count_less_than(race_times, threshold))

    # Tests for Problem 8
    print("\n--- Problem 8: print_todo_list(task) ---")
    task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
    print_todo_list(task)

    task = []
    print_todo_list(task)

    # Tests for Problem 9
    print("\n--- Problem 9: can_pair(item_quantities) ---")
    item_quantities = [2, 4, 6, 8]
    print(can_pair(item_quantities))

    item_quantities = [1, 2, 3, 4]
    print(can_pair(item_quantities))

    item_quantities = []
    print(can_pair(item_quantities))

    # Tests for Problem 10
    print("\n--- Problem 10: split_haycorns(quantity) ---")
    quantity = 6
    print(split_haycorns(quantity))

    quantity = 1
    print(split_haycorns(quantity))

    # Tests for Problem 11
    print("\n--- Problem 11: tiggerfy(s) ---")

    s = "suspicerous"
    print(tiggerfy(s))

    s = "Trigger"
    print(tiggerfy(s))

    s = "Hunny"
    print(tiggerfy(s))

    # Tests for Problem 12
    print("\n--- Problem 12: locate_thistles(items) ---")
    items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
    print(locate_thistles(items))

    items = ["book", "bouncy ball", "leaf", "red balloon"]
    print(locate_thistles(items))