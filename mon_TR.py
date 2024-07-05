import numpy as np
import random


edges = {
    (1, 2): 1,
    (2, 3): 1,
    (3, 4): 1,
    (4, 5): 1,
    (5, 6): 1,
    (7, 8): 2,
    (8, 9): 2,
    (9, 3): 2,
    (3, 10): 2,
    (10, 5): 2,
    (5, 11): 2,
    (11, 12): 2,
    (12, 13): 2,
    (8, 12): 3,
    (12, 14): 3,
    (5, 15): 4,
}


observed_times = {edge: np.random.normal(loc=random.uniform(4, 10),
                                         scale=random.uniform(0.5, 2.0),
                                         size=random.randint(5, 15)).tolist()
                  for edge in edges}

eta_1 = 0.5


def expected_average_running_time(T_ij):
    return np.mean(T_ij)



def buffer_time(T_ij):
    return np.std(T_ij, ddof=1)



def reliable_running_time(E_T_ij, sigma_T_ij, eta_1):
    return E_T_ij + eta_1 * sigma_T_ij


line_reliable_times = {}
for edge, times in observed_times.items():
    line_id = edges[edge]
    E_T_ij = expected_average_running_time(times)
    sigma_T_ij = buffer_time(times)
    R_T_ij = reliable_running_time(E_T_ij, sigma_T_ij, eta_1)

    if line_id not in line_reliable_times:
        line_reliable_times[line_id] = R_T_ij
    else:
        line_reliable_times[line_id] += R_T_ij


sorted_lines = sorted(line_reliable_times.items(), key=lambda item: item[1], reverse=True)


for line_id, reliability in sorted_lines:
    print(
        f'地铁线路 {line_id} 的旅行时间可靠性为 {reliability:.2f}，优先级为 {sorted_lines.index((line_id, reliability)) + 1}')