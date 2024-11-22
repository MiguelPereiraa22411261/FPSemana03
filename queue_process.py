from collections import deque

inputed = input()
words = inputed.split()
queue = deque(words)
print(f"deque({list(queue)[::-1]})")
while queue:
    word = queue.pop()
    if "o" in word:
        print(word)