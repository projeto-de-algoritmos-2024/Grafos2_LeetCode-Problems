# You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

# Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

# If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

def maxProbability(n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
    import heapq
     
    def cria_grafo(n, edges,succProb):
        grafo = {}
        for i in range(n):
            grafo[i] = []
            
        for e in edges:
            grafo[e[0]].append((e[1],succProb[edges.index(e)]))
            grafo[e[1]].append((e[0],succProb[edges.index(e)]))
            
        return grafo
    
    grafo = cria_grafo(n,edges,succProb)
    
    
    def dikstra(grafo, origem):
        
        probabilidades = {}
        for no in grafo:
            probabilidades[no] = float(0)
        
        probabilidades[origem] = 0
        
        heap = [(0,origem)]
        
        while heap:
            
            probabilidade_atual, no_atual = heapq.heappop(heap)
            
            if probabilidade_atual < probabilidades[no_atual]:
                continue
            
            for vizinho, peso in grafo[no_atual]:
 
                if no_atual == origem:
                    probabilidade_vizinho = peso
                    
                else:
                    probabilidade_vizinho = probabilidade_atual * peso
                
                if probabilidade_vizinho > probabilidades[vizinho]:
                    probabilidades[vizinho] = probabilidade_vizinho
                    heapq.heappush(heap, (probabilidade_vizinho,vizinho))

                
        return probabilidades
         
    probabilidades = dikstra(grafo,start_node)
    
    print(probabilidades[end_node])
        
n = 3

edges = [[0,1]]

succProb = [0.5]

start_node = 0

end_node = 2

maxProbability(n,edges,succProb,start_node,end_node)