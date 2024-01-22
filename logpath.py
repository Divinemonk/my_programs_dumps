import os
import argparse
import time
import math

def create_directory_tree(root_path, log_file):
    with open(log_file, 'w') as log:
        log.write(f"[L0GP4TH] ROOT DIRECTORY: {root_path}\n") # write the root directory path (input by user)
        for root, dirs, files in os.walk(root_path):
            if root_path == '/':
                level = root.count(os.sep)
            else:
                level = root.replace(root_path, '').count(os.sep)
            indent = ' ' * 4 * (level)
            log.write('{}{}/\n'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                log.write('{}{}\n'.format(subindent, f))

def search_in_log(log_file, search_query):
    result = []
    with open(log_file, 'r') as log:
        lines = log.readlines()
        root_directory = lines[0].strip()
        for line in lines[1:]:
            if search_query.lower() in line.lower():
                line_index = lines.index(line)
                path = line
                result.append([path, line_index])
    return result

def print_indented_path(log_file, root_directory, results):
    with open(log_file, 'r') as log:
        lines = log.readlines()
        for result in results:
            try: indents = int(result[0].count(' ') / 4)
            except: continue
            path = result[0].strip()
            full_path = root_directory
            # going in reverse order to get the parent directories (parent has less indents than child)
            if indents == 1:
                full_path += path
            else:
                # search line with less indents from bottom to top compared to current line (indents - 1)
                sub_paths = ''
                while indents > 1:
                    indents -= 1
                    for line in reversed(lines[:result[1]]):
                        if line.count(' ') / 4 == indents:
                            sub_paths = line.strip() + sub_paths
                            break
                full_path += sub_paths + path
            ftype = '  [DIR ]' if path.endswith('/') else '  [FILE]'
            print(ftype, full_path)

def get_file_size(file_path):
    try:
        size = os.path.getsize(file_path)
        return size
    except FileNotFoundError:
        print("[L0GP4TH (err)] FILE NOT FOUND")

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0 B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

def display_help():
    help_msg = '''Welcome to logpath - your directory tree logger and searcher!
    \nUsage:
    python3 logpath.py -g -f custom_log_filename
    python3 logpath.py -q search_query -f custom_log_filename
    [default log filename is `directory_tree_log.txt` if `-f` is not specified]
    \nOptions:
    -h, --help        Display this help message
    -g, --generate    Generate directory tree log
    -f, --filename    Specify custom log file name (default is directory_tree_log.txt)
    -q, --query       Search for a file/folder and get its absolute path'''
    print(help_msg)

def main():
    parser = argparse.ArgumentParser(description="Welcome to logpath - your directory tree logger and searcher!")
    parser.add_argument('-g', '--generate', help="Generate directory tree log", action="store_true")
    parser.add_argument('-f', '--filename', help="Specify custom log file name (default is directory_tree_log.txt, optional)")
    parser.add_argument('-q', '--query', help="Search for a file/folder and get its absolute path")

    args = parser.parse_args()

    if not any(vars(args).values()):
        display_help()
        return

    if args.generate:
        root_directory = input("[L0GP4TH] ENTER THE 'ROOT DIRECTORY' PATH: ")
        if root_directory == '': # if user enters blank, set root directory to '/'
            root_directory = '/'
        if not os.path.exists(root_directory):
            print("[L0GP4TH (err)] ENTERED ROOT DIRECTORY DOES NOT EXIST")
            return
        start_time = time.time() # start timer
        root_directory = root_directory.rstrip('/') + '/'
        log_filename = args.filename if args.filename else "directory_tree_log.txt"
        create_directory_tree(root_directory, log_filename)
        print(f"[L0GP4TH] DIRECTORY TREE LOG GENERATED AT: ./{log_filename}")
        print(f"[L0GP4TH] GENERATED {convert_size(get_file_size(log_filename))} BYTES FILE IN {(time.time() - start_time):.2f} SECS")

    if args.query:
        start_time = time.time() # start timer
        search_query = args.query
        log_filename = args.filename if args.filename else "directory_tree_log.txt"

        with open(log_filename, 'r') as log:
            lines = log.readlines()
            root_directory = lines[0].split(":")[1].strip().rstrip('/') + '/'

        search_result = search_in_log(log_filename, search_query)

        if search_result:
            print(f"[L0GP4TH] SEARCH RESULTS FOR '{search_query}':")
            print_indented_path(log_filename, root_directory, search_result)
            print(f"[L0GP4TH] ABOUT {len(search_result)} RESULTS FOUND IN {(time.time() - start_time):.2f} SECS")
        else:
            print("[L0GP4TH (err)] NO MATCHING RESULTS FOUND")

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: print("\n[L0GP4TH (exit)] PROGRAM TERMINATED AS PER USER'S REQUEST")


# for search query
# - add display only files or only directories option (-file, -dir)
# - add display only files with certain extension option (-ext)
# - add search for files from perticular location option (-loc)
