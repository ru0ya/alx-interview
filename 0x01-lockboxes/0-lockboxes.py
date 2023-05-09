#!/usr/bin/python3
"""
function to determine whether an n number of locked boxes
can be opened: each box is numbered sequentially from 0
- n -1 and each box may contain keys to other boxes
"""


def canUnlockAll(boxes):
    """
    determines whether n boxes can be opened

    Parameters: boxes

    Returns: true if all boxes can be unlocked
    """
    n = len(boxes)
    unlocked_boxes = [0]  # start with the first box unlocked

    for box in unlocked_boxes:
        for key in boxes[box]:
            if key not in unlocked_boxes:
                unlocked_boxes.append(key)

    return len(unlocked_boxes) == n
