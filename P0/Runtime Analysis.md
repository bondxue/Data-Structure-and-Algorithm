### Runtime Analysis 

---

#### Task0.py

Array access via index 5 times, so time complexity is $O(5*1)\approx O(1)$.

#### Task1.py

There are two `for` loops and each loop with complexity $O(n)$ will implement two `set.add()` with complexity $O(1)$. So total complexity is $O(2\times2\times n) \approx O(n)$ overall.

#### Task2.py

+ One `for` loop with complexity $O(n)$, and each iteration will check existence of element in dictionary with complexity $O(1)$ twice and add insert value $O(1)$. Then add value with complexity $O(1)$.

+ Find `max` value in the dictionary has complexity $O(n)$. 
+ `print` with access dictionary $O(1)$.

So complexity of the program is roughly $O(n\times4 + n + 1) \approx O(n)$.

#### Task3.py

+ One `for` loop with complexity $O(n)$, in each iteration check `is_from_Bangalore()` with complexity $O(1)$ and `get_areacode()` with constant complexity $O(1)$, add 1 for two `count` with complexity $O(1)$ and `set.add()` with $O(1)$. So total `for` loop with $O(n)$

+ sort list with complexity $O(nlog(n))$.
+ `for` loop `print` with $O(n)$
+ final `print` with `divide` calcuation with $0(1)$

So complexity of the program is roughly $O(n+ nlog(n)+n+1)\approx O(nlog(n))$

#### Task4.py

+ four list comprehension with complexity $O(n)$
+ set operation to find the difference among sets with complexity $O(n)$
+ sort list with complexity $O(nlog(n))$
+ `for` loop `print` with $O(n)$

So complexity of the program is roughly $O(n+n+nlog(n)+n)\approx O(nlog(n))$

