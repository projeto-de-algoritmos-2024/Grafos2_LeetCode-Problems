# There is a country of n cities numbered from 0 to n - 1 where all the cities are connected by bi-directional roads. The roads are represented as a 2D integer array edges where edges[i] = [xi, yi, timei] denotes a road between cities xi and yi that takes timei minutes to travel. There may be multiple roads of differing travel times connecting the same two cities, but no road connects a city to itself.

# Each time you pass through a city, you must pay a passing fee. This is represented as a 0-indexed integer array passingFees of length n where passingFees[j] is the amount of dollars you must pay when you pass through city j.

# In the beginning, you are at city 0 and want to reach city n - 1 in maxTime minutes or less. The cost of your journey is the summation of passing fees for each city that you passed through at some moment of your journey (including the source and destination cities).

# Given maxTime, edges, and passingFees, return the minimum cost to complete your journey, or -1 if you cannot complete it within maxTime minutes.

def minCost(maxTime: int, edges: list[list[int]], passingFees: list[int]) -> int:
    import pprint
    num_nodes = len(passingFees)
        
    grafo = []
    for i in range(num_nodes):
        grafo.append([])
        
    for e in edges:
        grafo[e[0]].append((e[1], e[2]))
        
        
    pprint.pprint(grafo)

maxTime = 30
edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]]
passingFees = [5,1,2,20,20,3]

minCost(maxTime=maxTime,edges=edges,passingFees=passingFees)

# import pprint
#     class MinHeap:
#         def __init__(self):
#             self.heap = []

#         def push(self, val):
#             # Adiciona o elemento no final
#             self.heap.append(val)
#             # Reorganiza a heap para manter a propriedade mínima
#             self._heapify_up(len(self.heap) - 1)

#         def pop(self):
#             if not self.heap:
#                 raise IndexError("Pop from empty heap")
#             # Troca o primeiro e último elemento
#             self._swap(0, len(self.heap) - 1)
#             # Remove o menor elemento (raiz)
#             min_val = self.heap.pop()
#             # Reorganiza a heap
#             self._heapify_down(0)
#             return min_val

#         def peek(self):
#             if not self.heap:
#                 raise IndexError("Peek from empty heap")
#             return self.heap[0]

#         def _heapify_up(self, index):
#             parent = (index - 1) // 2
#             # Enquanto não estiver na raiz e o elemento for menor que o pai
#             if index > 0 and self.heap[index] < self.heap[parent]:
#                 self._swap(index, parent)
#                 self._heapify_up(parent)

#         def _heapify_down(self, index):
#             smallest = index
#             left = 2 * index + 1
#             right = 2 * index + 2
#             # Verifica o filho esquerdo
#             if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
#                 smallest = left
#             # Verifica o filho direito
#             if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
#                 smallest = right
#             # Se o menor não for o nó atual, troca e continua descendo
#             if smallest != index:
#                 self._swap(index, smallest)
#                 self._heapify_down(smallest)

#         def _swap(self, i, j):
#             self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
#     def constroi_grafo(num_nodes: int, edges: list[list[int]]) -> dict:
    
#         grafo = {}
        
#         for i in range(num_nodes):
#             grafo[i]= {'vizinhos':[],'pesos':[],'pedagio':-1}
#         return grafo
        
#     grafo = constroi_grafo(len(passingFees),edges)
    
#     heap = MinHeap()
    
#     for i in edges:
#         grafo[i[0]]['vizinhos'].append(i[1])
#         grafo[i[0]]['pesos'].append(i[2])
#         grafo[i[0]]['pedagio']=passingFees[i[0]]
#     grafo[len(passingFees)-1]['pedagio']=passingFees[-1]   
    
        
#     pprint.pprint(grafo)