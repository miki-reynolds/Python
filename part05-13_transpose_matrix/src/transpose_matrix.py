def transpose(matrix: list):
    for i in range(len(matrix)):
        for j in range(i+1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# result = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
# def transpose(matrix: list):
#     result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             result[j][i] = matrix[i][j]
#     matrix = result

# transpose(matrix)
# print(matrix)
#
# # 10 = 01
# # 11 = 11
# # 12 = 21
# # [
# #     [1, 4, 7]
# #     [2, 5, 8]
# #     [3, 6, 9]
# # ]
# Program to transpose a matrix using a nested loop
#
# X = [[12,7],
#     [4 ,5],
#     [3 ,8]]
#
# result = [[0,0,0],
#          [0,0,0]]
#
# # iterate through rows
# for i in range(len(X)):
#    # iterate through columns
#    for j in range(len(X[0])):
#        result[j][i] = X[i][j]
#
# for r in result:
#    print(r)
