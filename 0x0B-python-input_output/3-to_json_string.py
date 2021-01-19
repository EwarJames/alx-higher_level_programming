#!/usr/bin/python3
"""Define a function that returns a json."""
import json


def to_json_string(my_obj):
    """
    Function that convert json to a string.

    Args:
       my_obj (str): Object to be converted.

    Return:
        JSON representation of an object (string)
    """
    return json.dumps(my_obj)
