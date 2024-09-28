#!/usr/bin/python3

def rain(walls):
    """
    Calculate the amount of rainwater that can be trapped between walls.
    Args:
    walls (list of int): List of non-negative integers representing wall heights.
    Returns:
    int: Total amount of rainwater that can be trapped.
    """
    # Check if the input list is empty
    if not walls:
        return 0
    # Initialize pointers to the start and end of the list
    left, right = 0, len(walls) - 1
    # Initialize variables to track maximum heights and total water
    left_max = right_max = water = 0
    # Continue until the two pointers meet
    while left < right:
        # Compare the heights of the walls at the left and right pointers
        if walls[left] < walls[right]:
            # If the left wall is smaller, focus on the left side
            if walls[left] >= left_max:
                # Update the maximum height on the left side
                left_max = walls[left]
            else:
                # Calculate water trapped above current wall and add to total
                water += left_max - walls[left]
            # Move left pointer inward
            left += 1
        else:
            # If the right wall is smaller or equal, focus on the right side
            if walls[right] >= right_max:
                # Update the maximum height on the right side
                right_max = walls[right]
            else:
                # Calculate water trapped above current wall and add to total
                water += right_max - walls[right]
            # Move right pointer inward
            right -= 1
     # Return the total amount of trapped water
    return water
