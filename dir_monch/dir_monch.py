#!/usr/bin/env python 
'''
dir_monch: a utility to help shorten paths.
'''

from os.path import expanduser
from os import sep as os_sep
from sys import exit
import sys

def dir_monch(path):
    # Substitute ~ for the home dir path when possible
    HOME = expanduser("~")
    if path.startswith(HOME):
        path = path.replace(HOME, '~', 1)

    MAX_PATH_LENGTH = 20
    if len(path) < MAX_PATH_LENGTH:
        return path
    
    split_path = path.split(os_sep)

    shortened_path = []
    for directory in split_path:
        end_idx = 1
        short_name = directory[0:end_idx]
        while (short_name in shortened_path) and end_idx < len(directory):
            end_idx += 1
            short_name = directory[0:end_idx]
        shortened_path.append(short_name)

    final_path = ''
    for short_dir in shortened_path[0:-1]:
        final_path += short_dir + os_sep

    final_path += split_path[-1]
    return final_path

def run_tests():
    test_paths = ['/Users/shiva', '/Users/shiva/git', '/Users/shiva/anaconda2/bin/Assistant.app', \
                  '/etc/apache2/extra', '/bin', '/', '/A/A/A/A/A/A/A/A', 'aaa/aaa/aaa/aaa/aaa/', \
                  '/Users/shiva/this\ folder\ has\ spaces/folder']

    expected_outputs = ['~', '~/git', '~/a/b/Assistant.app', '/etc/apache2/extra', '/bin', \
                        '/', '/A/A/A/A/A/A/A/A', 'a/aa/aaa/aaa/aaa/', '~/t/folder']
    for input_str, expected_str in zip (test_paths, expected_outputs):
        output = dir_monch(input_str)
        assert output == expected_str

if __name__ == '__main__':
    print dir_monch(sys.argv[1])
    exit(0)
