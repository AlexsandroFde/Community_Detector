def modularity(graph, community):
    total_edges = sum(len(neighbors) for neighbors in graph.values()) // 2
    intra_community_edges = sum(len([n for n in neighbors if n in community]) for neighbors in graph.values()) // 2
    community_degree = sum(len(neighbors) for vertex, neighbors in graph.items() if vertex in community)
    expected_edges = (community_degree / (2 * total_edges)) ** 2
    return intra_community_edges / total_edges - expected_edges