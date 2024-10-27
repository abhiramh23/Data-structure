""" Singly Linked List"""

from typing import Optional, Any


class Node:
    """Node class for singly linked list"""

    def __init__(self, item: Any = None, point=None):
        self.item: Any = item
        self.next: Optional[Node] = point


class SLL:
    """Singly Linked List"""

    def __init__(self, head: Optional[Node] = None):
        self.head: Optional[Node] = head

    def isempty(self) -> bool:
        """Check if the list is empty"""
        return self.head is None

    def insert_at_start(self, data: Any) -> None:
        """Insert data at the start of the list"""
        n = Node(item=data, point=self.head)
        self.head = n

    def search(self, key: Any) -> Optional[Node]:
        """Search for a key in the list"""
        current: Optional[Node] = self.head
        while current is not None:
            if current.item == key:
                return current
            current = current.next
        return None

    def insert_after(self, key: Any, data: Any) -> None:
        """Insert data after a key in the list"""
        at: Optional[Node] = self.search(key=key)
        if at is not None:
            n = Node(item=data, point=at.next)
            at.next = n

    def insert_last(self, data: Any) -> None:
        """Insert data at the end of the list"""
        n = Node(item=data)
        if not self.isempty():
            temp: Node = self.head  # type: ignore
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.head = n

    def display(self) -> None:
        """Display the list"""
        temp: Optional[Node] = self.head
        while temp:
            print(temp.item, end=" ")
            temp = temp.next
        print()
