class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution = {}
        for word in strs:
            key = ''.join(sorted(word))

            if key not in solution:
                solution[key] = []

            
            solution[key].append(word)

        return list(solution.values())