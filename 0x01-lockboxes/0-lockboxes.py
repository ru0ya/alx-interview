#!/usr/bin/python3
"""
function to determine whether an n number of locked boxes
can be opened: each box is numbered sequentially from 0
- n -1 and each box may contain keys to other boxes
"""


def canUnlockAll(boxes):
    """
    determines whether n boxes can be opened

    Parameters: boxes(list of lists)

    Returns: true if all boxes can be unlocked else false
    """
    n = len(boxes)  # number of boxes
    unlocked_boxes = [0]  # start with the first box unlocked
    keys_obtained = set([0])  # tracks obtained keys
    opened = set()  # tracks opened boxes

    while unlocked_boxes:
        current_box = unlocked_boxes.pop()  # get index of current box

        if current_box >= 0 and current_box < n:
            opened.add(current_box)  # add box to opened set

        for key in boxes[current_box]:
            if key < n:
                keys_obtained.add(key)  # add key to obtained keys set
                if key not in opened:
                    unlocked_boxes.append(key)  # add key to unlocked boxes list

    return len(opened) == n and len(keys_obtained) == n
