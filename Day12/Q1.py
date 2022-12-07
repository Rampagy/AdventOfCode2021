import helpers

if __name__=='__main__':
    graph = {}

    with open('input.txt', 'r') as f:
        for line in f:
            node_start, node_end = helpers.ParseLine('{}-{}\n', line)

            if node_start in graph:
                if node_end not in graph[node_start]:
                    graph[node_start] += [node_end]
            else:
                graph[node_start] = [node_end]

            # now add the end back to the start paths
            if node_end in graph:
                if node_start not in graph[node_end]:
                    graph[node_end] += [node_start]
            else:
                graph[node_end] = [node_start]

    paths = helpers.BFS(graph, 'start', 'end')
    print(len(paths)) # 3410