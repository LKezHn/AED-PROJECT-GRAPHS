class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self,vertex_name):
        self.graph["%s" % (vertex_name)] = []

    def add_edge(self,vertex_origin,vertex_destination):
        dic = {vertex_destination : None}#Creo el diccionario donde estara la arista
        if not (vertex_destination in self.graph["%s" % (vertex_origin)]):
            self.graph["%s" % (vertex_origin)].append(dic)#Agrego ese diccionario como arista

    def connectVertices(self,x):

        graph,s = self.graph,{}

        for k,v in graph.items():
            if k == x:
                for i in v:
                    s[i]= None
            elif x in v:
                s[k]=None

        return list(s.keys()) 

    def convert(self,content):
        self.graph.clear()
        parent = "" 
        for row in content:
            if(row.find("\t") == -1):#Si no tiene tabulado
                row = row.replace(":","")#Quita los dos puntos y lo agrega
                self.add_vertex("%s"%row)
                parent = row #Es el padre donde se añadiran las aristas
            else:
                row = row.replace("\t","")#Quito el tab    
                row = row.replace(",","")#Quito las comas(por si tiene)
                self.add_edge("%s"%parent,"%s"%row)#Lo agrego como nodo arista del parent actual
        return self.graph # Retorno el grafo

    
    
"""
filename = "archivo.txt"
d = open(filename,"r")
content = d.read()
content = content.split("\n")
if(content[-1] == ""):
    content.pop()
g = Graph()
#g.convert(content)
#print(g.graph)
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_edge("A","C")
g.add_edge("A","B")
g.add_edge("A","E")
g.add_edge("B","E")
g.add_edge("C","A")
x = 'A'
print(list(g.dfs_paths("A","C")))
#print(g.graph)
#print("The graph is: %s" % (g.graph))
#print("The vertices connected to '%s' are: %s" % (x,g.connectVertices(x)))"""