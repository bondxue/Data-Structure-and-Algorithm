# Explanations for Project 3 Problems

#### Problem 1 - Finding the Square Root of an Integer

The idea is to find the largest integer `i​` whose square is less than or equal to the given value. The idea is to use **binary search** to solve the problem. The values of ​`i` * `i​` is monotonically increasing, so the problem can be solved using binary search.

**Complexity Analysis:**

- **Time complexity:** O(log n).
  The time complexity of binary search is O(log n).
- **Space Complexity:** O(1).
  Constant extra space is needed.



#### Problem 2 - Search in a Rotated Sorted Array

The idea is to find the *pivot point*, divide the array in two sub-arrays and call **binary search**.
The main idea for finding pivot is - for a sorted (in increasing order) and pivoted array, pivot element is the only element for which next element to it is smaller than it.

**Complexity Analysis:**

- **Time complexity:** O(log n).
  The time complexity of binary search is O(log n).

- **Space Complexity:** O(1).
  Constant extra space is needed.

  

#### Problem 3 - Rearrange Array Elements

We know that a maximum number can be formed from given digits (0-9) when the largest digit appears first, second largest digit appears second, and so on. Finally, the smallest digit appears in the end. We can extend the same logic to solve this problem. We start by merged sorting the specified array in descending order and construct two numbers (say `num1` and `num2`) by picking alternating digits from the array, i.e., `num1` is filled with digits at the odd indices and `num2` is filled with digits at the even indices of the sorted array. 

**Complexity Analysis:**

- **Time complexity:** O(nlog n).
  The time complexity of merged sort is O(log n) and iterate the sorted array twice with O(n), so the total complexity is O(log n).
- **Space Complexity:** O(n).
  Merge sort space complexity is O(n) as it must create a copy of the entire list.



#### Problem 4 - Dutch National Flag Problem

Firstly, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

**Complexity Analysis:**

- **Time complexity:** O(n).
  Iterate the array once for counting number O(n), then need O(n) to overwrite array
- **Space Complexity:** O(1).
  Since we overwrite input list, so no extra space needed. 




