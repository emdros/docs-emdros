import sys
import os
import pprint

#
# pip install PyYAML
#
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

def read_file():
    fin = open("mkdocs.yml", "rb")
    data = load(fin, Loader=Loader)
    fin.close()

    return data

def make_files(data):
    pprint.pprint(data)

    make_files_recursive(data["pages"])

def make_files_recursive(data):
    if type(data) == type([]):
        print("UP200: type is list:")
        pprint.pprint(data)
        for inner in data:
            make_files_recursive(inner)
    elif type(data) == type({}):
        print("UP202: type is dict:")
        pprint.pprint(data)
        for inner in data:
            make_files_recursive(data[inner])
    elif type(data) == type(""):
        print("UP206: type is string:")
        pprint.pprint(data)
        if ".md" in data:
            make_file(data)
    else:
        print("UP209: Unknown data type: %s" % type(data))
        pprint(data)

def make_file(filename):
    real_path = os.path.join("docs", filename)
    print("UP220: Making filename: %s" % real_path)

    dirname = os.path.dirname(real_path)

    os.system("mkdir -p %s" % dirname)
    os.system("touch %s" % real_path)
    

def doIt():
    data = read_file()

    make_files(data)

if __name__ == '__main__':
    doIt()
    
        
        
        
