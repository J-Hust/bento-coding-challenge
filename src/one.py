import os


files = []
def get_files_by_size(path):
    for entry in os.scandir(path):
        try:
            is_dir = entry.is_dir(follow_symlinks=False)
        except OSError as e:
            print(e)
            continue
        except FileNotFoundError as e:
            return e.strerror
        if is_dir:
            get_files_by_size(entry.path)
        else:
            try:
                if not entry.name.startswith('.'):
                    files.append([entry.path, entry.name, entry.stat(follow_symlinks=False).st_size])
            except OSError as e:
                print(e)

    # sort by size descending, then path
    sorted_files = sorted(files, key=lambda x: (x[2], x[0]), reverse=True)
    return sorted_files

def format_size(number):
    sizes = ['B', 'KB', 'MB', 'GB', 'TB']
    i = 0
    converted = number
 
    while number >= 1024 and i < len(sizes):
        converted = number/1024.0
        i += 1
        number = number/1024
 
    return str(round(converted, 2)) + ' ' + sizes[i]

def nice_table(data):
    if not len(data):
        print('no files found for given path')
    else:
        columns = ['Path', 'Name', 'Size']
        col_one_length = len(max(data, key=lambda x: len(x[0]))[0])
        col_two_length = len(max(data, key=lambda x: len(x[1]))[1])
        col_three_length = len(str(max(data, key=lambda x: len(str(x[2])))[2]))

        print('{:<{col_one_length}} {:{col_two_length}} {:<{col_three_length}}'.format(*columns, 
                                                                                        col_one_length=col_one_length, 
                                                                                        col_two_length=col_two_length, 
                                                                                        col_three_length=col_three_length))
        for row in data:
            print('{:<{col_one_length}} {:{col_two_length}} {:<{col_three_length}}'.format(row[0], row[1], format_size(row[2]), 
                                                                                            col_one_length=col_one_length, 
                                                                                            col_two_length=col_two_length, 
                                                                                            col_three_length=col_three_length))


def run(path):
    nice_table(get_files_by_size(path))