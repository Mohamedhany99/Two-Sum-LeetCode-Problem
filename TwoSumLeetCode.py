class Solution(object):
    def twoSum(self, nums, target):
        sz = len(nums)
        result =[]
        i=0
        while(i<sz):
            print("i:",i)
            j=i+1
            while(j<sz):
                if nums[i]+nums[j]==target:
                    result.append(i)
                    result.append(j)
                    print("appended")
                else:
                    print("false ",nums[i]," + ",nums[j],"not equals to ",target)
                j+=1
            i+=1
        return result
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        