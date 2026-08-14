nums = [1,2,3,4,5,6,7]
k=5

nums1 = nums[-k:]
nums2 = nums[0:len(nums)-k]
nums3 = nums1 + nums2
print(nums3)