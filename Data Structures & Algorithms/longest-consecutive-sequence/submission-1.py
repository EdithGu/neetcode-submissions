class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0

        # put the list array to a set
        nums_set = set(nums)

        # loop through the array searching for the possible start of a sequence
        max_seq_len = 1
        for num in nums:
            if num-1 in nums_set: # num is not the start
                continue
            
            # num is the start, then search for numbers follow it
            num_in_sequence = num+1
            seq_len = 1
            while num_in_sequence in nums_set:
                seq_len += 1
                num_in_sequence += 1
            if seq_len > max_seq_len:
                max_seq_len = seq_len

        return max_seq_len





        