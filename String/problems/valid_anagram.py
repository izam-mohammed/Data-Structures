class Solution:
    def valid_anagram(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        s1_d = {i: sum([1 for k in s1 if k == i]) for i in set(list(s1))}
        s2_d = {i: sum([1 for k in s2 if k == i]) for i in set(list(s2))}

        return s1_d == s2_d


obj = Solution()
print(obj.valid_anagram("hai hai", "hai iah"))
