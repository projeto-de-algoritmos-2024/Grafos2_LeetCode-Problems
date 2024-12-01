
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
            
        return dikstra(grafo,start_node,end_node)
        
