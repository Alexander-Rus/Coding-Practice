
class Solution():
	def longestPalindrome(self, s):
		res = ''
		
		for i in range(len(s)):
			odd = self.palindromeAt(s, i, i)
			even = self.palindromeAt(s, i, i+i)
			
			res = max(res, odd, even, key=len)
		return res
		
	def palindromeAt(self, s, l, r):
		while l >= 0 and r < len(s) and s[l] == s[r]:
			l -= 1
			r += 1
		return s[l+1:r]



def main():
	solution1 = Solution()
	print(solution1.longestPalindrome("abcdefedgh"))


if __name__ == "__main__":
	main()
