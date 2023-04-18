class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graphDict = {}
        for start, end in self.edges:
            if start in self.graphDict:
                self.graphDict[start].append(end)
            else:
                self.graphDict[start] = [end]
        print(self.graphDict)

    def get_paths(self, start, end, path=[]):

        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graphDict:
            return []

        paths = []

        for node in self.graphDict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path+[start]
        if start == end:
            return path
        if start not in self.graphDict:
            return None

        shortest_path = None
        for node in self.graphDict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path


if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]

    routed_graph = Graph(routes)
    start = "Mumbai"
    end = "New York"

    print(f"Path between {start} and {end}: ", routed_graph.get_paths(start, end))
    print(f"Shortest Path between {start} and {end}: ", routed_graph.get_shortest_path(start, end))
