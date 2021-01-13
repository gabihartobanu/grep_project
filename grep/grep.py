import re
import os
import argparse

out_file = "D:\\files\\test"
global got_mutiple_files

def find_in_file(location, find_what, ignore_case_option, not_option, count_option):
    print("In functia de cautare")
    global got_mutiple_files

    count = 0

    file_handle = open(location, "r")

    if count_option:
        if not_option:
            if ignore_case_option:
                for line in file_handle.readlines():
                    if not re.search(find_what, line, re.IGNORECASE):
                        count += 1
                if got_mutiple_files:
                    print(location + ":" + count)
                else:
                    print(count)
            else:
                for line in file_handle.readlines():
                    if not re.search(find_what, line):
                        count += 1
                if got_mutiple_files:
                    print(location + ":" + count)
                else:
                    print(count)
        else:
            if ignore_case_option:
                for line in file_handle.readlines():
                    if re.search(find_what, line, re.IGNORECASE):
                        count += 1
                if count >= 1:
                    if got_mutiple_files:
                        print(location + ":" + count)
                    else:
                        print(count)
            else:
                for line in file_handle.readlines():
                    if re.search(find_what, line):
                        count += 1
                if count >= 1:
                    if got_mutiple_files:
                        print(location + ":" + count)
                    else:
                        print(count)
    else:
        if not_option:
            if ignore_case_option:
                for line in file_handle.readlines():
                    if not re.search(find_what, line, re.IGNORECASE):
                        if got_mutiple_files:
                            print(location + ":" + line[:-1])
                        else:
                            print(line[:-1])
            else:
                for line in file_handle.readlines():
                    if not re.search(find_what, line):
                        if got_mutiple_files:
                            print(location + ":" + line[:-1])
                        else:
                            print(line[:-1])
        else:
            if ignore_case_option:
                for line in file_handle.readlines():
                    if re.search(find_what, line, re.IGNORECASE):
                        if got_mutiple_files:
                            print(location + ":" + line[:-1])
                        else:
                            print(line[:-1])
            else:
                for line in file_handle.readlines():
                    if re.search(find_what, line):
                        if got_mutiple_files:
                            print(location + ":" + line[:-1])
                        else:
                            print(line[:-1])

    file_handle.close()


def find_in_location(location, find_what, ignore_case_option , not_option, count_option):
    global got_mutiple_files

    if os.path.exists(location):
        print("fisierul/directorul exista")
        if os.path.isdir(location):
            print("locatia e director")
            content = os.listdir(location)
            for file in content:
                new_location = os.path.join(location, file)
                find_in_location(new_location)
        elif os.path.isfile(location) and location[-4:] == ".txt":
            print("locatia este fisier")
            find_in_file(location, find_what, ignore_case_option, not_option, count_option)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Simulates some grep functionalities")
    parser.add_argument("--not_option", "-n", action='store_true', required=False, help="Verifica daca nu face match")
    parser.add_argument("--ignoreCase", "-i", action='store_true', required=False, help="Ignore case for search")
    parser.add_argument("--count", "-c", action='store_true', required=False, help="Count number of apariton in file")
    parser.add_argument("EXPRESION", metavar="e", type=str, help="Ce sa caute")
    parser.add_argument("PATH", type=str, metavar="p", help="Unde sa caute")
    args = parser.parse_args()

    not_option = args.not_option
    ignoreCase_option = args.ignoreCase
    count_option = args.count
    expresion = args.EXPRESION
    path = args.PATH

    global got_mutiple_files

    if os.path.exists(path) and os.path.isdir(path):
        got_mutiple_files = True
    else:
        got_mutiple_files = False

    find_in_location(path, expresion, ignoreCase_option, not_option, count_option)