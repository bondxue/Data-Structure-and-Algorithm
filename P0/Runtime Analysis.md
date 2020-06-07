### Runtime Analysis 

---

#### Task0.py

Array access via index 5 times, so time complexity is $O(5*1)\approx O(1)$.

#### Task1.py

There are two `for` loops and each loop with complexity $O(n)$ will implement two `set.add()` with complexity $O(1)$. So total complexity is $O(2*2*n) \approx O(n)$ overall.

#### Task2.py

+ One `for` loop with complexity $O(n)$, and each iteration will check existence of element in dictionary with complexity $O(1)$ twice and add insert value $O(1)$. Then add value with complexity $O(1)$.

+ Find `max` value in the dictionary has complexity $O(n)$. 
+ `print` with access dictionary $O(1)$.

So complexity of the program is roughly $O(n*4 + n + 1) \approx O(n)$.





