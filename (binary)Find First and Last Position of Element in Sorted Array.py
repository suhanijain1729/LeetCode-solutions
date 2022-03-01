class Solution(object):
    def searchRange(self, nums, target):
        nums.sort()
        f=-1
        l=-1
        for i in range(len(nums)):
            if(nums[i]==target):
                f=i
                break
        for i in range(len(nums)-1,-1,-1):
            if(nums[i]==target):
                l=i
                break
        
        return(f,l)