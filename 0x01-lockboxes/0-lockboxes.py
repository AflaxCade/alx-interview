#!/usr/bin/python3
"""Unlocking  Boxes"""


def canUnlockAll(boxes):
    keys = [0]
    counter = 0
    total_boxes = len(boxes)
    index = 0
    while index < len(keys):
        setkey = keys[index]
        for key in boxes[setkey]:
            if key < total_boxes and key not in keys and key > 0:
                keys.append(key)
                counter += 1
        index += 1
    if counter == total_boxes - 1:
        return True
    else:
        return False
