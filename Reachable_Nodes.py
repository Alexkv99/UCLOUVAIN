def reachable(adj_list, start_node):
    visited = set()
    def function(node):
        visited.add(node)
        for i in adj_list[node]:
            if i not in visited:
                function(i)
    function(start_node)
    return visited

reachable_nodes = reachable([[1, 3], [2], [0], [4], [3], []], 0)

print(reachable_nodes)
