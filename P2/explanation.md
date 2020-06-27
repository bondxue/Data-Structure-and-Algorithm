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
  The time complexity of merged sort is O(nlog n) and iterate the sorted array twice with O(n), so the total complexity is O(n log n).
- **Space Complexity:** O(n).
  Merge sort space complexity is O(n) as it must create a copy of the entire list.



#### Problem 4 - Dutch National Flag Problem

Using two pointers, one records the number of `0`  and the other records the number of `0` and `1`.

**Complexity Analysis:**

- **Time complexity:** O(n).

  Only iterate the input array once. 

- **Space Complexity:** O(1).
  Since we overwrite input list, so no extra space needed. 



#### Problem 5 - Autocomplete with Tries

Tried to use `yeild` function instread of recursive method. 

To generate suffixes, we first call `find` on the Trie class to find our prefix. Then, with the returned node, we can call `suffixes` on the TrieNode class. This is a simple wrapper to join the yielded result of `generate_suffixes`, which uses recursion to search all nodes in children and call itself until is_word is True.

##### Find Method:

+ **Time Complexity:** O(n*m)

  `n` is the number of inputs and `m` is the length of the average input

+ **Space Complexity:** O(1)

  No memory is allocated

##### Insert Method:

+ **Time Complexity:** O(n)

  Each character needs to be iterated through

+ **Space Complexity:** O(n)

  n characters need to be allocated

##### Suffixes Method:

+ **Time Complexity:** O(n)

  Each character needs to be iterated through

+ **Space Complexity:** O(1)

  No memory is allocated besides a simple variable `generated`. 



#### Problem 6 - Max and Min in a Unsorted Array

Set the initial `min_num` and `max_num` values as the first value in the array. It then iterates once through and adjusts them accordingly.

**Complexity Analysis:**

- **Time complexity:** O(n).
  The array is iterated through once.
- **Space Complexity:** O(1).
  No additional memory is allocated.



#### Problem 7: Request Routing in a Web Server with a Trie

My implementation is exactly the same as problem 5 with some slight differences. I had to string clean the path by removing outside occurences of `/` with strip and then split it.



##### Find Method:

+ **Time Complexity:** O(n*m) 

  `n` is the number of  path part and `m` is the length of the average length of path part

+ **Space Complexity:** O(1)

  No memory is allocated

##### Insert Method:

+ **Time Complexity:** O(n)

  Each part of the path needs to be iterated through

+ **Space Complexity:** O(n)

  n characters need to be allocated

##### Add Handler Method

+ Time Complexity: O(n) 

  Each part of the path needs to be iterated through

+ Space Complexity: O(n) 

  A new TrieNode is created for each part of the path

##### Lookup Method

+ Time Complexity: O(n)

+ Space Complexity: O(1)

  No additional memory is allocated



