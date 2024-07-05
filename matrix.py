import numpy as np


edges = [
    (1, 2), (2, 3), (3, 4), (4, 5), (5, 6),
    (7, 8), (8, 9), (9, 3), (3, 10), (10, 5),
    (5, 11), (11, 12), (12, 13), (8, 12), (12, 14),
    (5, 15)
]


max_node = max(max(ori, des) for ori, des in edges)


symmetric_demand_matrix = np.zeros((max_node, max_node), dtype=int)


for i in range(max_node):
    for j in range(i+1, max_node):  # 只遍历上三角部分，不包括对角线
        symmetric_demand_matrix[i][j] = np.random.randint(1, 10)


symmetric_demand_matrix = symmetric_demand_matrix + symmetric_demand_matrix.T


print("Symmetric Demand Matrix:")
print(symmetric_demand_matrix)