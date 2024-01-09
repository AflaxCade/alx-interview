#!/usr/bin/python3
"""Unlocking Boxes"""

def canUnlockAll(boxes):
    """
    take boxes
        create set of keys
            go to box0
                get all keys and add them setofkeys
            start opening boxes from setofkeys
                go to each box of each key
                    and take the keys from it and add them to set of keys
                keep loping through all setof keys
            ignore keys that dont have box
            track opening of boxes by a counter, if at end it
            equal to lentgh of boxes it mean all boxes unlock
            OPTIMIZE IDEA :
                if we add 0 to setofkeys at start, we dont need for in 23
    """
    keys = [0]
    opened_boxes = 0
    total_boxes = len(boxes)
    index = 0
    while index < len(keys):
        current_key = keys[index]
        for key in boxes[current_key]:
            if key < total_boxes and key not in keys and key > 0:
                keys.append(key)
                opened_boxes += 1
        index += 1
    if opened_boxes  == total_boxes - 1:
        return True
    else:
        return False
