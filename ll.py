class Node(object):
    """A node object"""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return "<Node %s>" % (self.data)

class LinkedList(object):
    """A linked list object"""

    def __init__(self, head):
        self.head = head

    def __repr__(self):
        return "<LinkedList head=%s>" % (self.head)

    def traverse_list(self):
        current = self.head
        while current:
            print current.data
            current = current.next

