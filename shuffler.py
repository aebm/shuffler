#!/usr/bin/env python3

import argparse
import random
import sys

DESCRIPTION = '''Shuffle the arguments received, if called without arguments
                 the lines read from stdin will be shuffled and printed to
                 stdout'''


def get_list():
    return sys.stdin.readlines()


def print_list(list_):
    for elem in list_:
        print(elem.rstrip())


def main():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    (args, list_) = parser.parse_known_args()
    r = random.SystemRandom()
    if not list_:
        list_ = get_list()
    r.shuffle(list_)
    print_list(list_)


if __name__ == '__main__':
    main()
