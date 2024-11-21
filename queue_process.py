from collections import deque

inputed = input()
words = inputed.split()
queue = deque(words)
print(queue)
while queue:
    word = queue.popleft()
    if "o" in word:
        print(word)