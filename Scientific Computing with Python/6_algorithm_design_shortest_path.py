# Algorithms are step-by-step procedures that developers use to perform calculations and
# solve computational problems.

# In this project, you'll learn how to use functions, loops, conditional statements, and
# dictionary comprehensions to implement a Shortest Path algorithm.

# Define a graph
my_graph = {
    "A": [("B", 5), ("C", 3), ("E", 11)],
    "B": [("A", 5), ("C", 1), ("F", 2)],
    "C": [("A", 3), ("B", 1), ("D", 1), ("E", 5)],
    "D": [("C", 1), ("E", 9), ("F", 3)],
    "E": [("A", 11), ("C", 5), ("D", 9)],
    "F": [("B", 2), ("D", 3)],
}


# Define a function to find the shortest path
def shortest_path(graph, start, target=""):
    # Initialize the variables
    unvisited = list(graph)  # unvisited nodes
    distances = {node: 0 if node == start else float("inf") for node in graph}  # distances from start
    paths = {node: [] for node in graph}  # paths from start
    paths[start].append(start)  # append start to paths as we start from here

    # Find the shortest path
    while unvisited:
        # get the node with the smallest distance
        current = min(unvisited, key=distances.get)
        # for each neighbor of current node
        for node, distance in graph[current]:
            # if the total distance is smaller than the neighbor's distance
            if distance + distances[current] < distances[node]:
                # update the neighbor's distance
                distances[node] = distance + distances[current]
                # update the neighbor's path with the current node
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                # if the neighbor is not in the path, extend the neighbor's path with the current node
                else:
                    paths[node].extend(paths[current])
                # append the neighbor to the path
                paths[node].append(node)
        # remove the current node from the unvisited nodes
        unvisited.remove(current)

    # Print the shortest path
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        # Ignore the start node
        if node == start:
            continue
        # Print the shortest path from the start node to the target node and the distance
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')

    return distances, paths


# Call the function to find the shortest path from A to F. Run only if this file is executed.
if __name__ == "__main__":
    _, _ = shortest_path(my_graph, "A", "F")
