class Vertex:
    """Base class for a vertex in a generic, undirected adjacency list graph"""

    def __init__(self, n, v=0):
        self.name = n
        self.value = v
        self.adjacency_list = [] #list of adjacent vertex objects
    def __repr__(self):
        return "<vertex %s adjacency_list='%s'/>" % (self.name, list(map(str, self.adjacency_list)))
    def __str__(self):
        return self.name

class Graph:
    """Base class for a generic, undirected adjacency list graph"""

    def __init__(self, n):
        self.name = n
        self.verticies = []
        
    def __repr__(self):
        representation = "<graph %s/>\n" % (self.name)
        for vertex in self.verticies:
            representation += "\t" + repr(vertex) + "\n"
        representation += "</graph>\n"
        return representation
    
    def __str__(self):
        return self.name
    
    def adjacent(self, a, b):
        if b in a.adjacency_list:
            return True
        
    def neighbors(self, a):
        return a.adjacency_list

    def get_all_neighbors(self, a, max_depth=float("inf")):
        visited, distance, queue = {}, {a:0}, [a]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited[vertex] = distance[vertex]
                for neighbor in self.neighbors(vertex):
                    queue.append(neighbor)
                    neighbor_distance = distance[vertex] + 1
                    if (neighbor not in distance) or (distance[neighbor] > neighbor_distance):
                        distance[neighbor] = neighbor_distance

        for i in visited:
            if visited[i] <= max_depth:
                visited.pop(i)

        return visited
    
    def add_vertex(self, a):
        if a not in self.verticies:
            self.verticies.append(a)
        else:
            print("Vertex " + str(a) + " is already in graph " + str(self))
            
    def remove_vertex(self, a):
        if a in self.verticies:
            for vertex in self.verticies:
                if a in vertex.adjacency_list:
                    vertex.adjacency_list.remove(a)
            self.verticies.remove(a)
        else:
            print("Vertex " + str(a) + " is not in graph " + str(self))
            
    def add_edge(self, a, b):
        if a in self.verticies and b in self.verticies:
            if b not in a.adjacency_list: 
                a.adjacency_list.append(b)
                b.adjacency_list.append(a)
            else:
                print("An edge from " + str(a) + " to " + str(b) + " is already in graph " + str(self))
        else:
            print("Verticies " + str(a) + " or " + str(b) + " are not in graph " + str(self))
            
    def remove_edge(self, a, b):
        if a in self.verticies and b in self.verticies:
            a.adjacency_list.remove(b)
            b.adjacency_list.remove(a)
        else:
            print("Verticies " + str(a) + " or " + str(b) + " are not in graph " + str(self))

    def get_vertex(self, n):
        vertex = None
        for v in self.verticies:
            if v.name == n:
                vertex = v
                break
        return vertex

    def get_vertex_value(self, a):
        return a.value
    
    def set_vertex_value(self, a, v):
        a.value = v

if __name__ == "__main__":
    graph = Graph("g")
    vertex1 = Vertex("v1")
    vertex2 = Vertex("v2")
    vertex3 = Vertex("v3")
    graph.add_vertex(vertex1)
    graph.add_vertex(vertex2)
    graph.add_vertex(vertex3)
    graph.add_edge(vertex1, vertex2)
    graph.add_edge(vertex2, vertex3)
    graph.add_edge(vertex1, vertex3)
    print(repr(graph))
    print(graph.get_vertex_value(vertex1))
    print(list(map(str, graph.neighbors(vertex1))))
    print(graph.adjacent(vertex1, vertex2))
