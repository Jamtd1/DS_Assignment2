import unittest

class QueueItem:
    next = None
    previous = None

    def __init__(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

    def get_value(self):
        return self.value

    # This is returned when attempting to evaulate the class
    def __repr__(self):
        return str(self.value)

class myQueue:
    head = None
    tail = None

    # We do this here so we don't need to traverse the entire
    # linked list in order to get its length
    size = 0

    def enqueue(self, value):
        # if the tail is none, we create a new QueueItem
        # and set the head and tail to it
        # else we create a new item, set the current tails
        # next element to be it & then set tail to the new
        # item
        if (self.tail == None):
            self.head = QueueItem(value)
            self.tail = self.head
        else:
            self.tail.next = QueueItem(value)
            self.tail.next.previous = self.tail
            self.tail = self.tail.next

        self.size += 1


    def dequeue(self):
        if (self.head == None): return None

        # Get the value of the first element in the queue
        # and store it in a temporary parameter. Then set
        # the head to the next QueueItem and clear its
        # previous value
        head = self.head.get_value()
        self.head = self.head.get_next()
        if (self.head != None): self.head.previous = None

        self.size -= 1

        return head

    def top(self):
        return self.head.get_value()

    def is_empty(self):
        return self.head == None

    def get_size(self):
        return self.size;

    def __repr__(self):
        item = self.head
        items = []

        while item is not None:
            items.append(str(item.value))
            item = item.next

        items.append("None")
        return " -> ".join(items)


###############
#### TESTS ####
###############

class TestMyLinkedList(unittest.TestCase):
    def test_can_enqueue_to_queue(self):
        queue = myQueue()

        self.assertEqual(queue.head, None, "the was initialized correctly")

        queue.enqueue(1)

        self.assertEqual(queue.head.get_value(), 1, "the value was enqueueed to the queue")
        self.assertEqual(queue.tail.get_value(), 1, "the tail is the last value")

        queue.enqueue(2)

        self.assertEqual(queue.head.get_value(), 1, "the value was enqueueed to the queue")
        self.assertEqual(queue.tail.get_value(), 2, "the tail is still the last value")

    def test_can_dequeue_from_queue(self):
        queue = myQueue()

        queue.enqueue(1)
        queue.enqueue(2)

        self.assertEqual(queue.head.get_value(), 1, "the value was enqueueed to the queue")
        self.assertEqual(queue.tail.get_value(), 2, "the tail is correct")

        value = queue.dequeue()

        self.assertEqual(value, 1, "dequeue returns the value from the top of the queue")
        self.assertEqual(queue.head.get_value(), 2, "the head was dequeued from the queue")

    def test_can_retrieve_the_top_element_without_removing_it(self):
        queue = myQueue()

        queue.enqueue(1)

        self.assertEqual(queue.head.get_value(), 1, "the value was enqueueed to the queue")

        value = queue.top()

        self.assertEqual(value, 1, "dequeue returns the value from the top of the queue")
        self.assertEqual(queue.head.get_value(), 1, "the head was dequeued from the queue")

    def test_can_tell_if_queue_is_empty(self):
        queue = myQueue()

        self.assertEqual(queue.is_empty(), True, "is_empty returns true initially")

        queue.enqueue(1)

        self.assertEqual(queue.is_empty(), False, "is_empty returns false when items are in the queue")

        queue.dequeue()

        self.assertEqual(queue.is_empty(), True, "is_empty returns true once all queue items are removed")

    def test_size_is_reported_correctly(self):
        queue = myQueue()

        self.assertEqual(queue.get_size(), 0, "The size of the stack is correct")

        queue.enqueue(1)

        self.assertEqual(queue.get_size(), 1, "The size of the stack has increased")

        queue.dequeue()

        self.assertEqual(queue.get_size(), 0, "The size of the stack has decreased")

    def test_can_print_queue(self):
        queue = myQueue()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        self.assertEqual(str(queue), "1 -> 2 -> 3 -> None", "The queue is structured correctly")


if __name__ == "__main__":
    unittest.main()
