import sys


	
	
class Solution:
	def twoSum(self, nums: list[int], target: int) -> list[int]:
	    for num in nums:
		    for second_num in nums:
			    if num + second_num == target:
				    return [nums.index(num), nums.index(second_num)]
	
	
def main():
	solution1 = Solution()
	print(solution1.twoSum([2, 7, 11, 15], 9))
					    
	
if __name__ == "__main__":
	main()
