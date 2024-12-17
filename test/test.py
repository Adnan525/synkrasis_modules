# from typing import List
#
#
# def find_combinations(arg_list_tuple: List[tuple]) -> List[tuple]:
#     # Step 1: Initialize an empty set to store unique sums as tuples
#     sums_set = set()
#
#     # Step 2: Add each tuple's elements directly as sums (as single element tuples)
#     for tup in arg_list_tuple:
#         for element in tup:
#             sums_set.add((element,))
#
#     # Step 3: Iterate through pairs of tuples and add their sums
#     n = len(arg_list_tuple)
#     for i in range(n):
#         for j in range(i + 1, n):
#             combined_sum = sum(arg_list_tuple[i]) + sum(arg_list_tuple[j])
#             sums_set.add(tuple(sorted(combined_sum)))
#
#     # Step 4: Continue for higher combinations
#     for r in range(3, n + 1):
#         for combo in combinations(range(n), r):
#             selected_tuples = [arg_list_tuple[idx] for idx in combo]
#             combined_sum = sum(tup)
#             for tup in selected_tuples)
#             sums_set.add(tuple(sorted(combined_sum)))
#
#             # Step 5: Convert the set to a sorted list of tuples
#     return sorted(sums_set)