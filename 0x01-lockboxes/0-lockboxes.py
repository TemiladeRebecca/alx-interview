#!/usr/bin/python3
"""
This method unlocks boxes, there are a number of boxes and each box numbered sequentially.
Each box contains keys to other boxes
"""

def canUnlockAll(boxes):
    unlocked = set([0])  # Use a set for faster membership testing

    for box_index, box_elements in enumerate(boxes):
        if not box_elements:
            continue

        unlocked |= set(box_elements) & set(range(len(boxes))) - {box_index}
        # Combine the sets to update unlocked indices efficiently

    return len(unlocked) == len(boxes)
