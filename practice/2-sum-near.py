class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) < len(nums2):
            return findMedianSortedArrays(nums2,nums1)
        else:
            temp = []
            i=0;j=0;
            print len(nums1),len(nums2)
            while i<=len(nums1)-1 and j<=len(nums2)-1:
                if nums1[i]<nums2[j]:
                    temp.append(nums1[i])
                    i+=1
                else:
                    temp.append(nums2[j])
                    j+=1
        print temp

s=Solution()
s.findMedianSortedArrays([1,3,5],[2,4])
