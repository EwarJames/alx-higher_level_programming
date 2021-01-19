#!/usr/bin/python3
"""Defines a function converts JSON files to string object"""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON"""
    return json.loads(my_str)
