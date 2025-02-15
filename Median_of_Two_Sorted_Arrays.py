class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged_list = nums1 + nums2
        merged_list.sort()  
        print(merged_list)
        total_elements = len(merged_list)

        if total_elements % 2 == 1:
            return float(merged_list[total_elements // 2 - 1])
        else:
            middle1 = merged_list[total_elements // 2 - 1 ]
            middle2 = merged_list[total_elements // 2]
            return (middle1 +middle2 )/2

solution = Solution()

nums1 = input("nums1: ")
nums2 = input("nums2: ")
nums1 = list(map(int,nums1.split()))
nums2 = list(map(int,nums2.split()))
result = solution.findMedianSortedArrays(nums1, nums2)

print("Median:", result)
