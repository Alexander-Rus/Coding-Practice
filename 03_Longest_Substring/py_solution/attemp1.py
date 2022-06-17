

class Solution:
	def longestSubstring(self, s):
		d = {}
		length = 0
		for i, s in enumerate(s):
			if s in d:
				templength = i - d[s]
				if templength > length:
					length = templength
				d[s] = i
			else:
				d[s] = i
				print(d)
		return length

def main():
	solution1 = Solution()
	print(solution1.longestSubstring("pwwkew"))
	
	
if __name__ == "__main__":
	main()
