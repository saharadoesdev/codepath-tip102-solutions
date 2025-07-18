# # Problem 1
# def find_cruise_length(cruise_lengths, vacation_length):
#     def _find_cruise_length(left,right):
#         if left > right:
#             return False
#         pivot = (left+right) // 2
#         if cruise_lengths[pivot] == vacation_length:
#             return True
#         elif cruise_lengths[pivot] < vacation_length:
#             return _find_cruise_length(pivot+1, right)
#         else:
#             return _find_cruise_length(left, pivot-1)
#     return _find_cruise_length(0,len(cruise_lengths)-1)

# print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))
# print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))

# # Problem 2
# def find_cabin_index(cabins, preferred_deck):
#     def _find_cabin_index(left,right):
#         if left > right:
#             return left
#         pivot = (left+right) // 2
#         if cabins[pivot] == preferred_deck:
#             return pivot
#         elif cabins[pivot] < preferred_deck:
#             return _find_cabin_index(pivot+1, right)
#         else:
#             return _find_cabin_index(left, pivot-1)
#     return _find_cabin_index(0,len(cabins)-1)

# print(find_cabin_index([1, 3, 5, 6], 5))
# print(find_cabin_index([1, 3, 5, 6], 2))
# print(find_cabin_index([1, 3, 5, 6], 7))  

# # Problem 3
# def count_checked_in_passengers(rooms):
#     def _count_checked_in_passengers(left, right):
#         if left > right:
#             return len(rooms)
#         pivot = (left+right) // 2
#         if rooms[pivot] == 1:
#             return min(pivot, _count_checked_in_passengers(left, pivot-1))
#         return _count_checked_in_passengers(pivot+1, right)
#     index_1 = _count_checked_in_passengers(0,len(rooms)-1)
#     return len(rooms) - index_1
#     # for i in range(potential_index_1,0,-1):
#     #     if rooms[i] == 1:
            

# rooms1 = [0, 0, 0, 1, 1, 1, 1]
# rooms2 = [0, 0, 0, 0, 0, 1]
# rooms3 = [0, 0, 0, 0, 0, 0]

# print(count_checked_in_passengers(rooms1)) 
# print(count_checked_in_passengers(rooms2))
# print(count_checked_in_passengers(rooms3))

# # Problem 4
# def is_profitable(excursion_counts):
#     n = len(excursion_counts)
#     def _is_profitable(left, right):
#         mid = (left+right) // 2
#         x = n - mid
#         if left > right:
#             return -1
#         if excursion_counts[mid] >= x:
#             if mid == 0 or excursion_counts[mid-1] < x:
#                 return x
#             return _is_profitable(left,mid-1)
#         return _is_profitable(mid+1, right)
#     return _is_profitable(0, n - 1)          

# print(is_profitable([3, 5]))
# print(is_profitable([0, 0]))

# Problem 5
def find_shallowest_point(arr):
    def _find_shallowest_point(left,right):
        if arr[left] < arr[right]:
            return arr[left]
        mid = (left+right) // 2
        # if arr[mid]   ## This is where we stopped!

print(find_shallowest_point([5, 7, 2, 8, 3]))
print(find_shallowest_point([12, 15, 10, 21]))