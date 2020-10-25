import os


files = []
def get_files_by_size(path):
    for entry in os.scandir(path):
        try:
            is_dir = entry.is_dir(follow_symlinks=False)
        except OSError as e:
            print(e)
            continue
        if is_dir:
            get_files_by_size(entry.path)
        else:
            try:
                if not entry.name.startswith('.'):
                    files.append([entry.path, entry.name, entry.stat(follow_symlinks=False).st_size])
            except OSError as e:
                print(e)

    # sort by size, then path
    sorted_files = sorted(files, key=lambda x: (x[2], x[0]))
    return sorted_files

def format_size(number):
    sizes = ['B', 'KB', 'MB', 'GB', 'TB']
    i = 0
    converted = number
 
    while number >= 1024 and i < len(sizes):
        converted = number/1024.0
        i += 1
        number = number/1024
 
    return str(round(converted, 2)) + " " + sizes[i]

def nice_table(data):
    columns = ['Path', 'Name', 'Size']
    print("{:<80} {:<10} {:<10}".format(*columns))
    for row in data:
        print("{:<80} {:<10} {:<10}".format(row[0], row[1], format_size(row[2])))


# nice_table([['one', 'two', 3333], ['four', 'five', 666]])



nice_table(get_files_by_size('/home/justin/test/'))