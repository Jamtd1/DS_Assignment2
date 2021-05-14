# Stack ADT

A stack Abstract Data Type (ADT) is defined by it's first in last out data structure. This means in a stack ADT whatever value is `pushed` onto the stack first will be the last element to be processed. For example take the following list of operations:

- push(1): Head -> 1
- push(2): Head -> 2 -> 1
- pop(): Head -> 1
- push(3): Head -> 3 -> 1
- pop(): Head -> 1

In the above example the first element or "Head" of the stack always points to the last value pushed onto the stack and even though 2 pop operations are made the value first pushed onto the stack (1) is not processed yet.

### Key Operations

#### push

This operation is used to add a value to the top of the stack, as long as this value remains on top of the stack it will be the first value processed.

#### pop

This operation returns the value currently on top of the stack and removes it from the stack.

#### top

This operations differs from the pop operation by returning the value on top of the stack without removing it.

### Uses of a stack ADT

#### Undo Function

A stack is very useful when attempting to implement undo functionality. For this functionality to work we need to maintain an ordered list of operations (changes) that have been made and be able to revert those changes in the correct order.

Using a the `push` operation we can add changes onto the stack, ensuring they are recorded without overwriting the previous changes while maintaining the correct order.

When we whish to complete an undo operation we can then `pop` the operation from the stack, essentially undoing the change.

#### NEEDS ONE MORE HERE!!!!!!!

tail recursion

# Queue ADT

A queue ADT is defined by it's first in, first out data structure. This means the first value put into the queue will be the first value to be processed.



### Key Operations

#### enqueue

This operation will add a value to the end of the queue. To do this we need to create a new node (QueueItem in my examples) and set the current tails (i.e. last value in the queue) next value to be the new value. We then set the previous value of the new node (i.e. `tail.next.previous`) to be the current tail. Now that the new node exists on the queue the last step is to point the tail at it by setting the tail to `tail.next`.

> Note that when adding the first item to the list the operation only creates a new node and sets both the head and tail to point at it

#### dequeue

This operation takes the first item from the queue (the first value added), removes it from the queue and returns the value. This operation is much simpler than the `enqueue` operation. It first retrieves the current value of the first item in the queueu (head) and stores it in a temporary parameter to be returned later. Lastly it sets the head to equal the next item in the queue and if that item is not empty it will set it's previous value to None as no items exist after the head pointer.

### Other operations

#### peek

This operation acts much the same as the top operation does for a stack by returning the first value of a

#### get_size

Chacking the overall length of the queue allows us to allocate resources to a particular queue if it is growing quicker than another. However checking the entire length of a linked list via traversal is inefficient so instead we keep a record of the number of successful enqueue & dequeue operations that have occurred and record these as a single integer value. While there is the possiblity of the length of the queue and the integer value becoming out of sync via a logic error the performance gains are worth it.

#### is_empty

This is a helper function that allows us to check if the queue has any elements in it without calling peek or dequeue

#### is_full

Most queues will have some upper bound after which you can no longer add items to the queue. This ensures that the queue cannot absorb allocate too much memory on the system which will impact performance or worse crash the system if memory completely runs out.

### Uses of a queue ADT

#### Ticketing

Many companies that sell tickets online implement a queue system in order to prevent the same ticket being sold to two people or having their infrastructure overwhelmed by the traffic.

A queue helps them to combat this by only allowing a small number of people to purchase tickets at a time. As new people request a place they are added to the back of the queue and as people complete their purchases the next people are allowed in to buy tickets.

#### Process Backlogs

Some operations are inherently asynchronousor mechanical. For instance a printer maintains a queue of jobs that it need to process. When it recieves a new job it adds it to the queue but it must first process all other items in the queue before it can print the page sent to it.

Using a queue allows us to wait for the asynchronous behaviour to complete before a new job can be sent. Without this operations sent to the printer would instead fail if another operation was in progress, or worse change the operation mid-way.
