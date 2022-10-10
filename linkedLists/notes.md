## Linked Lists Notes
- Use dummys nodes for edge cases
- Use slow/fast pointers to:
    - Reach the `1/n` th node of the list, when the length of the list is unknown
    - Reach the `nth` last node of the list by keeping distance between slow & fast pointers
- Use data structures (minHeap, etc.) to keep track of global min/max nodes of more than 2 lists
    - minHeap in Python:
    ```
    from queue import PriorityQueue
    minHeap = PriorityQueue()
    minHeap.get()
    minHeap.put((value, index))
    minHeap.qsize()
    ```
