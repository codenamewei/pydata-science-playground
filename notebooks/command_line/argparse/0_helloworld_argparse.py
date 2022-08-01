
import argparse

import os
import sys


"""
python 0_helloworld_argparse.py Path helloworld
"""


if __name__ == "__main__":
    
    # Create the parser
    my_parser = argparse.ArgumentParser(description='List the content of a folder')

    # Add the arguments
    my_parser.add_argument('--path',
                           type=str,
                           help='the path to list')

    # Execute the parse_args() method
    args = my_parser.parse_args()

    input_path = args.path

    if not os.path.isdir(input_path):
        print('The path specified does not exist')
        sys.exit()

    print('\n'.join(os.listdir(input_path)))