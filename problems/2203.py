from typing import List
from collections import defaultdict
import heapq

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        
        grafoNormal = defaultdict(list)
        grafoReverso = defaultdict(list)

        for origem, destino, peso in edges:
            grafoNormal[origem].append((destino, peso))
            grafoReverso[destino].append((origem, peso))
            
        infinito = float('inf')
        
        def dijkstra(grafo, pontoPartida):
            distancias = [infinito] * n 
            distancias[pontoPartida] = 0 
            filaPrioridade = [(0, pontoPartida)] 

            while filaPrioridade: 
                distanciaAtual, no = heapq.heappop(filaPrioridade) 
                if distanciaAtual > distancias[no]: 
                    continue
                for vizinho, peso in grafo[no]: 
                    novaDistancia = distancias[no] + peso 
                    if distancias[vizinho] > novaDistancia: 
                        distancias[vizinho] = novaDistancia
                        heapq.heappush(filaPrioridade, (novaDistancia, vizinho))
            return distancias
        