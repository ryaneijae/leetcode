class Solution:
    def merge_arrays(self, arr1, arr2):
        i = j = 0
        new_arr = []
        
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                new_arr.append(arr1[i])
                i += 1
            else:
                new_arr.append(arr2[j])
                j += 1
        
        if i < len(arr1):
            new_arr.extend(arr1[i:])
        elif j < len(arr2):
            new_arr.extend(arr2[j:])

        return new_arr


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_arr = self.merge_arrays(nums1, nums2)
        arr_len = len(new_arr)
        if arr_len % 2: # is odd
            return new_arr[arr_len // 2]
        return (new_arr[arr_len // 2] + new_arr[(arr_len // 2) - 1]) / 2
