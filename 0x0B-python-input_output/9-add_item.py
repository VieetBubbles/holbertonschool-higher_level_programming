#!/usr/bin/python3
"""
The 9-add_item module.
"""


from sys import argv
from os import path

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

args = argv[1:]
new_list = []

if path.exists("add_item.json"):
    new_list = load_from_json_file("add_item.json")

new_list += args
save_to_json_file(new_list, "add_item.json")
