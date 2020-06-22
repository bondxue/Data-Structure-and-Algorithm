# Explanation to Problems

#### problem 1 - LRU Cache

I build LRU Cache use  `OrderedDict` from `collections` module which keep order of insertion of keys and we can change that order if required. The best part is all operations have O(1)​ time complexity.

We maintain our `OrderedDict` in such a way that the order shows how recently they were used. In the beginning, we will have least recently used and in the end, most recently used.
If any update or query is made to a key it moves to the end (most recently used). If anything is added, it is added at the end (most recently used/added)

For `get(key)`: we return the value of the key that is queried in O(1) and return -1 if we don’t find the key in out dict/cache. And also move the key to the end to show that it was recently used.

For `set(key, value)`: first, we add/ update the key by conventional methods. And also move the key to the end to show that it was recently used. But here we will also check whether the length of our ordered dictionary has exceeded our capacity, If so we remove the first key (least recently used)

Since the get and set operations are constant time, our Big O Notation is O(1). Space complexity consists of a node list and a cache dictionary, so our Big O there is O(2n).

Big O Notation Time: O(1) Space: O(n)



#### problem 2 - File Recursion

Since we have to look through every directory to check each file with no limit to the depth of subdirectories can be, the best approach is **recursion**. The trick here was to use `append` in the base case and `extend` in the recursive case for building the list.

The time complexity is Big O of N times the number of directories, since for each directory we call our function again. The space complexity can grow exponentially with each recursive call.

Big O Notation Time: O(n)  Space: O(n)



#### Problem 3 - Huffman Encoding/Decoding

My solution was to use Python's `heapq` library. To encode a string, we first count the frequency of each letter. I then make a binary tree by pulling the two smallest values off of the heap, and adding back my newly made node to the heap.

I then make a mapping from the tree, where I recursively add a '0' or a '1' to the prefix, and put that as the value for the map, where the key is the label or character from the tree.

To get the final encoding, I simply iterate over each key (or character) in the string and get the binary value from the map, and join it all together.

For decoding, we simply iterate over each "bit" in the binary string and append the value (label) while traversing the tree.

For Big O we loop over all characters, we then loop over all frequencies to make the heap. We also recurse through the tree when making the map of characters to binary code. So I believe our performance is O(3n). For space complexity we use a dictionary, a heap, and a recursive call in makeMap, giving us Big O(3n log n)

Big O Notation Time: O(n log n) Space: O(n)



#### Problem 4 - Users in Group

I choose **recursion** to solve this problem. If the user is in the group we return True. Else, for every group in the group we call our function again and search through users.

Big O Notation Time & Space: O(n) No matter the size of users and groups, we have to search through them all recursively to find our user. We use two arrays to store our users and groups, so our Big O grows as simple multiples of these for space.



#### Problem 5 - BlockChain

Our BlockChain problem is really just a node and a linked list. Each node in the list points to the next, while also storing the hash of itself, and its previous hash.

Since we merely iterate through a linked list, and do some hashing functions, the Big O for time should be a simple O(1). And Big O for space is 1 for our hash sha and 1 for our linked list: O(2n). Big O Notation Time: O(1) Space: O(n)



#### Problem 6 - Union and Intersection

In my solution, duplicates are removed, and order is by the input order. The algorithms for both `union` and `intersection` are straightforward. 

The union algorithm has a complexity of O(n^2). The intersection algorithm has a complexity of O(n^2)





