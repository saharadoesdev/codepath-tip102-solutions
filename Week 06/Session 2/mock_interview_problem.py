## LeetCode Medium 2? Add Two Numbers
# Peer mock interview, i had 15 minutes for the whole problem.
# I didn't get to run my solution but I think I finished, not sure if it works haha

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # A number stored in linked list digit-by-digit in reverse order
        # given two LLs, add the numbers and return them

        # Loop to generate from l1
        curr = l1
        placeValue = 0
        n1 = 0
        while curr:
            n1 += curr.val * (10 ** placeValue)
            curr = curr.next
            placeValue += 1

        # Loop to generate from l2
        curr = l2
        placeValue = 0
        n2 = 0
        while curr:
            n2 += curr.val * (10 ** placeValue)
            curr = curr.next
            placeValue += 1

        sum = n1 + n2 # 807
        # Create a linked list for sum
        digit = sum % 10
        sum = sum // 10
        sumList = ListNode(digit)
        while (sum != 0):
            digit = sum % 10
            sum = sum // 10
            sumList.val = digit
            if (sum != 0):
                sumList.next = ListNode()
                sumList = sumList.next


        