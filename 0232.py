class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        temp = []
        while self.stack: temp.append(self.stack.pop())
        r = temp.pop()
        while temp: self.stack.append(temp.pop())
        return r

    def peek(self) -> int:
        """
        Get the front element.
        """
        temp = []
        while self.stack: temp.append(self.stack.pop())
        r = temp[-1]
        while temp: self.stack.append(temp.pop())
        return r

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack