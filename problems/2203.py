from typing import List
from collections import defaultdict

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        
        grafoNormal = defaultdict(list)
        grafoReverso = defaultdict(list)

        for origem, destino, peso in edges:
            grafoNormal[origem].append((destino, peso))
            grafoReverso[destino].append((origem, peso))
        