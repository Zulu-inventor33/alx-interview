#!/usr/bin/python3
"""
Module for UTF-8 validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list of int): List of integers where each integer represents
                            1 byte of data (only the 8 least significant bits).

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes remaining in the current UTF-8 character
    num_bytes = 0

    # Masks to check the leading bits
    mask1 = 1 << 7    # 10000000
    mask2 = 1 << 6    # 01000000

    for byte in data:
        # Mask to get the 8 least significant bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Count the number of leading 1's to determine the byte size
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            if num_bytes == 0:
                continue

            # For 1 byte character, the count should be 1
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the byte starts with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrease the count of remaining bytes
        num_bytes -= 1

    return num_bytes == 0
