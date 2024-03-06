from src.detection.find_community import find_community
from src.detection.modularity import modularity

def detect_communities(graph):
    best_partition = []
    best_modularity = -1

    for _ in range(len(graph)):
        communities = find_community(graph)
        current_modularity = sum(modularity(graph, community) for community in communities)

        if current_modularity > best_modularity:
            best_partition = communities
            best_modularity = current_modularity

    return best_partition