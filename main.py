class Vertex:
    def __init__(self, data):
        self.data = data
        self.edges = {}

    def add_edge(self, vertex_data, weight):
        self.edges[vertex_data] = weight

    def retrieve_edges(self):
        return list(self.edges.keys())

class Graph:
    def __init__(self, directed):
        self.vertices = {}
        self.directed = directed

    def add_vertex(self, vertex):
        self.vertices[vertex.data] = vertex

    def add_edge(self, vertex_a, vertex_b, weight):
        self.vertices[vertex_a.data].add_edge(vertex_b.data, weight)
        if not self.directed:
            self.vertices[vertex_b.data].add_edge(vertex_a.data, weight)

    def find_vert(self, name):
            if self.vertices[name]:
                return self.vertices[name]
            else:
                return "city not found"

    def path_exists(self, vertex_a, vertex_b):
        to_visit = [vertex_a]
        visited = []
        while len(to_visit) > 0:
            current = to_visit.pop(0)
            visited.append(current)
            if current == vertex_b:
                return True
            else:
                vertices = self.vertices[current].edges.keys()
                to_visit += [vertex for vertex in vertices if vertex not in visited]
        return False


travels = Graph(directed=False)

destination_1 = Vertex("Kuwait")
destination_2 = Vertex("Dubai")
destination_3 = Vertex("Colombo")
destination_4 = Vertex("Male")
destination_5 = Vertex("Doha")
destination_6 = Vertex("Tokyo")
destination_7 = Vertex("Oslo")



travels.add_vertex(destination_1)
travels.add_vertex(destination_2)
travels.add_vertex(destination_3)
travels.add_vertex(destination_4)
travels.add_vertex(destination_5)
travels.add_vertex(destination_6)
travels.add_vertex(destination_7)

travels.add_edge(destination_1, destination_2, "2 hours, 120$")
travels.add_edge(destination_1, destination_2, "2 hours, 120$")
travels.add_edge(destination_1, destination_3, "4 hours, 200$")
travels.add_edge(destination_3, destination_4, "1 hour, 60$")
travels.add_edge(destination_2, destination_5, "1.5 hours, 100$")
travels.add_edge(destination_5, destination_6, "11 hours, 500$")
travels.add_edge(destination_2, destination_7, "6 hours, 300$")

for i in travels.vertices:
    print(f"{i} \t")
from_city = input("what city are you traveling from: ")
city = travels.find_vert(from_city)

list_of_cities = city.retrieve_edges()
print(list_of_cities)
to_city = input("What city do you want to travel to: ")
dest = travels.find_vert(to_city)
print(f"{dest.data} {city.edges[dest.data]}")