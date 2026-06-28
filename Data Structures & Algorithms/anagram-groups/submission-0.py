class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        omg = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in omg:
                omg[key] = [word]
            else:
                omg[key].append(word)
        return list(omg.values())