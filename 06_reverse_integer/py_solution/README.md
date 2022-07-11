<!-- AUTO-GENERATED-CONTENT:START (STARTER) -->
<h1 align="center">
  Notes on Solution
</h1>


## 1 Brute Force Solution

To reverse the integer there are a few ways that this can be done. But there is a very strict size limit that we need to consider. 
It is very useful to remember that %10 (mod 10) is a good way to get the last digit. We are dividing by 10, and the remainder will always be what the last digit is. 

    
## 2 Correct Solution 💫 

So yes you do use modulo to get the digit that is in the ones place. Once you add that to the string you are building, you then will divide by 10 without using modulo. 

So 123 % 10 -> 3, as 3 is the remainder. Our new string then will have a 3 added to it, assuming you start at zero. You will then do 123 / 10 -> 12. You then multiply our string builder by 10, so it becomes 30. You then would repeat the process and add 2, making it 32. 

So to make sure that we stay in the 32-bit bounds, we are going to see if our value is equal to the max value all the way up the last digit. Since we can't store the entire value, we are going to have to store most of it, and then keep the last digit seperate. 


