#!/usr/bin/env python3
"""
Method that determines if a given data
set represents a valid UTF-8 validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents
    a valid UTF-8 encoding

    Arguments: data

    Returns: True if data is valid UTF-8 encoding
     else returns False
    """
    rem_byte = 0

    for byte in data:
        if rem_byte == 0:
            if byte & 0x80 == 0:
                # check if byte is a single-byte
                continue
            if byte & 0xE0 == 0xC0:
                # check if byte is start of two-byte character
                rem_byte = 1
            elif byte & 0xF0 == 0xE0:
                # check if byte is start of three-byte character
                rem_byte = 2
            elif byte & 0XF8 == 0xF0:
                # check if byte is start of four-byte character
                rem_byte = 3
            else:
                return False
        else:
            if byte & 0xC0 != 0x80:
                # check if byteis a subsequent byte of a multi-byte character
                return False
            rem_byte -= 1

    return rem_byte == 0
