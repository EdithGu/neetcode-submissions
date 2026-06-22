class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # [caconical form of a groupt of anagrams] : [list of anagrams]

        for word in strs:
            # conver each word to the standard caconical form
            array = [0] * 26
            for char in word:
                array[ord(char) - ord('a')] += 1

            array = tuple(array)

            res[array].append(word)

        return list(res.values())







