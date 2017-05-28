class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) < len(nums2):
            return findMedianSortedArrays(nums2,nums1)
        else:
            i=0;j=0
            temp = []
            while True:
                if i<=len(nums1)-1:
                    if nums1[i]<nums2[j]:
                        temp.append(nums1[i])
                        i+=1
                elif j<=len(nums2)-1:
                    if nums2[j]<nums1[i]:
                        temp.append(nums2[j])
                        j+=1
                else:
                    break
        print temp
        if len(temp)%2 != 0.0:
            return temp[len(temp)/2]
        else:
            return (temp[(len(temp)/2)-1]+temp[(len(temp)/2)])/2
s=Solution()
print(s.findMedianSortedArrays([1,2],[3,4]))
