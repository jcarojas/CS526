#!/usr/bin/env python
# coding: utf-8

# In[9]:


import re
import sys


from problem2 import SinglyLinkedList

ARG_COUNTS = {
    "append": 1,
    "prepend": 1,
    "insert": 2,
    "get": 1,
    "find": 1,
    "len": 0,
    "update": 2,
    "delete": 1,
    "delete_at": 1,
    "print_list": 0,
}

WHOLE_NUMBER = re.compile(r"[+-]?\d+")


class DirectiveError(Exception):
    pass

def parse_index(token):
    if not WHOLE_NUMBER.fullmatch(token):
        raise DirectiveError(f"index '{token}' is not a whole number")
    return int(token)


def parse_value(token):
    return int(token) if WHOLE_NUMBER.fullmatch(token) else token


def execute(lst, directive, args):
    if directive == "append":
        lst.append(parse_value(args[0]))
    elif directive == "prepend":
        lst.prepend(parse_value(args[0]))
    elif directive == "insert":
        lst.insert(parse_index(args[0]), parse_value(args[1]))
    elif directive == "get":
        print(lst.get(parse_index(args[0])))
    elif directive == "find":
        print(lst.find(parse_value(args[0])))
    elif directive == "len":
        print(len(lst))
    elif directive == "update":
        lst.update(parse_index(args[0]), parse_value(args[1]))
    elif directive == "delete":
        if not lst.delete(parse_value(args[0])):
            raise DirectiveError(f"value '{args[0]}' is not in the list")
    elif directive == "delete_at":
        print(lst.delete_at(parse_index(args[0])))
    elif directive == "print_list":
        lst.print_list()


def warn(line_number, message):
    print(f"Warning (line {line_number}): {message}")


def main():
    lst = SinglyLinkedList()

    for line_number, raw in enumerate(sys.stdin, start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue

        directive, *args = line.split()

        if directive not in ARG_COUNTS:
            warn(line_number, f"unknown directive '{directive}'")
            continue

        expected = ARG_COUNTS[directive]
        if len(args) != expected:
            warn(
                line_number,
                f"'{directive}' expects {expected} argument(s), got {len(args)}",
            )
            continue

        try:
            execute(lst, directive, args)
        except DirectiveError as err:
            warn(line_number, str(err))
        except IndexError:
            warn(line_number, f"index out of range in '{line}'")
    
    print("Final list: ", end="")
    lst.print_list()


if __name__ == "__main__":
    main()

