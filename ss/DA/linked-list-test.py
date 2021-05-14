import unittest

class LinkedListItem:
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


class myLinkedList:
    def __init__(self):
        self.head = None

    def get_tail(self):
        # Get the current head which we will use to
        # traverse the list of items in the list
        item = self.head

        # We are after the second last item in this case
        # as the None value is only there to tell us we
        # have reached the end of the list
        while item.next is not None:
            item = item.next

        # Return the second last item, i.e the tail
        return item

    def get_head(self):
        return self.head

    def add_first(self, value):
        self.head = LinkedListItem(value, self.head)

    def add_last(self, value):
        # Find the second last element in the list and
        # set it's value to a new LinkedListItem. It is
        # important that the new "tail" was a next value
        # of None so we know it's the last element in the
        # list
        item = self.get_tail()
        item.next = LinkedListItem(value, None)

    def remove_first(self):
        # Set the head to be the list item that is next
        # of the current head
        self.head = self.head.next

    def list_traversal(self):
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
    def test_can_add_to_the_list(self):
        linked_list = myLinkedList()

        self.assertEqual(linked_list.get_head(), None, "The head of the linked_list was initialized")

        linked_list.add_first(1)

        self.assertEqual(linked_list.get_head().get_value(), 1, "The head of the linked_list was updated")

    def test_can_add_to_the_end_of_the_list(self):
        linked_list = myLinkedList()

        self.assertEqual(linked_list.get_head(), None, "The head of the linked_list was initialized")

        linked_list.add_first(1)
        linked_list.add_last(2)

        self.assertEqual(linked_list.get_head().get_value(), 1, "The head of the linked_list was updated")
        self.assertEqual(linked_list.get_tail().get_value(), 2, "The tail of the linked_list was updated")

    def test_can_remove_from_the_list(self):
        linked_list = myLinkedList()

        self.assertEqual(linked_list.get_head(), None, "The head of the linked_list was initialized")

        linked_list.add_first(1)

        self.assertEqual(linked_list.get_head().get_value(), 1, "The head of the linked_list was updated")

        linked_list.remove_first()

        self.assertEqual(linked_list.get_head(), None, "The head of the linked_list was initialized")

    def test_can_traverse_the_list(self):
        linked_list = myLinkedList()

        linked_list.add_first(1)
        linked_list.add_first(2)
        linked_list.add_first(3)

        self.assertEqual(linked_list.list_traversal(), "3 -> 2 -> 1 -> None", "The list is traversed correrctly")

if __name__ == "__main__":
    unittest.main()
