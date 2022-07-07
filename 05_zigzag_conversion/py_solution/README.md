<!-- AUTO-GENERATED-CONTENT:START (STARTER) -->
<h1 align="center">
  Notes on Solution
</h1>


## 1 Brute Force Solution

I would say right off the bat that when considering how to solve this you are going to need to consider the index as an important factor. In the first example, the first letter is going to go into index[0] of the first array. The second letter would then go into index[0] of the second array. The third letter then goes into the index[0] of the third array. Then you have to send the fourth leter to array 2, but of index[1]. Very tricky. 

How about we look at this from the perspective of jumps. If we want to consider how many characters we should be jumping then how do we determine where we want to go each time?

    
## 2 Correct Solution 💫
The best solution is to consider how many jumps from the first row and onwards we need to go.









