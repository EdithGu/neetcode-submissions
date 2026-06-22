class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} # num : freqCount
        for num in nums:
            count = freq.get(num, 0) + 1
            freq[num] = count
        
        # Bucket Array size n+1, cuz the most times an element can occur is n
        bucketArray = [[] for _ in range(len(nums)+1)] 

        for num, count in freq.items():
            bucketArray[count].append(num)

        res = []
        # from tail to get the topK
        for i in range(len(bucketArray)-1, 0, -1):
            if (k>0 and bucketArray[i] is not None):
                res.extend(bucketArray[i])
                k -= len(bucketArray[i])
                if (k==0) :
                    return res
            

