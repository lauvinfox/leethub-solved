class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = []
        curX = 0
        curY = 0

        while curX < len(nums1) and curY < len(nums2):
            if nums1[curX] <= nums2[curY]:
                merged_list.append(nums1[curX])
                curX += 1
            else:
                merged_list.append(nums2[curY])
                curY += 1

        if nums1[curX:] or nums2[curY:]:
            merged_list.extend(nums1[curX:]) if nums1[curX:] else merged_list.extend(nums2[curY:])

        index = (len(merged_list) - 1) // 2
        if len(merged_list) % 2:
            return (float(merged_list[index]))
        else:
            return (merged_list[index] + merged_list[index+1]) / 2