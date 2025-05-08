from collections import defaultdict

graph = defaultdict(list)

num_edges = int(input("Enter the number of edges: "))
print("Enter edges in the format 'A B' (without quotes):")

for _ in range(num_edges):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)  

def bfs(graph, start_node, goal_node):
    visited = []
    queue = []
    visited.append(start_node)
    queue.append(start_node)
    print("\nBFS Traversal:")
    while queue:
        m = queue.pop(0)
        print(m)
        if m == goal_node:
            print("Node is Found !!!")
            break
        else:
            for n in graph[m]:
                if n not in visited:
                    visited.append(n)
                    queue.append(n)

def dfs(graph, start_node, goal_node):
    visited = []
    stack = []
    print("\nDFS Traversal:")
    stack.append(start_node)
    visited.append(start_node)
    while stack:
        node = stack.pop()
        print("Node:", node)
        if node == goal_node:
            print("Goal node found!")
            return
        for n in graph[node]:
            if n not in visited:
                visited.append(n)
                stack.append(n)

start = input("\nEnter the start node: ")
goal = input("Enter the goal node: ")

bfs(graph, start, goal)
dfs(graph, start, goal)