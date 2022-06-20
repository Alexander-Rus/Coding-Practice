<!-- AUTO-GENERATED-CONTENT:START (STARTER) -->
<h1 align="center">
  Notes on Solution
</h1>


## 1 Brute Force Solution

So right away, my first thought is to just reverse each of the lists, and then convert the values to numbers and then add them together. 

Create a string builder, make the values into numbers, then add them, then put them back into a linked list. 

So for the first example:
[2, 4, 3] -> 342
[5, 6, 4] -> 465

342+465 = 807 -> [7, 0, 8]


Okay, so for each element in the list, you would add them. If the value is over 9, you would add the remainder to the next value in the list. You would then be sure to add that to the next value when you do the addition.

Example:

[2, 4, 3]
[5, 6, 4]

2+5 = 7
4+6 = 10, therefore you put 0, and then carry the 1
3+4=7, then plus the 1 is 8. So the final answer is 807


    
## 2 Correct Solution 💫 
This question is not too bad in my opinion, the tricky part is the edge cases. You need to be careful about adding the additional item to the list for the carry over value. 

Additionally, you need to understand that the lists are not normal lists, they are nodes, that have values and then a next value. Interacting with the node is the important part of this problem.
So essentially you do just end up doing addition along the lines of each index, you then carry the remainder and continue.




