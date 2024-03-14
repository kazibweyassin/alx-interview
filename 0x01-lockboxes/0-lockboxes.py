#!/usr/bin/python3
""" keys and lock boxes"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes in the list can be unlocked.

    Args:
        boxes (list): A list of lists representing the boxes and their corresponding keys.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    newlist = []
    k = len(boxes)
    for i in boxes:
        if len(i) == 0 and i is not boxes[k-1]:
            return False
        for j in i:
            newlist.append(j)
    print(newlist)
    for index, keys in enumerate(boxes):
        if index in newlist or index < k-1:
            return True
        else:
            return False
