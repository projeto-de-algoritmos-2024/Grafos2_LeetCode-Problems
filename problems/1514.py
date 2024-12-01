# You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

# Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

# If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.
class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        import heapq
        
        def cria_grafo(n, edges,succProb):
            grafo = {}
            for i in range(n):
                grafo[i] = []
                
            for i in range(len(edges)):
                u, v = edges[i]
                prob = succProb[i]
                grafo[u].append((v, prob))
                grafo[v].append((u, prob))  
            
            return grafo
        
        grafo = cria_grafo(n,edges,succProb)
        
        
        def dikstra(grafo, origem,destino):
            
            probabilidades = [0] * n
            
            probabilidades[origem] = 1.0
            
            heap = [(-1.0,origem)]
            
            while heap:
                
                probabilidade_atual, no_atual = heapq.heappop(heap)
                probabilidade_atual = -probabilidade_atual
                
                if no_atual==destino:
                    return float(probabilidade_atual)
                
                if probabilidade_atual < probabilidades[no_atual]:
                    continue
                
                for vizinho, peso in grafo[no_atual]:
    
                    probabilidade_vizinho = probabilidade_atual * peso
                    
                    if probabilidade_vizinho > probabilidades[vizinho]:
                        probabilidades[vizinho] = probabilidade_vizinho
                        heapq.heappush(heap, (-probabilidade_vizinho,vizinho))
                        #print(f"vizinho_prob= {vizinho}: {probabilidades[vizinho]}")

                    
            return float(0)
            
        dikstra(grafo,start_node,end_node)
        
