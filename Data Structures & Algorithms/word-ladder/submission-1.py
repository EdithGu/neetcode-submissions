class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = collections.deque()
        queue.append(beginWord)
        step = 1
        wordList = set(wordList)

        if endWord not in wordList:
            return 0

        while queue:
            print(queue)
            level_size = len(queue)
            step += 1
            # if there are not candidates word and no current words is endWord
            # we can terminate early
            if not wordList:
                return 0

            for _ in range(level_size):
                cur_word = queue.popleft()
                # there are 25 * n neis
                for pos in range(len(cur_word)):
                    for alpha in "abcdefghijklmnopqrstuvwxyz":
                        print(f"pos:{pos}, alpha:{alpha}")
                        nei = cur_word[0:pos] + alpha + cur_word[pos+1:]
                        if nei in wordList and nei == endWord:
                            return step
                        if nei in wordList:
                            wordList.remove(nei)
                            queue.append(nei)

        return 0

        
