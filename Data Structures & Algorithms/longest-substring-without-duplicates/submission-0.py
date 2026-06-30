class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        hashset = set()
        globalMax = 0

        for right in range(len(s)):
            if s[right] not in hashset:
                hashset.add(s[right])
                globalMax = max(globalMax, len(hashset))
            else: 
                # keep removing left elements until there is no duplicated elements in hashset
                while s[left] != s[right]:
                    hashset.remove(s[left])
                    left += 1

                hashset.remove(s[left])
                left += 1
                hashset.add(s[right])

        return globalMax

            