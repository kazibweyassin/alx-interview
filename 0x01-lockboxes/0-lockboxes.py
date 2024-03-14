#!/usr/bin/python3
def canUnlockAll(boxes):
    """Determine if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing the lockboxes and their corresponding keys.

    Returns:
        bool: True if all the boxes can be opened, False otherwise.
    """
    keys = [0]
    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys and new_key < len(boxes):
                keys.append(new_key)
    return len(keys) == len(boxes)