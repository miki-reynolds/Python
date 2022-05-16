



# def longest_series_of_neighbours(numbers: list):
#     # Global variable to keep track of the final output
#     g_longest = 0
    
#     for index in range(len(numbers)-1):
#         l_longest = 1

#         cur = numbers[index]
#         next = numbers[index + 1]

#         while abs(cur - next) == 1 and (index + 1) < len(numbers):
#             cur = numbers[index]
#             next = numbers[index + 1]
        
#             l_longest += 1
#             index += 1

#         # This allows you to update the global tracker only if the local variable found a larger/better value
#         g_longest = max(g_longest, l_longest)
        
  
#     # if g_longest % 2 != 0:
#     #     result = g_longest - 1

#     return g_longest

# my_list = [1, 2, 3, 5, 6, 9, 10]
# # [1, 2, 10, 7, 6, 5, 6, 3, 4, 1, 0]
# print(longest_series_of_neighbours(my_list))