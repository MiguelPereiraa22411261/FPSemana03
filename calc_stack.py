from collections import deque

inputed = input()
numbers = list(map(int, inputed.split()))
stack = deque(numbers)
print(stack)
while stack:
    number = stack.pop()
    print(number ** 2)