class Graph:
    def __init__(self):
        self.size = 0
        self.adjacency_list = {}

    def add_vertex(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []
            self.size += 1
        return

    def add_edge(self, node1, node2):
        if node1 not in self.adjacency_list:
            print(f"vertex {node1} not in graph!")
            return
        if node2 not in self.adjacency_list:
            print(f"vertex {node2} not in graph!")
            return
        vertex1 = self.adjacency_list[node1]
        vertex2 = self.adjacency_list[node2]

        if node1 not in vertex2:
            vertex2.append(node1)
        if node2 not in vertex1:
            vertex1.append(node2)

    def show_connections(self):
        s = ""
        for key in self.adjacency_list.keys():
            s += key
            s += " --> "
            adjacency_list = self.adjacency_list[key]
            s += str(adjacency_list)
            s += "\n"
        s += f"number of nodes: {self.size}"
        print(s)


def main():
    graph = Graph()
    graph.add_vertex("0")
    graph.add_vertex("1")
    graph.add_vertex("2")
    graph.add_vertex("3")
    graph.add_vertex("4")
    graph.add_vertex("5")
    graph.add_vertex("6")

    graph.add_edge("0", "1")
    graph.add_edge("0", "2")
    graph.add_edge("1", "2")
    graph.add_edge("1", "3")
    graph.add_edge("2", "4")
    graph.add_edge("3", "4")
    graph.add_edge("4", "5")
    graph.add_edge("5", "6")

    graph.show_connections()


if __name__ == "__main__":
    main()
