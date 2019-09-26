class Graph:
    def __init__(self):
        self.graph = {}
        self.toRoad = {}

    def add_vertex(self,vertex_name):
        self.graph["%s" % (vertex_name)] = []
        self.toRoad["%s"%vertex_name] = set()

    def add_edge(self,vertex_origin,vertex_destination):
        dic = {vertex_destination : None}#Creo el diccionario donde estara la arista
        if not (vertex_destination in self.graph["%s" % (vertex_origin)]):
            self.graph["%s" % (vertex_origin)].append(dic)#Agrego ese diccionario como arista
            self.toRoad["%s"%vertex_origin].add(vertex_destination)
        return dic

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
        edge_name = ""
        edge_parent = None 
        features_edges = {}
        for row in content:
            if(row.find("\t") == -1):#Si no tiene tabulado
                row = row.replace(":","")#Quita los dos puntos y lo agrega
                self.add_vertex("%s"%row)
                parent = row #Es el padre donde se añadiran las aristas
            else:
                if(row.count("\t") == 1):
                    features_edges.clear()#Limpio el diccionario de caracteristicas para que no las agregue en otro vertice
                    row = row.replace("\t","")#Quito el tab    
                    row = row.replace(":","")#Quito las comas(por si tiene)
                    edge_name = row #Guardo el nombre del vertice arista
                    edge_parent = self.add_edge("%s"%parent,"%s"%row)#Lo agrego como nodo arista del parent actual
                else:
                    row = row.replace("\t","")
                    row = row.split(":")
                    edge_parent["%s"%edge_name] = {}#Convierto el nodo arista en diccionario
                    features_edges["%s"%row[0]] = "%s"%row[1] #Guardo la caracteristica actual
                    edge_parent["%s"%edge_name].update(features_edges)#Agrego el diccionario de caracteristicas al vertice arista
        return self.graph # Retorno el grafo

    
