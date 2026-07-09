class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dt = {}
        for st in strs:
            arr = [0]*26
            for char in st:
                arr[97 - ord(char)] += 1
            key = "-".join(map(str, arr))
            if key in dt:
                dt[key].append(st)
            else:
                dt[key] = [st]
        return list(dt.values())