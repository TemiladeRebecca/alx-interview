#!/usr/bin/python3
"""
Function that unlocks boxes, each box contains a list of keys
that can open other boxes
"""


def canUnlockAll(boxes):
    """Function to unlock all boxes"""
    unlocked = [0]

    for box_index, box_elements in enumerate(boxes):
        # Enumerates and returns box indices and their corresponding
        # elements which are keys in this case
        if not box_elements:
            continue        # if the box has no keys/empty, we continue

        for key in box_elements:
            if key < len(boxes) and key != box_index and key not in unlocked:
                unlocked.append(key)
                # unlocks boxes only if conditions are met

    if len(unlocked) == len(boxes):
        return True
    return False
