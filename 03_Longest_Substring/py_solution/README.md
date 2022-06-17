<!-- AUTO-GENERATED-CONTENT:START (STARTER) -->
<h1 align="center">
  Notes on Solution
</h1>


## 1 Brute Force Solution

The brute force way to do this would be to loop through the string, for each element, look for if it is found in the string at another point. If it is, then keep track of that value. Do this for the entire string.

At worst, you will have to loop through the entire string for each element in the list, thus the time complexity would be O(n^2) I beleive. 

A better solution would be to keep track of each element in a dictionary with the index. Then when we come upon an element, we say is this element in the dictionary, if not, then add it. If it is, then return it's index we have stored, substrac the current index from that index, and if that value is greatest, then that is our answer.

Okay, so I made my solution, but it's not perfect, it looks to mimimize the size of the string length, when we want to maximize it. 


    
## 2 Correct Solution 💫 
The solution looks at a sliding window. You can check to see if you have a duplicate value by using a set. A set can only contain one of each value, therefore we can use that to keep track of our string.

We will look at the string and see if there is a character that contains the same letter, if it does then we minimize our substring by one on the left, we then check again, if we no longer have a repreated character then we extend one to the right. We then continue this process until we have found our longest substring. We are almost inching accross the string, and then we shorten or lengthen our window or substring, until we have our answer. 

The time complexity would be O(N), and the space is O(m). 






