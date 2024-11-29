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
        
        distanciasSrc1 = dijkstra(grafoNormal, src1)
        distanciasSrc2 = dijkstra(grafoNormal, src2) 
        distanciasDest = dijkstra(grafoReverso, dest)
        
        menorPeso = infinito
        
        for no in range(n):
            if any(distancia[no] == infinito for distancia in [distanciasSrc1, distanciasSrc2, distanciasDest]):
                continue  
            pesoTotal = distanciasSrc1[no] + distanciasSrc2[no] + distanciasDest[no]
            menorPeso = min(menorPeso, pesoTotal)

        return menorPeso if menorPeso != infinito else -1
                