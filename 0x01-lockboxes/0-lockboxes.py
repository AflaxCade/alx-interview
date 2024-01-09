#!/usr/bin/python3
from collections import deque
"""method that determines if all the boxes can be opened"""

def canUnlockAll(boxes):
    if not boxes or len(boxes) == 1:
        return True

    keys = set(boxes[0])
    opened = {0}

    queue = deque([0])

    while queue:
        current_box = queue.popleft()

        for key in boxes[current_box]:
            if key not in opened:
                opened.add(key)
                queue.append(key)
                keys.update(boxes[key])

    return len(opened) == len(boxes)
