from typing import Any


# Stack data structure


class Stack:
    def __init__(self):
        self.values: list[Any] = []

    def push(self, item: Any) -> None:
        self.values.append(item)

    def pop(self) -> Any:
        return self.values.pop()

    def peek(self) -> [Any]:
        if not self.is_empty():
            return self.values[-1]
        else:
            print('Empty stack')

    def is_empty(self) -> bool:
        return not bool(self.values)

    def size(self) -> int:
        return len(self.values)


s = Stack()
s.peek()
print(s.is_empty())
s.push('cat')
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.is_empty())
s.push(777)
print(s.values)
print(s.pop())
print(s.pop())
print(s.size())
