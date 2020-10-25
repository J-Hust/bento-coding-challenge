import os
import glob


def print_files_by_size(path):
    files = []
    subfolders = []
    for entry in os.scandir(path):
        try:
            is_dir = entry.is_dir(follow_symlinks=False)
        except OSError as e:
            print(e)
            continue
        if is_dir:
            subfolders.append(entry.path)
        else:
            try:
                if not entry.name.startswith('.'):
                    files.append([entry.path, entry.name, entry.stat(follow_symlinks=False).st_size])
            except OSError as e:
                print(e)

    return files


def using_walk(path):
    for cur, _dirs, files in os.walk(path):
        pass

def scandir_again(path):
    for entry in os.scandir(path):
        if entry.is_dir:
            scandir_again(path)
        print(entry.path)

def try_glob(path):
    for filename in glob.iglob(path + '**/**', recursive=True):
        print(filename)

print(try_glob('/home/justin/test/'))