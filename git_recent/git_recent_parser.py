#!/usr/bin/env python
'''
git_recent_parser: a utility to parse the output of git_recent and provide the
selected branch.
'''

import sys


def git_recent_parser(line):
    if not line:
        return None

    words = line.split()

    if len(words) < 2:
        return words[0]

    # Handle cases where the current git branch line starts with a "*":
    if words[0] == "*":
        return words[1]
    else:
        return words[0]


def run_tests():
    test_paths = [
        'branch - description - 1234',
        'branch',
        '* branch',
        "feature/abc - 123abcd45 - Commit description goes here - User Name (2 days ago)",
        '',
    ]

    expected_outputs = [
        'branch',
        'branch',
        'branch',
        'feature/abc',
        None,
    ]

    for input_str, expected_str in zip(test_paths, expected_outputs):
        output = git_recent_parser(input_str)
        assert output == expected_str, "Input: {}, Expected output: {}".format(
            input_str, expected_str)
    print("All tests have passed!")
    sys.exit(0)


if __name__ == '__main__':
    for line in sys.stdin:
        print("git checkout {}".format(git_recent_parser(line)))
    # run_tests()
    sys.exit(0)
