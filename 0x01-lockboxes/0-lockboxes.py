#!/usr/bin/python3
"""Unlocking Boxes"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.
    
    Take a list of boxes containing keys.
    Start with key 0 and collect all available keys.
    Continue opening boxes using collected keys.
    Track the opening of boxes by a counter.
    If the counter reaches the total number of boxes, all boxes can be unlocked.
    Optimized idea: Adding 0 to keys initially eliminates the need for a separate loop.

    Args:
    - boxes: A list of lists, where each inner list contains keys to other boxes.

    Returns:
    - Boolean: True if all boxes can be unlocked, False otherwise.
    """
    keys = [0]
    opened_boxes = 0
    total_boxes = len(boxes)
    index = 0
    while index < len(keys):
        current_key = keys[index]
        for key in boxes[current_key]:
            if 0 < key < total_boxes and key not in keys:
                keys.append(key)
                opened_boxes += 1
        index += 1
    if opened_boxes == total_boxes - 1:
        return True
    else:
        return False
