#!python
#I used Faith's code as a referance, our code may be simular.


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.list_length = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        #O(1)
        return self.head is None

    def length(self):
        # O(1)
        # Normally O(n)
        return self.list_length

    def append(self, item):
        node = Node(item)
        # O(n)+1
        if self.tail is not None: #<--- this means self.tail is none
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.list_length += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # O(n)+1 Just like Append but uses .head insted of .tail
        node = Node(item)
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.list_length += 1

    def find(self, quality):
        # O(N+2) becuase we have one loop
        node = self.head
        while(node != None):
            if (quality(node.data)):
                return node.data
            node = node.next
        return None

    def delete(self, item):
        # Best case: O(n)--> obejct at begining of list
        # worst Case: O(n+2)  --> has a few checks
        previous = None
        found = False
        node = self.head
        while not found and node is not None:
            if node.data == item:
                # if we're not at the head, connect the previous node with the next one
                if previous is not None:
                    previous.next = node.next
                # if we ARE at the head, make the next node the head
                else:
                    self.head = node.next
                # if we're at the tail, point the tail to the previous node
                if node.next is None:
                    self.tail = previous
                self.list_length -= 1
                found = True
            previous = node
            node = node.next
        if not found:
            raise ValueError('Item not found: {}'.format(item))

    def replace(self, comparator, replacement):
    # Walk through list until we find the target, then replace the data
    # O(N) --> we have one loop in the function
        found = False
        node = self.head
        while not found and node is not None:
            if comparator(node.data) is True:
                node.data = replacement
                found = True
            node = node.next
        if not found:
            raise ValueError('Replacement target not found.')



def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
