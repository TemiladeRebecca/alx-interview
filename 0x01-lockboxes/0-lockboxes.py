#!/usr/bin/python3
"""
This method unlocks boxes, there are a number of boxes and each box numbered sequentially.
Each box contains keys to other boxes
"""


def canUnlockAll(boxes):
    """Function to unlock all boxes"""
    unlocked = [0]

    for box_index, box_elements in enumerate(boxes):
        # Enumerates and returns box indices and their corresponding
        # elements which are keys in this case
        if not box_elements:
            continue        # if the box has no keys or is empty

        for key in box_elements:
            if key < len(boxes) and key != box_index and key not in unlocked:
                unlocked.append(key)
                # the box is unlocked only if conditions are met

    if len(unlocked) == len(boxes):
        return True
    return False
