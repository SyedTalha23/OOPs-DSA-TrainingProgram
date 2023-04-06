'''Given a queue of whole numbers. Write a python function to return a new queue which contains the evenly divisible numbers.

Note: A number is said to be evenly divisible if it is divisble by all the numbers in the given range without any reaminder.
Consider the range to be from 1 to 10 (both inclusive)
Assume that there will always be few elements in the input queue, which are evenly divisible by the  numbers in the mentioned
range.

Example:
Input Queue: 13983,10080,7113,2520,2500(front -rear)
Output Queue: 10080,2520(front-rear)'''

from queue import Queue
q1 = Queue()
q2= Queue()
l=list(map(int,input().split(",")))
for i in l:
    q1.put_nowait(i)
for i in range(q1.qsize()):
    temp=q1.get_nowait()
    if all(temp%i==0 for i in range(1,11)):
        q2.put_nowait(temp)
for i in range(q2.qsize()-1):
    print(q2.get_nowait(),end=",")
print(q2.get_nowait())

