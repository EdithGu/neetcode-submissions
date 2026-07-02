class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashmap = {}
        for char in t:
            hashmap[char] = hashmap.get(char, 0) + 1
        print(hashmap)

        left = 0
        charCount = 0
        res_len = float("inf")
        res = [0, 0]

        for right in range(len(s)):
            if s[right] in hashmap:
                hashmap[s[right]] -= 1
                if hashmap[s[right]] == 0:
                    charCount += 1
                print(f"right:{right}, charCount:{charCount}, hashmap:{hashmap}")
            
            while charCount == len(hashmap):
                # record current sliding window
                if right - left + 1 < res_len:
                    print(f"cur left and right pointer: {left} and {right}, cur_len:{right - left + 1}, res_len:{res_len}")
                    res_len = right - left + 1
                    res = [left, right]
                if s[left] in hashmap:
                    hashmap[s[left]] += 1
                    if hashmap[s[left]] == 1:
                        charCount -= 1
                left += 1

        print(res_len)
        print(res_len is not float("inf"))
        return s[res[0]:res[1]+1] if res_len != float("inf") else ""




