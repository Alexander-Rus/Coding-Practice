<!-- AUTO-GENERATED-CONTENT:START (STARTER) -->
<h1 align="center">
  Notes on Solution
</h1>


## 1 Brute Force Solution

The brute force solution would be to check every sub-string to see if it is a palidrome, then check to see if it is the longest one. 

s = "abcadefgfedi" You should start at the beginning, and then as you go, check to see if there are any paldromes.

Okay, so for something to be palidromic, we need to see the same character in the string right, so in the example above, I would store the entire string in a dictionary, then I would say, is a a repreated character? no , then remove it. Is be a repreated character? no, then remove it. Continue until you get to d, it is a repreated character, is the substring between them a palidrome? Yes, if it is the longest right now, set that as our result. 

There is definitely a way to do this with pointers. So consider if you have a pointer at the beginning.
So for this solution I would think that we are going to want to do a sliding window type of solution.


    
## 2 Correct Solution 💫
The best solution is to have two pointers that start off the same, then move outwards and check to see if they is a palindrome. You would want to start by looking at the first element, if there is nothing to the left of it, then it's max palindrome can only be itself. 








