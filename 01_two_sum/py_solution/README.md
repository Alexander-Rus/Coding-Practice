<!-- AUTO-GENERATED-CONTENT:START (STARTER) -->
<h1 align="center">
  Notes on Solution
</h1>


## 1 Brute Force Solution

In this solution we simply check all combinations of values in the array, until we get a value that adds to the target value.

In the first example we have the array `[2,7,11,15]` with a target of `9`. Let's actually change that around so we have a better example. Let's say the array is `[11, 7, 15, 6, 2, 4]` and the target is still 9. We want to return a value of `[1,4]` as 7+2 = 9.
 
For the brute force solution, you would loop through the array, and then for each element, you would try adding all additional elements following it. For example, starting with 11, you would loop through and do 11+7, 11+15, 11+6, 11+2, 11+4, and see if any of them add to 9. None do, so you then move to 7, and do 7+15, 7+6, 7+2, 7+4, and so on. You so find the solution this way, but at it's worst case this would take O(n^2) to complete, because you are re-checking values you tested before. 

This solution does work, but you ideally want to do a one pass solution. You want to be able to check a value once, and then move on.
    
## 2 Correct Solution 💫 

We know that there can only ever be one pair of indices that add to the target. Therefore, we can assume that if num1 +num2 = target, then num1 = target - num2.

We can use enumerate to create a list of values and pair them to indices in the array, and we can store the values that we have already checked in a dictionary. 

So we start by doing x = 9 - 11. In this case x = -2. 
We then say, is -2 in our dictionary? 
No it is not, the dictionary is emtpy right now. 
We then add it to our dictionary with value d[11] = 0 (denotes that 11 is at index 0)

We then do x = 9 - 7. In this case x = 2.
We then is, is 2 in our dictionary?
It is not.
We then add our value to the dictionary once again. d[7] = 1

We then repeat this process for the next values and our dicionary will look like:
{
[11, 0]
[7, 1]
[15, 2]
[6, 3]
}

We now get to the value 2. 
We do x = 9 - 2. X would equal 7
Is 7 in our dicionary? Yes! it is. We know then that we have a pair that matches.
We would then look in our dicionary and return the index of 7. d[7] = 1, and return the current index of 2 -> 4.


So what makes this solution work well, is that looking in the dicionary has a near constant time. 
Additionally, we use enumerate to easily pair indices to values in the array.




