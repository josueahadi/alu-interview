# Rainwater Trapping Algorithm
## Problem Description
Given a list of non-negative integers representing the heights of walls with unit width 1, as if viewing the cross-section of a relief map, calculate how many square units of water will be retained after it rains.

## Constraints:

- The input `walls` is a list of non-negative integers.
- The ends of the list (before index 0 and after index walls[-1]) are not walls, meaning they will not retain water.
- If the list is empty, the function should return `0`.

## Algorithm: Two Pointers Approach
The algorithm uses the "Two Pointers" technique to efficiently calculate the amount of trapped water.

## Steps:

1. Initialize two pointers, `left` and `right`, at the start and end of the list respectively.
2. Initialize variables to keep track of the maximum height seen from both left (`left_max`) and right (`right_max`).
3. Initialize a variable `water` to store the total amount of trapped water.
4. While the left pointer is less than the right pointer:
    <br>
    >a. Compare the heights of the walls at the left and right pointers.<br>
    b. Move the pointer pointing to the smaller wall inward.<br>
    c. Update the maximum height for that side if necessary.<br>
    d. Calculate the water trapped above the current wall and add it to the total.<br>
5. Return the total amount of trapped water.

## Implementation
```python
def rain(walls):
    if not walls:
        return 0
    
    left, right = 0, len(walls) - 1
    left_max = right_max = water = 0
    
    while left < right:
        if walls[left] < walls[right]:
            if walls[left] >= left_max:
                left_max = walls[left]
            else:
                water += left_max - walls[left]
            left += 1
        else:
            if walls[right] >= right_max:
                right_max = walls[right]
            else:
                water += right_max - walls[right]
            right -= 1
    
    return water
```
## Complexity Analysis

- **Time Complexity: O(n)**, where n is the number of walls. We traverse the list once with two pointers.
- **Space Complexity: O(1)**, as we only use a constant amount of extra space regardless of the input size.

## Example Usage
```python
walls = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(rain(walls))  # Output: 6
```
## Explanation
The algorithm works by understanding that the amount of water that can be trapped above any wall depends on the minimum of the maximum heights to its left and right.
By using two pointers and keeping track of the maximum heights from both ends, we can calculate the water trapped at each position in a single pass through the list. This approach is more efficient than calculating left and right max heights for each position separately.