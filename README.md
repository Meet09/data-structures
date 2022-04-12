# data-structures

Linked list methods
----
- push(data)\
    data: The data or element which you  want to add to linkedlist.
    ```python
    ll = linkedlist()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.printnodes()
    ```
  output\
  `1 2 3`


- pushAfter(element, data)\
element: Element in the linkedlist after which the data will be added.\
data: The data or element which you  want to add to linkedlist.

    ```python
    ll = linkedlist()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.printnodes()
    ll.pushAfter(2,10)
    ll.printnodes()
    ```
  output
  ```
  1 2 3
  1 2 10 3
  ```
- pop()\
    It removes the last element of linkedlist
     ```python
    ll = linkedlist()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.printnodes()
    ll.pop()
    ll.printnodes()
    ```
  output
  ```
  1 2 3
  1 2
  ```
  
- removeFirst()\
    It removes the first element of linkedlist
    ```python
    ll = linkedlist()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.printnodes()
    ll.removeFirst()
    ll.printnodes()
    ```
  output
  ```
  1 2 3
  2 3
  ```
- removeAfter(element)\
    It removes the data, after given element from linkedlist
    ```python
    ll = linkedlist()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll.printnodes()
    ll.removeAfter(3)
    ll.printnodes()
    ```
  output
  ```
  1 2 3 4 5
  1 2 3 5
  ```
- searchElement(element)\
   If the given element is found in the linkedlist then it will return `True` otherwise `False`.
    ```python
    ll = linkedlist()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll.printnodes()
    print(ll.searchElement(3))
    print(ll.searchElement(10))
    ```
  output
  ```
  1 2 3 4 5
  True
  False
  ```
- printnodes()\
   It removes the data, after given element from linkedlist
    ```python
    ll = linkedlist()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.printnodes()
    ```
  output
  ```
  1 2 3
  ```
- length()\
 It removes the first element of linkedlist
    ```python
    ll = linkedlist()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll.printnodes()
    ll.length()
    ```
  output
  ```
  1 2 3 4 5
  5
  ```
