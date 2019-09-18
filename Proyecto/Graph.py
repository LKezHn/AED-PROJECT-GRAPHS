class Graph:

    def __init__(self):
        self.graph = {}

    def add_vertex(self,vertex_name):
        self.graph["%s" % (vertex_name)] = []

    def add_edge(self,vertex_origin,vertex_destination):
        if not (vertex_destination in self.graph["%s" % (vertex_origin)]):
            self.graph["%s" % (vertex_origin)].append(vertex_destination)

    def connectVertices(self,x):

        graph,s = self.graph,{}

        for k,v in graph.items():
            if k == x:
                for i in v:
                    s[i]= None
            elif x in v:
                s[k]=None

        return s.keys() 


g = Graph()

g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_edge("A","C")
g.add_edge("A","B")
g.add_edge("A","E")
g.add_edge("B","E")

x = 'A'

print("The graph is: %s" % (g.graph))
print("The vertices connected to '%s' are: %s" % (x,g.connectVertices(x)))
