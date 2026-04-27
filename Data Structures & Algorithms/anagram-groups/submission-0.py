class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dt = {}
        for st in strs:
            sort_st = ''.join(sorted(st))
            if sort_st in dt:
                dt[sort_st].append(st)
            else:
                dt[sort_st] = [st]
        return list(dt.values())

