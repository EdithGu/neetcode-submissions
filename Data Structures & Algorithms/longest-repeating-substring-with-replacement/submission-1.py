class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        hashmap = {}
        longest = 0
        mostFreq = 0

        for right in range(len(s)):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1
            temp = max(mostFreq, hashmap[s[right]])
            
            if self.checkValid(left, right, k, max(mostFreq, hashmap[s[right]])):
                mostFreq = max(mostFreq, hashmap[s[right]])
                longest = max(longest, right-left+1)
                
                continue
            else:
                while not self.checkValid(left, right, k, max(mostFreq, hashmap[s[right]])):
                    hashmap[s[left]] = max(hashmap[s[left]]-1, 0)
                    left += 1

        return longest

    def checkValid(self, left, right, k, mostFreq):
        curLength = right - left + 1
        return curLength - mostFreq <= k

          