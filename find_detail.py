class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        lt1 = nums1.sort()
        lt2 = nums2.sort()
        result = []
        i=j=0
        while i< len(nums1) and j < len(nums2):
            if nums1[i]>nums2[j]:
                j += 1
            elif nums1[i]<nums2[j]:
                i += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1
        result.sort()
        k=0
        while k<len(result)-1:
            if result[k]==result[k+1]:
                result.pop(k)
            k+=1
        return result

a = Solution()
b=a.intersection([1, 2, 2, 1,5],[1,2,5,2])
print(b)
