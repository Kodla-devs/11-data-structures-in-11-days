V = 4
mat = [[0] * V for _ in range(V)]

def add_edge(mat, i, j):
    mat[i][j] = 1
    mat[j][i] = 1

add_edge(mat, 0, 1)
add_edge(mat, 0, 2)
add_edge(mat, 1, 2)
add_edge(mat, 2, 3)

for row in mat:
    print(" ".join(map(str, row)))


adj = [[] for _ in range(V)]

def added_edge_list(adj, i, j):
    adj[i].append(j)
    adj[j].append(i)

added_edge_list(adj, 0, 1)
added_edge_list(adj, 0, 2)
added_edge_list(adj, 1, 2)
added_edge_list(adj, 2, 3)

print("\n\n")

for i in range(len(adj)):
    print(f"{i}: ", end="")
    for j in adj[i]:
        print(j, end=" ")
    print()
    