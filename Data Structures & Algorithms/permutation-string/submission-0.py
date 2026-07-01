class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = {}
        for i in s1:
            hashmap[i] = hashmap.get(i, 0) + 1
        totalCount = len(hashmap)

        left = 0
        charCount = 0
        for right in range(len(s2)):
            hashmap[s2[right]] = hashmap.get(s2[right], 0) - 1

            if hashmap[s2[right]] == 0:
                charCount += 1

            if right - left + 1 > len(s1):
                hashmap[s2[left]] += 1
                if hashmap[s2[left]] == 1:
                    charCount -= 1
                left += 1

            if charCount == totalCount:
                return True

        return False




        