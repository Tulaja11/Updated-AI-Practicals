class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

# Kruskal's Algorithm 
def kruskal(vertices, edges):
    mst = []
    total_weight = 0
    disjoint_set = DisjointSet(vertices)

    edges.sort(key=lambda x: x[2])

    for u, v, weight in edges:
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst.append((u, v, weight))
            total_weight += weight
    
    return mst, total_weight

def main():
    vertices = int(input("Enter the number of vertices: "))
    edges_count = int(input("Enter the number of edges: "))
    
    edges = []
    print("Enter each edge as: vertex1 vertex2 weight (Vertices must be between 0 and", vertices - 1, ")")
    
    for i in range(edges_count):
        try:
            u, v, weight = map(int, input(f"Edge {i+1}: ").split())
            if u >= vertices or v >= vertices or u < 0 or v < 0:
                print(f" Invalid vertex! Please enter vertices between 0 and {vertices - 1}.")
                return
            edges.append((u, v, weight))
        except ValueError:
            print(" Invalid input! Please enter exactly three integers: u v weight.")
            return

    mst, total_weight = kruskal(vertices, edges)

    print("\n Edges in the Minimum Spanning Tree (MST):")
    for u, v, weight in mst:
        print(f"Edge ({u}, {v}) with weight {weight}")
    print(f" Total weight of the MST: {total_weight}")

if __name__ == "__main__":
    main()
