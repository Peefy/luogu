from collections import defaultdict

def read_data():
    lines = input().split()
    return int(lines[0]), int(lines[1])

# Double edge graph
graph = defaultdict(list)
n, m = read_data()
for i in range(m):
    u, v = read_data()
    graph[u].append(v)
    graph[v].append(u)

# Visited array and color array
visited = [0] * (n + 1)
color = [0] * (n + 1)
# Color count
red = black = 0

# DFS
def dfs(k, go):
    global red
    global black
    # Adjacent points have different colors
    color[k] = go % 2
    if color[k]:
        black += 1
    else:
        red += 1
    visited[k] = 1
    e = graph.get(k) or []
    for v in e:
        if visited[v]:
            # Color conflict
            if color[v] == color[k]:
                return False
        elif not dfs(v, go + 1):
            return False
    return True

ans = 0
impossible = False

# Note including sub graph
for k in graph:
    if not visited[k]:
        red = black = 0
        if not dfs(k, 0):
            impossible = True
            break
        ans += min(red, black)

if impossible:
    print("Impossible")
else:
    print(ans)
