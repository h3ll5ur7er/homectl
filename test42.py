#! /usr/bin/env python3
try:
    from sys import argv
    print('hello from python: ', ", ".join(argv[1:]))
except Exception as e:
    print('hello from python', e)