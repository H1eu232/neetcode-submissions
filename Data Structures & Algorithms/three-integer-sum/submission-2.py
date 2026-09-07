class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # a + b + c = 0 
        # -a = b + c

        # 1. Sort the array 
        # 2. For each number in nums, do the 2Sum II approach (leftpointer, rightPointer) to find all the sums that can create a triplet
        # 3. Once you find it, add it to an array of triplets, put leftPointer to the next index, because you dont want to redo the matches of the numbers you already passed 
        #  keep going until you reach the second last index (as you cant create a triplet with 2 values)

        tripletsArray = []
        nums.sort()

        for index, number in enumerate(nums): 

            target = -number 
            leftPointer = index+1
            rightPointer = len(nums) - 1

            print('target: ', target)

            total = 0

            if index == 0 or nums[index] != nums[index-1]: 

                while leftPointer < rightPointer:

                    total = nums[leftPointer] + nums[rightPointer]
                    
                    if total > target: 
                        rightPointer = rightPointer - 1

                    elif total < target:
                        leftPointer = leftPointer + 1

                    elif total == target: 
                        triplets = [-target, nums[leftPointer], nums[rightPointer]]
                        tripletsArray.append(triplets)

                        leftPointer = leftPointer + 1
                        while nums[leftPointer] == nums[leftPointer - 1] and leftPointer < rightPointer:
                            leftPointer += 1

        return tripletsArray

                



            

            

    




            
        
