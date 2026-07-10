class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)

        half = total_length // 2

        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        # we are searching how many elements from A should goto the left half
        left = 0
        right = len(A)
        while left <= right:
            mid = left + (right-left)//2  # there are mid elements from A go to the lefthalf
            
            A_left_last_index = mid - 1
            B_left_last_index = half - mid - 1
            A_right_first_index = mid
            B_right_first_index = half - mid

            if A_left_last_index == -1:
                A_left_last_value = float("-inf")
            if B_left_last_index == -1:
                B_left_last_value = float("-inf")
            if A_right_first_index == len(A):
                A_right_first_value = float("inf")
            if B_right_first_index == len(B):
                B_right_first_value = float("inf")
            
            if A_left_last_index in range(len(A)):
                A_left_last_value = A[A_left_last_index]
            if B_left_last_index in range(len(B)):
                B_left_last_value = B[B_left_last_index]
            if A_right_first_index in range(len(A)):
                A_right_first_value = A[A_right_first_index]
            if B_right_first_index in range(len(B)):
                B_right_first_value = B[B_right_first_index]

            # check whether this partition is valid
            if A_left_last_value <= B_right_first_value and B_left_last_value <= A_right_first_value:
                break
            elif A_left_last_value > B_right_first_value:
                # A took so many elements, which means mid is a too big
                right = mid-1
            elif B_left_last_value > A_right_first_value:
                # B took so many elements, which means mid is too small
                left = mid + 1

        if total_length % 2 == 0:
            return (max(A_left_last_value, B_left_last_value) + min(A_right_first_value, B_right_first_value)) / 2
        else:
            return min(A_right_first_value, B_right_first_value)

