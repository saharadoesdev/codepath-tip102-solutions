# Week 01, Session 2 (01-02) - Standard Problem Set Version 1

# -----------------------------------------------------------------------------
# Problem 1: Reverse Sentence
# -----------------------------------------------------------------------------
'''
Problem:
Write a function `reverse_sentence()` that takes in a string `sentence` and returns
the sentence with the order of the words reversed. The sentence will contain only
alphabetic characters and spaces to separate the words. If there is only one word
in the sentence, the function should return the original string.

Example Usage:
sentence = "tubby little cubby all stuffed with fluff"
reverse_sentence(sentence)

sentence = "Pooh"
reverse_sentence(sentence)

Example Output:
"fluff with stuffed all cubby little tubby"
"Pooh"
'''
def reverse_sentence(sentence):
    """
    Description.
    
    Args:
        variable (type): Description.
    """
    words = sentence.split()
    words.reverse()
    return " ".join(words)

# Complexity Analysis:
# Time Complexity: O(n) - Splits sentence into words; n = number of characters in input.
# Space Complexity: O(n) - Stores list of words.


# -----------------------------------------------------------------------------
# Problem 2: Goldilocks Number
# -----------------------------------------------------------------------------
'''
Problem:
In the extended universe of fictional bears, Goldilocks finds an enticing list
of numbers in the Three Bears' house. She doesn't want to take a number that's
too high or too low - she wants a number that's juuust right. Write a function
`goldilocks_approved()` that takes in the list of distinct positive integers `nums`
and returns any number from the list that is neither the minimum nor the maximum
value in the array, or -1 if there is no such number.

Return the selected integer.

Example Usage:
nums = [3, 2, 1, 4]
goldilocks_approved(nums)

nums = [1, 2]
goldilocks_approved(nums)

nums = [2, 1, 3]
goldilocks_approved(nums)

Example Output:
2
-1
2

Note: The example output returns 2 for the first input, while mine returns 3,
which is also correct because it only has to return any value that is not the
min or max (so for [3, 2, 1, 4], where the minimum value is 1 and the maximum
value is 4, 2 and 3 are both valid Goldilocks numbers).
'''
def goldilocks_approved(nums):
    """
    Description.
    
    Args:
        variable (type): Description.
    """
    min_val = min(nums)
    max_val = max(nums)
    for num in nums:
        if num != min_val and num != max_val:
            return num
    return -1   # If no number found

# Complexity Analysis:
# Time Complexity: O(n) - Checks at most every element in the input array.
# Space Complexity: O(1) - No extra data structures used; space doesn't depend on input size.


# -----------------------------------------------------------------------------
# Problem 3: Delete Minimum
# -----------------------------------------------------------------------------
'''
Problem:
Pooh is eating all of his hunny jars in order of smallest to largest. Given a list
of integers `hunny_jar_sizes`, write a function `delete_minimum_elements()` that
continuously removes the minimum element until the list is empty. Return a new list
of the elements of `hunny_jar_sizes` in the order in which they were removed.

Example Usage:
hunny_jar_sizes = [5, 3, 2, 4, 1]
delete_minimum_elements(hunny_jar_sizes)

hunny_jar_sizes = [5, 2, 1, 8, 2]
delete_minimum_elements(hunny_jar_sizes)

Example Output:
[1, 2, 3, 4, 5]
[1, 2, 2, 5, 8]
'''
def delete_minimum_elements(hunny_jar_sizes):
    """
    Removes the minimum element from hunny_jar_sizes repeatedly until empty.
    Returns a list of elements in the order they were removed.

    Args:
        hunny_jar_sizes (list of int): List of jar sizes.

    Returns:
        list of int: Elements in order of removal.
    """
    result = []
    while hunny_jar_sizes:
        min_val = min(hunny_jar_sizes)
        result.append(min_val)
        hunny_jar_sizes.remove(min_val)
    return result

# Complexity Analysis:
# Time Complexity: O(n) - Runs the while loop n times, where n = len(hunny_jar_sizes).
# Space Complexity: O(n) - Output list is the same size as input list.


# -----------------------------------------------------------------------------
# Problem 4: Sum of Digits
# -----------------------------------------------------------------------------
'''
Problem:
Write a function `sum_of_digits()` that accepts an integer `num` and returns the
sum of `num`'s digits.

Example Usage:
num = 423
sum_of_digits(num)

num = 4
sum_of_digits(num)

Example Output:
9 # Explanation: 4 + 2 + 3 = 9
4 
'''
def sum_of_digits(num):
    """
    Description.
    
    Args:
        variable (type): Description.
    """
    sum = 0
    while num != 0:
        sum += num % 10
        num = num // 10
    return sum

# Complexity Analysis:
# Time Complexity: O(n) - Runs the while loop n times, where n = number of digits in num.
# Space Complexity: O(1) - No new data structures created; space used does not depend on input size.


# -----------------------------------------------------------------------------
# Problem 5: Bouncy, Flouncy, Trouncy, Pouncy
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

Note: This is the same problem as Week 1, Session 1 (01-01) Advanced Problem #2.
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
# Time Complexity: O(n) - Checks each element in input array.
# Space Complexity: O(1) - No new data structures created; space used does not depend on input size.


# -----------------------------------------------------------------------------
# Problem 6: Acronym
# -----------------------------------------------------------------------------
'''
Problem:
Given an array of strings `words` and a string `s`, implement a function `is_acronym()`
that returns `True` if `s` is an acronym of `words` and returns `False` otherwise.

The string `s` is considered an acronym of `words` if it can be formed by concatenating
the first character of each string in `words` in order. For example, "pb" can be formed
from `["pooh"", "bear"]`, but it can't be formed from `["bear", "pooh"]`.

Example Usage:
words = ["christopher", "robin", "milne"]
s = "crm"
is_acronym(words, s)

Example Output:
True
'''
def is_acronym(words, s):
    """
    Description.
    
    Args:
        variable (type): Description.
    """
    acronym = ""
    for word in words:
        acronym += word[0]
    return acronym == s

# Complexity Analysis:
# Time Complexity: O(?) - Description.
# Space Complexity: O(?) - Description.


# -----------------------------------------------------------------------------
# Problem 7: Good Things Come in Threes
# -----------------------------------------------------------------------------
'''
Problem:
Write a function `make_divisible_by_3()` that accepts an integer array `nums`. In
one operation, you can add or subtract `1` from any element of `nums`. Return the
minimum number of operations to make all elements of `nums` divisible by 3.

Example Usage:
nums = [1, 2, 3, 4]
make_divisible_by_3(nums)

nums = [3, 6, 9]
make_divisible_by_3(nums)

Example Output:
3
0
'''
def make_divisible_by_3(nums):
    """
    Description.
    
    Args:
        variable (type): Description.
    """
    count = 0
    for num in nums:
        if num % 3 != 0:
            count += 1  # No need to actually modify element
    return count

# Complexity Analysis:
# Time Complexity: O(?) - Description.
# Space Complexity: O(?) - Description.


# -----------------------------------------------------------------------------
# Problem 8: Exclusive Elements
# -----------------------------------------------------------------------------
'''
Problem:
Given two lists `lst1` and `lst2`, write a function `exclusive_elemts()` that
returns a new list that contains the elements which are in `lst1` but not in
`lst2` and the elements that are in `lst2` but not in `lst1`.

Example Usage:
lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
exclusive_elemts(lst1, lst2)

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
exclusive_elemts(lst1, lst2)

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
exclusive_elemts(lst1, lst2)

Example Output:
["pooh", "roo", "eeyore", "owl"]
["pooh", "roo", "piglet", "eeyore", "owl", "kanga"]
[]
'''
def exclusive_elemts(lst1, lst2):
    """
    Description.
    
    Args:
        variable (type): Description.
    """
    exclusive = []
    for elt in lst1:
        if elt not in lst2:
            exclusive.append(elt)

    for elt in lst2:
        if elt not in lst1:
            exclusive.append(elt)

    return exclusive

# Complexity Analysis:
# Time Complexity: O(?) - Description.
# Space Complexity: O(?) - Description.


# -----------------------------------------------------------------------------
# Problem 9: Merge Strings Alternately
# -----------------------------------------------------------------------------
'''
Problem:
Write a function `merge_alternately()` that accepts two strings `word1` and
`word2`. Merge the strings by adding letters in alternating order, starting
with `word1`. If a string is longer than the other, append the additional
letters onto the end of the merged string.

Return the merged string.

Example Usage:
word1 = "wol"
word2 = "oze"
merge_alternately(word1, word2)

word1 = "hfa"
word2 = "eflump"
merge_alternately(word1, word2)

word1 = "eyre"
word2 = "eo"
merge_alternately(word1, word2)

Example Output:
"woozle"
"heffalump"
"eeyore"
'''
def merge_alternately(word1, word2):
    """
    Description.
    
    Args:
        variable (type): Description.
    """
    result = ""
    len1, len2 = len(word1), len(word2)
    min_length = min(len1, len2)
    for i in range(min_length):
        result += word1[i] + word2[i]

    # Append any leftover letters
    result += word1[min_length:]
    result += word2[min_length:]

    return result

# Complexity Analysis:
# Time Complexity: O(?) - Description.
# Space Complexity: O(?) - Description.


# -----------------------------------------------------------------------------
# Problem 10: Eeyore's House
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

Note: This is the same problem as Week 1, Session 1 (01-01) Advanced Problem #2.
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
# Main execution block for testing
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    # Tests for Problem 1
    print("\n--- Problem 1: reverse_sentence(sentence) ---")
    sentence = "tubby little cubby all stuffed with fluff"
    print(reverse_sentence(sentence))

    sentence = "Pooh"
    print(reverse_sentence(sentence))

    # Tests for Problem 2
    print("\n--- Problem 2: goldilocks_approved(nums) ---")
    nums = [3, 2, 1, 4]
    print(goldilocks_approved(nums))

    nums = [1, 2]
    print(goldilocks_approved(nums))

    nums = [2, 1, 3]
    print(goldilocks_approved(nums))

    # Tests for Problem 3
    print("\n--- Problem 3: delete_minimum_elements(hunny_jar_sizes) ---")
    hunny_jar_sizes = [5, 3, 2, 4, 1]
    print(delete_minimum_elements(hunny_jar_sizes))

    hunny_jar_sizes = [5, 2, 1, 8, 2]
    print(delete_minimum_elements(hunny_jar_sizes))

    # Tests for Problem 4
    print("\n--- Problem 4: sum_of_digits(num) ---")
    num = 423
    print(sum_of_digits(num))

    num = 4
    print(sum_of_digits(num))

    # Tests for Problem 5
    print("\n--- Problem 5: final_value_after_operations(operations) ---")
    operations = ["trouncy", "flouncy", "flouncy"]
    print(final_value_after_operations(operations))

    operations = ["bouncy", "bouncy", "flouncy"]
    print(final_value_after_operations(operations))

    # Tests for Problem 6
    print("\n--- Problem 6: is_acronym(words, s) ---")
    words = ["christopher", "robin", "milne"]
    s = "crm"
    print(is_acronym(words, s))

    # Tests for Problem 7
    print("\n--- Problem 7: make_divisible_by_3(nums) ---")
    nums = [1, 2, 3, 4]
    print(make_divisible_by_3(nums))

    nums = [3, 6, 9]
    print(make_divisible_by_3(nums))

    # Tests for Problem 8
    print("\n--- Problem 8: exclusive_elemts(lst1, lst2) ---")
    lst1 = ["pooh", "roo", "piglet"]
    lst2 = ["piglet", "eeyore", "owl"]
    print(exclusive_elemts(lst1, lst2))

    lst1 = ["pooh", "roo"]
    lst2 = ["piglet", "eeyore", "owl", "kanga"]
    print(exclusive_elemts(lst1, lst2))

    lst1 = ["pooh", "roo", "piglet"]
    lst2 = ["pooh", "roo", "piglet"]
    print(exclusive_elemts(lst1, lst2))

    # Tests for Problem 9
    print("\n--- Problem 9: merge_alternately(word1, word2) ---")
    word1 = "wol"
    word2 = "oze"
    print(merge_alternately(word1, word2))

    word1 = "hfa"
    word2 = "eflump"
    print(merge_alternately(word1, word2))

    word1 = "eyre"
    word2 = "eo"
    print(merge_alternately(word1, word2))

    # Tests for Problem 10
    print("\n--- Problem 10: good_pairs(pile1, pile2, k) ---")
    pile1 = [1, 3, 4]
    pile2 = [1, 3, 4]
    k = 1
    print(good_pairs(pile1, pile2, k))

    pile1 = [1, 2, 4, 12]
    pile2 = [2, 4]
    k = 3
    print(good_pairs(pile1, pile2, k))