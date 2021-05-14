import unittest

class StackItem:
    # Setup the initial values with the Next list item
    # being blank & setting the passed in value.
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def get_next(self):
        return self.next

    def get_value(self):
        return self.value

    # This is returned when attempting to evaulate the class
    def __repr__(self):
        return str(self.value)

class myStack:
    def __init__(self):
        self.head = None

    def push(self, value):
        self.head = StackItem(value, self.head)

    def pop(self):
        head = self.head.get_value()
        self.head = self.head.get_next()
        return head

    def top(self):
        return self.head.get_value()

    def isEmpty(self):
        return self.head == None

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
    def test_can_push_to_stack(self):
        stack = myStack()

        self.assertEqual(stack.head, None, "the was initialized correctly")

        stack.push(1)

        self.assertEqual(stack.head.get_value(), 1, "the value was pushed to the stack")

        stack.push(2)

        self.assertEqual(stack.head.get_value(), 2, "the value was pushed to the stack")

    def test_can_remove_from_stack(self):
        stack = myStack()

        stack.push(1)

        self.assertEqual(stack.head.get_value(), 1, "the value was pushed to the stack")

        value = stack.pop()

        self.assertEqual(value, 1, "pop returns the value from the top of the stack")
        self.assertEqual(stack.head, None, "the head was popped from the stack")

    def test_can_retrieve_the_top_element_without_removing_it(self):
        stack = myStack()

        stack.push(1)

        self.assertEqual(stack.head.get_value(), 1, "the value was pushed to the stack")

        value = stack.top()

        self.assertEqual(value, 1, "pop returns the value from the top of the stack")
        self.assertEqual(stack.head.get_value(), 1, "the head was popped from the stack")

    def test_can_check_for_empty(self):
        stack = myStack()

        self.assertEqual(stack.head, None, "the was initialized correctly")
        self.assertEqual(stack.isEmpty(), True, "the stack is empty")

        stack.push(1)

        self.assertEqual(stack.head.get_value(), 1, "the value was pushed to the stack")
        self.assertEqual(stack.isEmpty(), False, "the stack is not empty")



    def test_can_print_stack(self):
        stack = myStack()

        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(str(stack), "3 -> 2 -> 1 -> None", "The stack is structured correctly")


if __name__ == "__main__":
    unittest.main()
