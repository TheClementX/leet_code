from typing import * 
from collections import * 

def solution(startGene: str, endGene: str, bank: list[str]) -> int: 
    def get_neighbors(gene, bank): 
        neighbors = []
        for g in bank: 
            diff = 0
            for i in range(0, 8): 
                if gene[i] != g[i]: 
                    diff += 1

            if diff == 1: neighbors.append(g)

        return neighbors

    nodes, visited = deque([(startGene, 0)]), set([startGene])

    while nodes: 
        gene, mutation = nodes.popleft()
        if gene == endGene: return mutation 

        neighbors = get_neighbors(gene, bank)
        for gene in neighbors: 
            if gene in visited: continue
            nodes.append((gene, mutation+1))
            visited.add(gene)

    return -1

#more optimal solution
def solution(startGene: str, endGene: str, bank: list[str]) -> int: 
    def get_mutations(gene): 
        mutations = []
        for i in range(len(gene)): 
            cur_letter = gene[i]
            for l in ['A', 'C', 'G', 'T']: 
                if l != cur_letter: 
                    mutations.append(gene[:i] + l + gene[i+1:])

        return mutations
    
    bank_set = set(bank)
    nodes, visited = deque([(startGene, 0)]), set([startGene])

    while nodes: 
        gene, mutation = nodes.popleft()
        if gene == endGene: return mutation 

        mutations = get_mutations(gene)
        for m in mutations: 
            if m in bank_set and m not in visited:
                nodes.append((m, mutation+1))
                visited.add(m)

    return -1

def test(solution): 
    startGene = "AACCGGTT"
    endGene = "AACCGGTA"
    bank = ["AACCGGTA"]
    sol = solution(startGene, endGene, bank)
    print(sol)

    startGene = "AACCGGTT"
    endGene = "AAACGGTA"
    bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
    sol = solution(startGene, endGene, bank)
    print(sol)

    print("all tests passed")

if __name__ == "__main__": 
    test(solution) 


    
