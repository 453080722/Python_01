import os


def listfile(dir, file, parameter, recursion):
    str = parameter.split(" ")
    for root, dirs, files in os.walk(dir):
        for name in files:
            for string in str:
                if (name.endswith(string)):
                    file.write(name + "\n")
                    break
                if (not recursion):
                    break


def TXT():
    dir = input("input path: ")
    outfile = "testlist.txt"
    parameter = ".vi"

    file = open(outfile, "w")
    if not file:
        print("error")
    listfile(dir, file, parameter, 0)
    file.close()


TXT()
