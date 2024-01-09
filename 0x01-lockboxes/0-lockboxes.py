#!/usr/bin/python3
"""Unlocking  Boxes"""


def canUnlockAll(boxes):
    keys = [0]
    opened_boxes = 0
    total_boxes = len(boxes)
    index = 0
    while index < len(keys):
        setkey = keys[index]
        for key in boxes[setkey]:
            if key < total_boxes and key not in keys and key > 0:
                keys.append(key)
                opened_boxes += 1
        index += 1
    if opened_boxes == total_boxes - 1:
        return True
    else:
        return False
