import random
import heapq

def get_user_input():
    protocol_choice = input("Select routing protocol: (1) Link-State or (2) Distance-Vector: ").strip()
    while protocol_choice not in ['1', '2']:
        protocol_choice = input("Please enter '1' for Link-State or '2' for Distance-Vector: ").strip()
    protocol = 'link-state' if protocol_choice == '1' else 'distance-vector'
    
    N = input("Enter the number of nodes (N): ").strip()
    while not N.isdigit() or int(N) < 2:
        N = input("Please enter a valid number of nodes (N >= 2): ").strip()
    N = int(N)
    
    M_list = []
    for i in range(N):
        M = input(f"Enter max connections for node {i} (less than {N}): ").strip()
        while not M.isdigit() or int(M) < 1 or int(M) >= N:
            M = input(f"Please enter a valid max connections for node {i} (1 <= M < {N}): ").strip()
        M_list.append(int(M))
    
    return protocol, N, M_list

def build_random_graph(N, M_list):
    graph = {i: [] for i in range(N)}
    edges = set()

    for i in range(N - 1):
        weight = random.randint(1, 10)
        graph[i].append((i + 1, weight))
        graph[i + 1].append((i, weight))
        edges.add((min(i, i + 1), max(i, i + 1)))
    
    for i in range(N):
        num_existing_connections = len(graph[i])
        max_connections = M_list[i]
        max_additional_connections = max(0, max_connections - num_existing_connections)
        num_additional_connections = random.randint(0, max_additional_connections) if max_additional_connections > 0 else 0
        possible_nodes = [node for node in range(N) if node != i]
        random.shuffle(possible_nodes)
        added_connections = 0
        for node in possible_nodes:
            if len(graph[i]) >= max_connections:
                break
            if len(graph[node]) >= M_list[node]:
                continue
            edge = (min(i, node), max(i, node))
            if edge not in edges:
                weight = random.randint(1, 10)
                graph[i].append((node, weight))
                graph[node].append((i, weight))
                edges.add(edge)
                added_connections += 1
                if added_connections >= num_additional_connections:
                    break
    return graph

def get_init_and_end_nodes(N):
    
    init_node = input(f"Enter initial node (0 to {N-1}): ").strip()
    while not init_node.isdigit() or int(init_node) < 0 or int(init_node) >= N:
        init_node = input(f"Please enter a valid initial node (0 to {N-1}): ").strip()
    init_node = int(init_node)
    
    end_node = input(f"Enter end node (0 to {N-1}): ").strip()
    while not end_node.isdigit() or int(end_node) < 0 or int(end_node) >= N:
        end_node = input(f"Please enter a valid end node (0 to {N-1}): ").strip()
    end_node = int(end_node)
    
    return init_node, end_node

def dijkstra(graph, start_node, end_node):
    distances = {node: float('inf') for node in graph}
    previous_nodes = {node: None for node in graph}
    distances[start_node] = 0
    heap = [(0, start_node)]
    while heap:
        current_distance, current_node = heapq.heappop(heap)
        if current_node == end_node:
            break
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(heap, (distance, neighbor))
    
    path = []
    node = end_node
    if distances[end_node] == float('inf'):
        return [], float('inf')
    while node is not None:
        path.insert(0, node)
        node = previous_nodes[node]
    return path, distances[end_node]

def bellman_ford(graph, start_node, end_node):
    distances = {node: float('inf') for node in graph}
    previous_nodes = {node: None for node in graph}
    distances[start_node] = 0
    N = len(graph)
    for i in range(N - 1):
        updated = False
        for u in graph:
            for v, weight in graph[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    previous_nodes[v] = u
                    updated = True
        if not updated:
            break
    
    path = []
    node = end_node
    if distances[end_node] == float('inf'):
        return [], float('inf')
    while node is not None:
        path.insert(0, node)
        node = previous_nodes[node]
    return path, distances[end_node]

def main():
    protocol, N, M_list = get_user_input()
    graph = build_random_graph(N, M_list)
    
    while True:
        print("\nGenerated graph (Adjacency list with weights):")
        for node in graph:
            print(f"Node {node}: {graph[node]}")
        
        init_node, end_node = get_init_and_end_nodes(N)
        if protocol == 'link-state':
            path, weight = dijkstra(graph, init_node, end_node)
        elif protocol == 'distance-vector':
            path, weight = bellman_ford(graph, init_node, end_node)
        
        if not path:
            print(f"\nNo path exists from node {init_node} to node {end_node}.")
        else:
            print(f"\nThe minimum path from node {init_node} to node {end_node} is: {' -> '.join(map(str, path))}")
            print(f"The total weight is: {weight}")
        
        
        next_action = input("\nPress 'q' to quit or any other key to calculate a new path: ").strip().lower()
        if next_action == 'q':
            print("Exiting the program.")
            break
        else:
            regenerate = input("Do you want to generate a new graph? (y/n): ").strip().lower()
            if regenerate == 'y':
                protocol, N, M_list = get_user_input()
                graph = build_random_graph(N, M_list)

if __name__ == "__main__":
    main()
