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
    print("\n--- Problem #: can_pair(item_quantities) ---")

    # Tests for Problem 10
    print("\n--- Problem #: split_haycorns(quantity) ---")

    # Tests for Problem #
    print("\n--- Problem #: template(var, x) ---")
    # print(f"greeting(\"Michael\") => {greeting("Michael")}")
    # print(f"greeting(\"Winnie the Pooh\") => {greeting("Winnie the Pooh")}")