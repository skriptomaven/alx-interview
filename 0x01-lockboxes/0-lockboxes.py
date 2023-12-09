#!/usr/bin/python3
"""Lockboxes method module
"""


def canUnlockAll(boxes):
    """Determines if all boxes can be opened.
    """
    if type(boxes) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    for i in range(1, len(boxes) - 1):
        checked_box = False
        for j in range(len(boxes)):
            checked_box = i in boxes[j] and i != j
            if checked_box:
                break
            if checked_box is False:
                return checked_box
    return True
