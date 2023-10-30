# undirected graph
class Graph:
    def __init__(self) -> None:
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
        
    def remove_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            # remove the edge also
            for v in self.graph:
                self.graph[v] = [i for i in self.graph[v] if i != vertex]

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1] = [i for i in self.graph[vertex1] if i != vertex2]
            self.graph[vertex2] = [i for i in self.graph[vertex2] if i != vertex1]

    def get_vertex(self):
        return list(self.graph.keys())
    
    def get_edges(self):
        edges = []
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                if (vertex, neighbor) not in edges and (vertex, neighbor) not in edges:
                    edges.append((vertex, neighbor))
                    
        return edges
    
    
    
    