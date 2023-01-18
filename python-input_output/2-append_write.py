#!/usr/bin/python3
"""write a file"""


def append_file(filename="", text=""):
    """write"""
    if filename:
        with open(filename, mode='a', encoding="utf-8") as f:
            return (f.write(text))
