import os
import random
import base64
import argparse

# define a function to rename files starting with specific characters
def rename_files_starting_with(folder, old_prefix, new_prefix):
    for file_name in os.listdir(folder):
        if file_name.startswith(old_prefix):
            # construct the full paths for the old and new file names
            old_path = os.path.join(folder, file_name)
            new_path = os.path.join(folder, file_name.replace(old_prefix, new_prefix, 1))
            
            # rename the file
            try:
                os.rename(old_path, new_path)
                print("Renamed: ", old_path, "->", new_path)
            except FileNotFoundError:
                print("Rename Failed: ", old_path)
                continue

# define command line arguments
parser = argparse.ArgumentParser(description='Mass Rename Files')
parser.add_argument('folder', metavar='FOLDER', type=str, help='path to the folder containing the files')
parser.add_argument('-p', '--pattern', metavar='PATTERN', type=str, default='file_', help='new file name pattern')
parser.add_argument('-r', '--random', action='store_true', help='rename files randomly')
parser.add_argument('-pf', '--prefix', metavar='PREFIX', type=str, default=None, help='rename files starting with the specified prefix')
parser.add_argument('-npf', '--new-prefix', metavar='NEW_PREFIX', type=str, default=None, help='new prefix to replace the old prefix')
args = parser.parse_args()

# rename files starting with the specified prefix, if the --prefix and --new-prefix flags are set
if args.prefix is not None and args.new_prefix is not None:
    rename_files_starting_with(args.folder, args.prefix, args.new_prefix)

# get a list of all the files in the folder
files = os.listdir(args.folder)

# shuffle the list of files randomly if the --random flag is set
if args.random:
    random.shuffle(files)

# iterate over each file in the folder
for index, file_name in enumerate(files):
    # get the file extension
    file_ext = os.path.splitext(file_name)[1]

    # encode the new file name using base64 with some random text
    new_file_name = args.pattern + base64.b64encode(os.urandom(10)).decode() + file_ext

    # construct the full paths for the old and new file names
    old_path = os.path.join(args.folder, file_name)
    new_path = os.path.join(args.folder, new_file_name)

    # rename the file
    try:
        os.rename(old_path, new_path)
        print("Renamed: ", old_path, "->", new_path)
    except FileNotFoundError:
        print("Rename Failed: ", old_path)
        continue