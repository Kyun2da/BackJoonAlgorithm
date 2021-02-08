candidates = []


def dfs(start, graph, visited, cnt, route):
    global candidates
    if cnt == len(graph):
        candidates.append(route.split(" "))
    else:
        for i in range(len(graph)):
            if visited[i] == 0 and graph[i][0] == start:
                go = []
                for j in range(len(visited)):
                    go.append(visited[j])
                go[i] = 1
                dfs(graph[i][1], graph, go, cnt + 1, route + " " + graph[i][1])


def solution(tickets):
    tickets.sort()
    visited = [0] * len(tickets)
    dfs("ICN", tickets, visited, 0, "ICN")
    return candidates[0]
