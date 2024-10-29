"""Stack implementation using list"""

from typing import TypeVar, List, Generic


T = TypeVar("T")


class Stack(Generic[T]):

    def __init__(self, item: T) -> None:
        self.items: T = item

    def display(self):
        return self.items


s = Stack([1, 2, 3, 4])
