class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            length = len(string)
            res.append(f'{length}#{string}')
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # extract number
            i, length = self.extract_length(i, s)

            # i is pointing to # now
            string = []
            for j in range(i+1, i+1+length): 
                string.append(s[j])
            decoded = "".join(string)
            res.append(decoded)

            # update i to make it point to the length number of next string
            i = i + length + 1

        return res

    def extract_length(self, index: int, s: str) -> [int, int]:
        num = []
        while s[index] != "#":
            num.append(s[index])
            index += 1
        length = int("".join(num))
        return [index, length]
        





