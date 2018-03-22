#!/usr/bin/env python3
"""Support the jmp command to provide the working jump-list."""
import argparse
import os
import os.path
import sys
import ntpath
 
FILENAME = "{0}/.jump_list.txt".format(os.environ["HOME"])
VERSION = "0.2"
 
def load_state():
    """Loads the jumplist file into a dictionary and returns it.
    Returns:
        dict: jumplist
    """
    jmp_list = dict()
    if os.path.isfile(FILENAME):
        with open(FILENAME) as jump_file:
            for line in jump_file.readlines():
                pieces = line.split(':')
                key, val = pieces[0], ':'.join(pieces[1:])
                if key.strip and val.strip:
                    jmp_list[key.strip()] = val.strip()
    return jmp_list
 
def write_state(jmp_list):
    """Writes the given dictionary to the jumplist file."""
    with open(FILENAME, 'w') as file_handler:
        for key, val in jmp_list.items():
            file_handler.write("{0}: {1}\n".format(key, val))
 
def path_leaf(path):
    """Returns the leaf portion of a path.
    Returns:
        string: last component of the given path
    """
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)
 
def list_items(jmp_list):
    """List all known jump locations."""
    if not jmp_list:
        print("no items in jump list")
        return 2
 
    maxLen = 0
    for key in jmp_list.keys():
        maxLen = max(len(key), maxLen)
    for key, val in jmp_list.items():
        print("{0: >{1}}: {2}".format(key, maxLen, val))
    return 4
 
def add_item_to_list(jmp_list, name):
    """Add the current working directory to the jump list."""
    path = os.getcwd()
    if not name:
        # use the folder name
        name = path_leaf(path)
    home = os.path.expanduser('~')
    if path.startswith(home):
        # use tilde to replace home folders
        path = '~' + path[len(home):]
    jmp_list[name] = path
    print("added {0}: '{1}'".format(name, path))
    write_state(jmp_list)
 
def remove_item_from_list(jmp_list, name):
    """Remove the name from the jump-list."""
    if not name:
        print("err: no name speficied")
        print("  jmp rm (name} : removes the name from the jump list")
 
    if name in jmp_list:
        del jmp_list[name]
        print("removed '{0}'".format(name))
        write_state(jmp_list)
    else:
        print("name '{0}' not found".format(name))
 
def main():
    """Main program."""
    parser = argparse.ArgumentParser(description='Maintains a jump-list.')
    parser.add_argument('-l', '--list', action='store_true', help='list items')
    parser.add_argument('-a', '--add', action='store_true',
                        help='add the current path as an item in the jump-list')
    parser.add_argument('-r', '--rm', action='store_true',
                        help='remove a named item from the jump-list')
    parser.add_argument('-v', '--version', action='store_true', help='print version')
    parser.add_argument('name', nargs='?', default='', help='the name of the item to jump to')
    args = parser.parse_args()
 
    # load the jump list
    jmp_list = load_state()
    if args.version:
        print("jmp: version: {0}".format(VERSION))
    elif args.list:
        list_items(jmp_list)
    elif args.add:
        add_item_to_list(jmp_list, args.name)
    elif args.rm:
        remove_item_from_list(jmp_list, args.name)
    elif len(sys.argv) > 1:
        if sys.argv[1] in jmp_list:
            # get the path
            path = os.path.expanduser(jmp_list[sys.argv[1]])
            # you would think we do this:
            #os.chdir(path)
            # but, we just return the path to the shell so the shell can actually change its path
            print("{0}".format(path))
            exit(0)
    exit(1)
 
if __name__ == "__main__":
    main()
