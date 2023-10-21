class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxf = 0
        res = 0

        # count.get(s[i], 0) gets the current count of the character s[i] from the count dictionary. If the character s[i] is not already a key in the dictionary, count.get(s[i], 0) returns the default value of 0.
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res


obj = Solution()
print(obj.characterReplacement("ABAB", 2))
print(obj.characterReplacement("AABABBA", 1))
