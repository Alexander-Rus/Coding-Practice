

class Solution:
	def twoSum(self, nums: list[int], target: int) -> list[int]:
		d = {}
		for i, n in enumerate(nums):
			m = target - n
			if m in d:
				return [d[m], i]
			else:
				d[n] = i




def main():
	solution2 = Solution()
	print(solution2.twoSum([5, 7, 31, 67, 9, 78, 2, 7], 14))



if __name__ == "__main__":
	main()
