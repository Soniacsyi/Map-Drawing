import networkx as nx
from collections import defaultdict


G = nx.DiGraph()


edges = [
    (1, 2, 1),
    (2, 3, 1),
    (3, 4, 1),
    (4, 5, 1),
    (5, 6, 1),
    (7, 8, 2),
    (8, 9, 2),
    (9, 3, 2),
    (3, 10, 2),
    (10, 5, 2),
    (5, 11, 2),
    (11, 12, 2),
    (12, 13, 2),
    (8, 12, 3),
    (12, 14, 3),
    (5, 15, 4)
]


line_stations = defaultdict(list)


for ori, des, line in edges:
    G.add_edge(ori, des)
    line_stations[line].append(ori)
    line_stations[line].append(des)


for line in line_stations:
    line_stations[line] = list(set(line_stations[line]))


node_bc = nx.betweenness_centrality(G, normalized=True)


line_bc = {}
for line, stations in line_stations.items():
    line_sum_bc = 0
    for station in stations:
        line_sum_bc += node_bc[station]


    line_bc[line] = line_sum_bc / len(stations)


for line, avg_bc in line_bc.items():
    print(f"line {line}: AVGBC = {avg_bc}")