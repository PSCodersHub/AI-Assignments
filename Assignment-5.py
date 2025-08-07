# 1. write a program to implement stack using list in python.

stack = []

# Push operation
def push(item):
    stack.append(item)
    print(f"Pushed {item} to stack.")

# Pop operation
def pop():
    if is_empty():
        print("Stack is empty. Cannot pop.")
        return None
    item = stack.pop()
    print(f"Popped {item}")
    return item

# Peek operation
def peek():
    if is_empty():
        print("Stack is empty. Nothing to peek.")
        return None
    print(f"Top element is {stack[-1]}")
    return stack[-1]

# Check if stack is empty
def is_empty():
    return len(stack) == 0

# Get current size of the stack
def size():
    return len(stack)

# Display stack
def display():
    print("Current Stack:", stack)

# Example usage of all functions
push(5)
push(10)
push(15)
display()
peek()
print("Is stack empty?", is_empty())
print("Stack size:", size())
pop()
display()
pop()
pop()
print("Is stack empty after popping all?", is_empty())
pop()  # Try popping from empty stack

'''OUTPUT
Pushed 5 to stack.
Pushed 10 to stack.
Pushed 15 to stack.
Current Stack: [5, 10, 15]
Top element is 15
Is stack empty? False
Stack size: 3
Popped 15
Current Stack: [5, 10]
Popped 10
Popped 5
Is stack empty after popping all? True
Stack is empty. Cannot pop.
'''




# 2. write a program to implement queue using python.

queue = []

# Enqueue operation: add item at the end of the queue
def enqueue(item):
    queue.append(item)
    print(f"Enqueued {item}")

# Dequeue operation: remove item from the front of the queue
def dequeue():
    if is_empty():
        print("Queue is empty. Cannot dequeue.")
        return None
    item = queue.pop(0)
    print(f"Dequeued {item}")
    return item

# Peek operation: get the front item without removing it
def peek():
    if is_empty():
        print("Queue is empty. Nothing to peek.")
        return None
    print(f"Front element is {queue[0]}")
    return queue[0]

# Check if queue is empty
def is_empty():
    return len(queue) == 0

# Get current size of the queue
def size():
    return len(queue)

# Display the queue
def display():
    print("Current Queue:", queue)

# Example usage
enqueue(10)
enqueue(20)
enqueue(30)
display()
peek()
dequeue()
display()
print("Is queue empty?", is_empty())
print("Queue size:", size())

'''OUTPUT
Enqueued 10
Enqueued 20
Enqueued 30
Current Queue: [10, 20, 30]
Front element is 10
Dequeued 10
Current Queue: [20, 30]
Is queue empty? False
Queue size: 2
'''





# 3. write a program to implement dequeue using python.

# Implementing deque using a list
dq = []

# Add item to the right end
def add_right(item):
    dq.append(item)
    print(f"Added {item} to the right.")

# Add item to the left end
def add_left(item):
    dq.insert(0, item)
    print(f"Added {item} to the left.")

# Remove item from the right end
def remove_right():
    if is_empty():
        print("Deque is empty. Cannot remove from right.")
        return None
    item = dq.pop()
    print(f"Removed {item} from the right.")
    return item

# Remove item from the left end
def remove_left():
    if is_empty():
        print("Deque is empty. Cannot remove from left.")
        return None
    item = dq.pop(0)
    print(f"Removed {item} from the left.")
    return item

# Check if deque is empty
def is_empty():
    return len(dq) == 0

# Display the current deque
def display():
    print("Current Deque:", dq)


# Example usage:
add_right(10)
add_right(20)
add_left(5)
display()

remove_left()
display()

remove_right()
display()

print("Is deque empty?", is_empty())


'''OUTPUT
Added 10 to the right.
Added 20 to the right.
Added 5 to the left.
Current Deque: [5, 10, 20]
Removed 5 from the left.
Current Deque: [10, 20]
Removed 20 from the right.
Current Deque: [10]
Is deque empty? False
'''
