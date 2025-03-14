# Routing Protocol Simulator

This project implements a **Routing Protocol Simulator** in Python, allowing users to simulate and compare two fundamental routing algorithms:
- **Link-State Routing (Dijkstra's Algorithm)**
- **Distance-Vector Routing (Bellman-Ford Algorithm)**

The simulator randomly generates a **graph topology**, representing a network with nodes and weighted edges (links). Users can specify network parameters and compute the shortest path between two nodes.

## Quickstart Guide

### Running the Simulator
1. Copy all the contents from this repository.
2. Open a terminal and navigate to the folder containing `route.py`.
3. Run the program using:
   ```bash
   python route.py
   ```
4. You will be prompted to:
   - Choose a routing protocol: **(1) Link-State (Dijkstra) or (2) Distance-Vector (Bellman-Ford)**.
   - Define the number of network nodes (`N`).
   - Set the maximum number of connections (`M`) for each node.

### Computing a Path
- The program generates a **random weighted graph** based on the user input.
- Users select a **source node** and a **destination node**.
- The chosen algorithm computes and displays the **shortest path** and **total path weight**.

## Core Concepts
- **Link-State Routing (Dijkstra's Algorithm)**:
  - Computes the shortest path using a priority queue.
  - Guarantees the shortest path to all nodes.
- **Distance-Vector Routing (Bellman-Ford Algorithm)**:
  - Uses iterative updates to estimate shortest paths.
  - Handles **negative weights** (but not negative cycles).

## Preview of Simulation Output

### **Example Network Graph (Adjacency List)**
```bash
Generated graph (Adjacency list with weights):
Node 0: [(1, 5), (2, 8)]
Node 1: [(0, 5), (3, 2)]
Node 2: [(0, 8), (3, 6)]
Node 3: [(1, 2), (2, 6), (4, 3)]
...
```

### **Example Path Calculation**
```bash
Enter initial node (0 to 4): 0
Enter end node (0 to 4): 3

The minimum path from node 0 to node 3 is: 0 -> 1 -> 3
The total weight is: 7
```

## Notes:
- Users can **regenerate the graph** or **calculate new paths** within the same network.
- The simulator can be extended to **real-world networking applications**.
- The number of **nodes and connections** can be adjusted to create different network topologies.

## Future Enhancements
- Support for **real-time network traffic updates**.
- Implementation of **Hybrid Routing Algorithms**.
- Integration with **graph visualization tools** for better path representation.
