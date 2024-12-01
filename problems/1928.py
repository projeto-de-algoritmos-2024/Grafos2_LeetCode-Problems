class Solution:
    def minCost(self, maxTime: int, edges: list[list[int]], passingFees: list[int]) -> int:
        import heapq
        import pprint
        
        def cria_grafo(n, edges):
            grafo = {}
            for i in range(n):
                grafo[i] = []
                
            for i in range(len(edges)):
                u = edges[i][0]
                v = edges[i][1]
                peso = edges[i][2]
                grafo[u].append((v, peso))
                grafo[v].append((u, peso))
                
            
            return grafo
        
        n = len(passingFees)
        
        grafo = cria_grafo(n, edges)
        
        tempos = [1001] * n
        tempos[0] = 0
        heap = [(passingFees[0], 0, 0)] #(custo, no, tempo)
        
        while heap:
            
            custo_atual, no_atual, tempo_atual = heapq.heappop(heap)
            
            if tempo_atual > maxTime:
                
                continue

            if no_atual == n-1:
                
                return custo_atual

            for vizinho, tempo in grafo[no_atual]:
                
                tempo_vizinho = tempo_atual + tempo
                custo_vizinho = custo_atual + passingFees[vizinho]
                
                if tempo_vizinho <= maxTime and tempo_vizinho < tempos[vizinho]:
                    
                    tempos[vizinho] = tempo_vizinho
                    heapq.heappush(heap,(custo_vizinho,vizinho,tempo_vizinho))
        
        return -1 
            
     