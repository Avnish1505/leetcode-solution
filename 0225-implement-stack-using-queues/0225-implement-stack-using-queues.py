

class MyStack:

    def __init__(self):
        # Single Queue (Deque simulating standard FIFO queue)
        self.q = deque()

    def push(self, x: int) -> None:
        # Naya element peeche add karo
        self.q.append(x)
        
        # Pichle saare elements ko rotate karke naye element ke peeche daal do
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        # Front element ko remove karke return karo
        return self.q.popleft()

    def top(self) -> int:
        # Front element ko read karo without removing
        return self.q[0]

    def empty(self) -> bool:
        # Check karo agar queue khali hai
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()