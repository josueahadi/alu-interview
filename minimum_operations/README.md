# Minimum Operations to Reach 'H' Characters

## Overview

This script provides a Python function that calculates the minimum number of operations needed to reach exactly `n` **H** characters in a text file. The file starts with a single 'H' and supports only two operations: Copy All and Paste.

## Problem Description

Given an integer `n`, the task is to determine the minimum number of operations needed to achieve exactly `n` 'H' characters in a file, starting with a single 'H'. The only allowed operations are:

- **Copy All**: Copy all 'H' characters in the file.
- **Paste**: Paste the copied content back into the file.

For example, to get 9 'H' characters:

1. Start with `H`
2. Perform Copy All
3. Perform Paste to get `HH`
4. Perform Paste again to get `HHH`
5. Perform Copy All
6. Perform Paste to get `HHHHHH`
7. Perform Paste again to get `HHHHHHHHH`
8. Perform Copy All
9. Perform Paste to get `HHHHHHHHHHH`

The total number of operations required is 6.

## Function

The core functionality is provided by the `minOperations` function, which calculates the fewest number of operations needed to get exactly `n` 'H' characters.

### Function Signature

```python
def minOperations(n: int) -> int:
```
