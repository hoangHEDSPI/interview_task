def isCycle(v, visited, recStack, connections):
    visited[v] = True
    recStack[v] = True
    for v_neighbour in connections[v]:
        if visited[v_neighbour] == False:
            if isCycle(v_neighbour, visited, recStack, connections) == True:
                return True
        elif recStack[v_neighbour] == True:
            return True
    recStack[v] = False
    return False

def hasDeadlock(connections):
    visited = [False]*len(connections)
    recStack = [False]*len(connections)
    for node in range(len(connections)):
        if visited[node] == False:
            if isCycle(node, visited, recStack, connections) == True:
                return True
    return False

connections = [[1, 2, 3], [2, 3], [3], []]
print hasDeadlock(connections)