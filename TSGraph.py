from Graph import *

class Country(Vertex):

    def __init__(self, n, r, sr, st, bg):
        Vertex.__init__(self, n)
        
        self.region = r
        self.sub_region = sr
        self.stability = st
        self.battle_ground = bg

    def __repr__(self):
            return "<Country %s adjacency_list='%s'/>" % (self.name, list(map(str, self.adjacency_list)))

class Superpower(Vertex):
    
    def __init__(self, n):
        Vertex.__init__(self, n)

    def __repr__(self):
        return "<Superpower %s adjacency_list='%s'/>" % (self.name, list(map(str, self.adjacency_list)))

class Map(Graph):

    def __init__(self, n):
        Graph.__init__(self,n)
        self.__create_countries()
        self.__create_superpowers()
        self.__create_borders()

    def __create_countries(self):
        with open("countries/country_list.csv", "r") as handle:
            header = handle.readline()
            lines = handle.read().splitlines()
        
        for line in lines:
            country = Country(*line.split(","))
            self.add_vertex(country)
            
    def __create_superpowers(self):
        with open("superpowers/superpower_list.csv", "r") as handle:
            header = handle.readline()
            lines = handle.read().splitlines()
        
        for line in lines:
            superpower = Superpower(*line.split(","))
            self.add_vertex(superpower)
    
    def __create_borders(self):
        for file in ["countries/border_list.csv", "superpowers/border_list.csv"]:
            with open(file, "r") as handle:
                header = handle.readline()
                lines = handle.read().splitlines()
            
            for line in lines:
                neighbors = line.split(",")
                country = neighbors.pop(0)
                for neighbor in neighbors:
                    if neighbor == "": continue
                    self.add_edge(self.get_vertex(country), self.get_vertex(neighbor))

    def get_all_neighbors(self, a, max_depth=float("inf")):
        visited, distance, queue = {}, {a:0}, [a]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited[vertex] = distance[vertex]
                for neighbor in self.neighbors(vertex):
                    #skip superpowers because you can't place influence in them
                    if isinstance(neighbor, Superpower): continue
                    queue.append(neighbor)
                    neighbor_distance = distance[vertex] + 1
                    if (neighbor not in distance) or (distance[neighbor] > neighbor_distance):
                        distance[neighbor] = neighbor_distance

        return dict((k,v) for k, v in visited.items() if v <= max_depth)

    def calculate_access(self):
        return False

if __name__ == "__main__":
    board = Map("Twilight Struggle")
    
    #print the board
    print(repr(board))
    
    country = "Sudan"
    max_distance = 4
    #print the neighbors of country
    print(list(map(str, board.neighbors(board.get_vertex(country)))))
    #get the distance of each other country from country within max_distance spaces
    neighbors = board.get_all_neighbors(board.get_vertex(country), max_distance)
    for neighbor in neighbors:
        print("%s is %d spaces from %s" % (str(neighbor), neighbors[neighbor], country))












