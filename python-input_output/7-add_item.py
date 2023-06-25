#!/usr/bin/python3
""" Ex 7 """

from sys import argv as av
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


save_to_json_file(av[1:], "add_item.json")
print(load_from_json_file("add_item.json"))
