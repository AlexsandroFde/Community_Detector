def find_community(graph):
    communities = []
    remaining_nodes = set(graph.keys())

    while remaining_nodes:
        node = remaining_nodes.pop()
        community = [node]
        queue = [node]

        while queue:
            current_node = queue.pop(0)
            neighbors = graph[current_node]

            for neighbor in neighbors:
                if neighbor not in community and neighbor in remaining_nodes:
                    community.append(neighbor)
                    remaining_nodes.remove(neighbor)
                    queue.append(neighbor)

        communities.append(community)

    return communities