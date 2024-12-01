# There is a country of n cities numbered from 0 to n - 1 where all the cities are connected by bi-directional roads. The roads are represented as a 2D integer array edges where edges[i] = [xi, yi, timei] denotes a road between cities xi and yi that takes timei minutes to travel. There may be multiple roads of differing travel times connecting the same two cities, but no road connects a city to itself.

# Each time you pass through a city, you must pay a passing fee. This is represented as a 0-indexed integer array passingFees of length n where passingFees[j] is the amount of dollars you must pay when you pass through city j.

# In the beginning, you are at city 0 and want to reach city n - 1 in maxTime minutes or less. The cost of your journey is the summation of passing fees for each city that you passed through at some moment of your journey (including the source and destination cities).

# Given maxTime, edges, and passingFees, return the minimum cost to complete your journey, or -1 if you cannot complete it within maxTime minutes.
class Solution:
    def minCost(maxTime: int, edges: list[list[int]], passingFees: list[int]) -> int:
        import heapq
        import pprint
        
        def cria_grafo(n, edges):
            grafo = {}
            for i in range(n):
                grafo[i] = []
                
            for i in range(n):
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
            print(tempos)
            
            if tempo_atual > maxTime:
                
                continue

            if no_atual == n-1:
                
                return custo_atual

            for vizinho, tempo in grafo[no_atual]:
                if tempos[vizinho] == 1001 or vizinho == n-1:
                    tempo_vizinho = tempo_atual + tempo
                    custo_vizinho = custo_atual + passingFees[vizinho]
                    
                    if tempo_vizinho < tempos[vizinho]:
                        
                        tempos[vizinho] = tempo_vizinho
                        heapq.heappush(heap,(custo_vizinho,vizinho,tempo_vizinho))
        
        return -1 
     
maxTime = 29
edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]]
passingFees = [5,1,2,20,20,3]

print(Solution.minCost(maxTime=maxTime,edges=edges,passingFees=passingFees))