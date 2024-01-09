#!/usr/bin/python3
"""Unlocking Boxes"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.
    
    Take a list of boxes containing keys.
    Start with key 0 and collect all available keys.
    Continue opening boxes using collected keys.
    Track the opening of boxes by a counter.
    """
    setofkeys = [0]
    counter = 0
    total_boxes = len(boxes)
    index = 0
    while index < len(setofkeys):
        setkey = setofkeys[index]
        for key in boxes[setkey]:
            if key < total_boxes and key not in setofkeys and key > 0:
                setofkeys.append(key)
                counter += 1
        index += 1
    if counter == total_boxes - 1:
        return True
    else:
        return False
