import os


def readfilecontent(path):
    print("Reading file content from " + path)

    if os.path.exists(path) == 0:
        print("The file does not exist")
    else:
        file = open(path,"r")

        for line in file:
            print(line)

def readfoldercontent(path):
    print("Reading folder contents : " + path)

    if os.path.exists(path) == 0:
        print("The folder does not exist")
    else:
        d = os.listdir(path)

        for item in d:
            print(item)