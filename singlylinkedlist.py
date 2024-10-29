""" Singly Linked List"""

from typing import Optional, TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    """Node class for singly linked list"""

    def __init__(self, item: Optional[T] = None, point=None):
        self.item: Optional[T] = item
        self.next: Optional[Node] = point


class SLL(Generic[T]):
    """Singly Linked List"""

    def __init__(self, head: Optional[Node] = None):
        self.head: Optional[Node] = head

    def isempty(self) -> bool:
        """Check if the list is empty"""
        return self.head is None

    def insert_at_start(self, data: T) -> None:
        """Insert data at the start of the list"""
        n = Node(item=data, point=self.head)
        self.head = n

    def find(self, key: T) -> Optional[Node]:
        """Search for a key in the list"""
        current: Optional[Node] = self.head
        while current is not None:
            if current.item == key:
                return current
            current = current.next
        return None

    def insert_after(self, key: T, data: T) -> None:
        """Insert data after a key in the list"""
        at: Optional[Node] = self.find(key=key)
        if at is not None:
            n = Node(item=data, point=at.next)
            at.next = n

    def insert_last(self, data: T) -> None:
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

    def delete_at_first(self) -> None:
        """Delete the first node in the list"""
        if self.isempty():
            pass
        else:
            n: Optional[Node] = self.head
            self.head = n.next  # type: ignore
            print(f"delete item {n.item}")  # type: ignore

    def delete_at_last(self) -> None:
        """Delete the last node in the list"""
        if self.head is None:
            pass
        elif self.head.next is None:
            self.head = None
        else:
            temp: Optional[Node] = self.head
            while temp.next.next is not None:  # type: ignore
                temp = temp.next  # type: ignore
            temp.next = None  # type: ignore

    def delete_item(self, key: T):
        """Delete a item"""
        if self.head is None:
            pass
        elif self.head.next is None:
            if self.head.item == key:
                self.head = None
        else:
            temp: Optional[Node] = self.head
            if temp.item == key:  # type: ignore
                self.head = temp.next  # type: ignore
            else:
                while temp.next is not None:  # type: ignore
                    if temp.next.item == key:  # type: ignore
                        temp.next = temp.next.next  # type: ignore
                        break
                    temp = temp.next  # type: ignore
