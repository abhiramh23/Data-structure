"""Stack implementation extending list"""


class Stack(list):
    """initializer"""

    def __init__(self):
        super().__init__()
        self.__top = -1  # Pointer to the top of the stack

    def isempty(self) -> bool:
        """Check if the stack is empty"""
        return len(self) == 0

    def push(self, data):
        """Add item"""
        self.append(data)
        self.__top += 1

    def pop(self):
        """Remove and return the top item. Return None if stack is empty."""
        if self.__top != -1:
            self.__top -= 1
            return super().pop()
        return

    def peek(self):
        """__Top"""
        return self.__top

    def size(self) -> int:
        """Return size of stack"""
        return self.__top + 1

    def __str__(self) -> str:
        return f"Stack: {list(self)}, Top: {self.__top}"

    # Disable other list methods
    def __getattribute__(self, name):
        if name in ["insert", "extend", "remove", "clear", "reverse", "sort"]:
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{name}'"
            )
        return super().__getattribute__(name)
