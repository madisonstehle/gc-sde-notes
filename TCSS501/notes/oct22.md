_10/22/22, 9:30a-12:00p_

# TCSS 501: Stacks and Queues

## Assignment 1 Review

### **Question 1:**
![Question 1](../img/Question1HW1.png)

### **Question 2:**
![Question 2](../img/Question2HW1.png)

### **Question 3:**
> My Solution: [palindrome.py](./assignments/palindrome.py)

1. Treat a string as an array of characters: so you can use indexes
```python
idx_a = 0
idx_b = len(the_string - 1)
the_string[idx_a].lower() != the_string[idx_b].lower()
```
If they are the same, increment/decrement
```python
idx_a += 1
idx_b -= 1
```
Using `.replace()` works, but it creates a new array by looping through the whole list. This adds additional O(n) functions in the code. It isn't orders of magnitude more efficient though, so you have to balance.

Instead, you could just move the point when you get to the space.
```python
if the_string[idx_b] == " ":
  idx_b -= 1
  continue
```
When do you stop the pointer? When the indexes meet or overlap, or if they find two characters that don't match.
```python
while idx_a < idx_b:
```
![Palindrome Solution 1](../img/palindromesolution.png)

#### ASCII & Bitwise Solution

It can be done WITHOUT `.lower()`! To swap uppercase/lowercase, you can use an ASCII table:
![ASCII Table](../img/ASCIITable.png)

Upper and lower case are 32 apart, so you can toggle.

A = 65 = 01000001
a = 97 = 01100001

M = 77 = 01001101
m = 109 = 01101101

You can use a bitwise and (&) to flip to 0:

mask = 11011111
m & mask = 01001101
M & mask = 01001101

![ASCII Palindrome Solution](../img/ASCIIPalindrome.png)

_____
## Stacks

A data structure that organizes in a **LIFO (Last In First Out)** manner. If you have a stack of something, you much pick up an item at the top of the stack before you can get to items lower in the stack. If you want to add something, you can simply place it on top without disturbing the rest.

Start with an empty stack, and add our first element, we just set the top pointer. Adding a new element to a stack is called a **push**. We say we "push" data onto the stack.

When you push the next el on to the stack, the top element becomes the new element.

To remove, you use **`.pop()`** that takes the data from the top of the stack and the pointer moves to the previous element. To know what that is, you _could_ use an array, but more often using pointers.

```python
class StackNode:
  def __init__(self, data=None):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None
    self.size = 0

  def is_empty(self):
    return self.size == 0

  def push(self, data):
    n = StackNode(data)

    if self.is_empty():
      self.top = n
    else:
      n.next = self.top
      self.top = n
    
    self.size += 1
  
  def pop(self):
    if self.is_empty()
      return None
    else
      r = self.top
      self.top = self.top.next
      self.size -= 1
      return r.data

  def peek(self):
    if self.is_empty():
      return None
    else:
      return self.top.data

    # or return self.top.data if not self.is_empty() else None
```

One example of using a stack is to check and make sure you have matching brackets

```python
def check_brackets(n):
  s = Stack()

  for c in n:
    if c in ('{', '[', '('):
      s.push(c)
    if c in ('}', ']', ')'):
      l = s.pop()
      if l == '{' and c == '}':
        continue
      elif l == '[' and c == ']':
        continue
      elif l == '(' and c == ')':
        continue
      else:
        return False
      
  return s.is_empty()
```

Other uses of stacks:
- Call Stacks
  - Function calls push memory addresses and variables
  - When they return they pop their variables and push the results
  - There is a finite memory reserved for the call stack, if it fills up, then you get a `StackOverflow`
- CTRL + Z
  - As state changes, push the state change onto the stack
  - When undo, reset state (or perform reverse operation)
- Graph Traversal

_____
## Queues

Organize data in **FIFO (First In First Out)** manner. Basically the same as a queue in real life - standing in line for example. Typically only concerned about what is the next thing in line, not the people in positions 5 and 6.

There are reference pointers to the top and bottom. When you add, you **enqueue** an element, you set the top and bottom pointers. As you continue, you keep shifting the bottom pointers. Unlike a stack, items stay in place and aren't pushed down. When you need to remove things, you can **dequeue** them.

Traversal happens between nodes like in linked lists. You need to keep track of both next and previous, because you need to perform actions at both ends of the structure.

```python
class QueueNode:
  def __init__(self, data)
    self.data = data
    self.next = None
    self.prev = None

class Queue:
  def __init__(self):
    self.top = None
    self.bottom = None
    self.size = 0


  def enqueue(self, data):
    n = QueueNode(data)
    if self.top is None:
      self.top = n
      self.bottom = n
    else:
      self.bottom.prev = n
      n.next = self.bottom
      self.bottom = n
    self.size +=1


  def dequeue(self):
    r = self.top

    if not r:
      return None
    
    if self.size == 1:
      self.top = None
      self.bottom = None
    elif self.size > 1:
      self.top = self.top.prev
      self.top.next = None
    
    self.size -= 1
    return r.data
```
A queue _can_ be implemented using two stacks, an inbound stack and an outbound stack.

Accept incoming items on an inbound stack, and then move them when appropriate to an outbound stack.

```python

```
### Queues in Multi-App Environments
Many cloud based queue services are available, or you can implement your own. These services are at their core, just basic queue data structures that allow applications to send messages to the queue, and for (other) applications to listen to them.

Having the queue in between these apps allows them to process or send data at different cadences without one being bogged down by the other.

Events are often bursty, they can be collected faster than they can be processed. The queue can serve as a buffer.