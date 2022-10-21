import os


def count_lines(file_name):
    with open(path + file_name) as file:
        count = sum(1 for line in file if line.strip())

        if count in file_list:
            pass
        else:
            file_list[count] = [file_name]


def make_new_file(files):
    for file in files:
        count_lines(file)
    print(file_list)


path = "./sortfiles/"
files = os.listdir(path)
file_list = {}
make_new_file(files)
