# This is a dictionary representing a graph where each key is a node and the values are dictionaries 
# that represent the edges from that node to other nodes with their respective weights.
grap = {

'A': {'B': 5, 'C': 8, 'D': 9},

'B': {'A': 5, 'E': 15, 'F': 7},

'C': {'A': 8, 'G': 12, 'H': 10},

'D': {'A': 9, 'I': 11, 'J': 6},

'E': {'B': 15, 'K': 9, 'L': 13},

'F': {'B': 7, 'M': 8, 'N': 6},

'G': {'C': 12, 'O': 10, 'P': 5},

'H': {'C': 10, 'Q': 11, 'R': 7},

'I': {'D': 11, 'S': 14, 'T': 8},

'J': {'D': 6, 'U': 9, 'V': 12},

'K': {'E': 9},

'L': {'E': 13},

'M': {'F': 8},

'N': {'F': 6},

'O': {'G': 10},

'P': {'G': 5},

'Q': {'H': 11},

'R': {'H': 7},

'S': {'I': 14},

'T': {'I': 8},

'U': {'J': 9},

'V': {'J': 12}

}

# This function performs a Depth-First Search (DFS) on the graph.
def dfs(start, goal, graph=grap):
    # The stack stores tuples where the first element is a node and the second element is the path from the start node to the current node.
    stack = [(start, [start])]
    
    # While there are still nodes to visit in the stack
    while stack:
        # Pop a node and its path from the stack
        (vertex, path) = stack.pop()
        
        # For each neighbor of the current node that has not been visited yet
        for next in set(graph[vertex]) - set(path):
            # If the neighbor is the goal, yield the path to this node
            if next == goal:
                yield path + [next]
            # Otherwise, add the neighbor and the path to the stack to visit it later
            else:
                stack.append((next, path + [next]))
